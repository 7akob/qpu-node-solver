"""
QUBO construction for ultra-simple network flow problem.

This QUBO is mathematically equivalent to the classical reference solver
and is used as input for QAOA / quantum backends.
"""

import itertools
from network_reference_solver import var_names, costs

# ----------------------------
# Variable indexing
# ----------------------------
index = {v: i for i, v in enumerate(var_names)}
n = len(var_names)

Q = {}
P = 50  # penalty weight

# ----------------------------
# 1. Cost terms (linear)
# ----------------------------
for v, c in costs.items():
    i = index[v]
    Q[(i, i)] = Q.get((i, i), 0) + c


# ----------------------------
# 2. Sink constraints (exactly one)
# (x_AC + x_BC + x_EC - 1)^2
# (x_AD + x_BD + x_ED - 1)^2
# ----------------------------
def add_exactly_one(indices):
    # linear: -P * xi
    for i in indices:
        Q[(i, i)] = Q.get((i, i), 0) - P

    # quadratic: +2P * xi xj
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            a, b = sorted((indices[i], indices[j]))
            Q[(a, b)] = Q.get((a, b), 0) + 2 * P


add_exactly_one([
    index["f_A_C"],
    index["f_B_C"],
    index["f_E_C"],
])

add_exactly_one([
    index["f_A_D"],
    index["f_B_D"],
    index["f_E_D"],
])


# ----------------------------
# 3. Source capacity constraints (at most one)
# P * (x_i x_j)
# ----------------------------
def add_at_most_one(indices):
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            a, b = sorted((indices[i], indices[j]))
            Q[(a, b)] = Q.get((a, b), 0) + P


add_at_most_one([
    index["f_A_C"],
    index["f_A_D"],
    index["f_A_E"],
])

add_at_most_one([
    index["f_B_C"],
    index["f_B_D"],
    index["f_B_E"],
])


# ----------------------------
# 4. Battery conservation
# (x_AE + x_BE - x_EC - x_ED)^2
# ----------------------------
pos = [index["f_A_E"], index["f_B_E"]]
neg = [index["f_E_C"], index["f_E_D"]]

# diagonal terms
for i in pos + neg:
    Q[(i, i)] = Q.get((i, i), 0) + P

# same-sign pairs
Q[(min(pos), max(pos))] = Q.get((min(pos), max(pos)), 0) + 2 * P
Q[(min(neg), max(neg))] = Q.get((min(neg), max(neg)), 0) + 2 * P

# opposite-sign pairs
for i in pos:
    for j in neg:
        a, b = sorted((i, j))
        Q[(a, b)] = Q.get((a, b), 0) - 2 * P


# ----------------------------
# 5. Battery usage penalty (soft bias)
# ----------------------------
Q[(index["f_A_E"], index["f_A_E"])] += 0.5
Q[(index["f_B_E"], index["f_B_E"])] += 0.5


# ----------------------------
# 6. Brute-force validation
# ----------------------------
def qubo_energy(bits):
    E = 0.0
    for (i, j), w in Q.items():
        E += w * bits[i] * bits[j]
    return E


best_E = float("inf")
best_bits = None

for bits in itertools.product([0, 1], repeat=n):
    E = qubo_energy(bits)
    if E < best_E:
        best_E = E
        best_bits = bits

print("\n=== QUBO brute-force check ===")
print("Best QUBO energy:", best_E)
print("Best bitstring:", "".join(map(str, best_bits)))
print("Active flows:")
for i, b in enumerate(best_bits):
    if b == 1:
        print(" ", var_names[i])
