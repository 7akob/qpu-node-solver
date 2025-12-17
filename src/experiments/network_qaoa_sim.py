"""
network_qaoa_sim.py

Goal:
- Build the validated 8-variable network QUBO
- Convert QUBO -> Ising (h, J)
- Run p=2 QAOA on Aer simulator
- Compare best sampled bitstring to brute-force QUBO optimum

Requires:
- qiskit
- qiskit-aer
- scipy
"""

from __future__ import annotations

import itertools
from typing import Dict, Tuple, List

import numpy as np
from scipy.optimize import minimize

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

from network_reference_solver import costs, var_names


# ----------------------------
# 1) Problem definition
# ----------------------------

index = {v: i for i, v in enumerate(var_names)}
P = 50.0  # penalty weight


# ----------------------------
# 2) QUBO helpers
# ----------------------------

Qubo = Dict[Tuple[int, int], float]


def add_qubo(Q: Qubo, i: int, j: int, w: float) -> None:
    a, b = (i, j) if i <= j else (j, i)
    Q[(a, b)] = Q.get((a, b), 0.0) + float(w)


def add_eq_one_constraint(Q: Qubo, vars_: List[int], P: float) -> None:
    for i in vars_:
        add_qubo(Q, i, i, -P)
    for a in range(len(vars_)):
        for b in range(a + 1, len(vars_)):
            add_qubo(Q, vars_[a], vars_[b], 2.0 * P)


def add_leq_one_constraint(Q: Qubo, vars_: List[int], P: float) -> None:
    for a in range(len(vars_)):
        for b in range(a + 1, len(vars_)):
            add_qubo(Q, vars_[a], vars_[b], P)


def add_battery_conservation(Q: Qubo, pos: List[int], neg: List[int], P: float) -> None:
    for i in pos + neg:
        add_qubo(Q, i, i, P)

    for group in (pos, neg):
        for a in range(len(group)):
            for b in range(a + 1, len(group)):
                add_qubo(Q, group[a], group[b], 2.0 * P)

    for i in pos:
        for j in neg:
            add_qubo(Q, i, j, -2.0 * P)


def build_qubo() -> Qubo:
    Q: Qubo = {}

    # Costs
    for v, c in costs.items():
        add_qubo(Q, index[v], index[v], c)

    # Sink constraints
    add_eq_one_constraint(Q, [index["f_A_C"], index["f_B_C"], index["f_E_C"]], P)
    add_eq_one_constraint(Q, [index["f_A_D"], index["f_B_D"], index["f_E_D"]], P)

    # Source capacities
    add_leq_one_constraint(Q, [index["f_A_C"], index["f_A_D"], index["f_A_E"]], P)
    add_leq_one_constraint(Q, [index["f_B_C"], index["f_B_D"], index["f_B_E"]], P)

    # Battery conservation
    add_battery_conservation(
        Q,
        pos=[index["f_A_E"], index["f_B_E"]],
        neg=[index["f_E_C"], index["f_E_D"]],
        P=P,
    )

    # Battery usage penalty
    BATTERY_COST = 2.0
    add_qubo(Q, index["f_A_E"], index["f_A_E"], BATTERY_COST)
    add_qubo(Q, index["f_B_E"], index["f_B_E"], BATTERY_COST)

    return Q


# ----------------------------
# 3) QUBO energy + brute force
# ----------------------------

def qubo_energy(bits: Tuple[int, ...], Q: Qubo) -> float:
    return sum(w * bits[i] * bits[j] for (i, j), w in Q.items())


def brute_force_best(Q: Qubo, n: int) -> Tuple[float, Tuple[int, ...]]:
    best_e = float("inf")
    best_bits = None
    for bits in itertools.product([0, 1], repeat=n):
        e = qubo_energy(bits, Q)
        if e < best_e:
            best_e = e
            best_bits = bits
    return best_e, best_bits  # type: ignore


# ----------------------------
# 4) QUBO -> Ising
# ----------------------------

def qubo_to_ising(Q: Qubo, n: int):
    const = 0.0
    h = np.zeros(n)
    J: Dict[Tuple[int, int], float] = {}

    for (i, j), w in Q.items():
        if i == j:
            const += w / 2
            h[i] -= w / 2
        else:
            const += w / 4
            h[i] -= w / 4
            h[j] -= w / 4
            J[(i, j)] = J.get((i, j), 0.0) + w / 4

    return const, h, J


# ----------------------------
# 5) QAOA p=2 circuit
# ----------------------------

def build_qaoa_circuit_p2(
    n: int,
    h: np.ndarray,
    J: Dict[Tuple[int, int], float],
    gamma1: float,
    beta1: float,
    gamma2: float,
    beta2: float,
) -> QuantumCircuit:

    qc = QuantumCircuit(n, n)
    qc.h(range(n))

    # Layer 1
    for i in range(n):
        if abs(h[i]) > 1e-12:
            qc.rz(2 * gamma1 * h[i], i)
    for (i, j), Jij in J.items():
        qc.rzz(2 * gamma1 * Jij, i, j)
    for i in range(n):
        qc.rx(2 * beta1, i)

    # Layer 2
    for i in range(n):
        if abs(h[i]) > 1e-12:
            qc.rz(2 * gamma2 * h[i], i)
    for (i, j), Jij in J.items():
        qc.rzz(2 * gamma2 * Jij, i, j)
    for i in range(n):
        qc.rx(2 * beta2, i)

    qc.measure(range(n), range(n))
    return qc


# ----------------------------
# 6) Run QAOA
# ----------------------------

def main():
    Q = build_qubo()
    n = len(var_names)

    ref_e, ref_bits = brute_force_best(Q, n)
    ref_bitstring = "".join(map(str, ref_bits))

    _, h, J = qubo_to_ising(Q, n)

    backend = Aer.get_backend("aer_simulator")
    shots = 1024

    def expected_qubo_energy(gb: np.ndarray) -> float:
        gamma1, beta1, gamma2, beta2 = map(float, gb)

        qc = build_qaoa_circuit_p2(
            n, h, J, gamma1, beta1, gamma2, beta2
        )
        qc_t = transpile(qc, backend)
        result = backend.run(qc_t, shots=shots).result()
        counts = result.get_counts()

        total = sum(counts.values())
        e = 0.0
        for bitstr, cnt in counts.items():
            bits = tuple(int(b) for b in bitstr[::-1])
            e += (cnt / total) * qubo_energy(bits, Q)

        print(
            f"gamma1={gamma1:.3f}, beta1={beta1:.3f}, "
            f"gamma2={gamma2:.3f}, beta2={beta2:.3f} -> E={e:.3f}"
        )
        return e

    print("\n=== Reference ===")
    print("Best QUBO energy:", ref_e)
    print("Best bitstring:", ref_bitstring)
    print("Active flows:", [var_names[i] for i, b in enumerate(ref_bits) if b])

    print("\n=== QAOA p=2 ===")
    init = np.array([0.3, 0.3, 0.1, 0.1])
    res = minimize(expected_qubo_energy, init, method="COBYLA", options={"maxiter": 40})

    print("\nOptimal parameters:", res.x)

    gamma1, beta1, gamma2, beta2 = res.x
    qc = build_qaoa_circuit_p2(n, h, J, gamma1, beta1, gamma2, beta2)
    qc_t = transpile(qc, backend)
    counts = backend.run(qc_t, shots=shots).result().get_counts()

    best = max(counts, key=counts.get)[::-1]
    bits = tuple(int(b) for b in best)

    print("\nMost frequent bitstring:", best)
    print("QUBO energy:", qubo_energy(bits, Q))
    print("Active flows:", [var_names[i] for i, b in enumerate(bits) if b])
    print("\nMatch reference?", best == ref_bitstring)


if __name__ == "__main__":
    main()
