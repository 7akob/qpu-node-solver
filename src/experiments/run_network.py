import argparse
from scipy.optimize import minimize

from src.qubo.problem_network import build_network_qubo
from src.qaoa.qaoa_circuit import build_qaoa_circuit
from src.backends import get_backend

# ----------------------------
# CLI
# ----------------------------
parser = argparse.ArgumentParser()
parser.add_argument(
    "--backend",
    type=str,
    default="sim",
    help="Backend: sim | ionq | iqm"
)
args = parser.parse_args()

backend = get_backend(args.backend)
print(f"Using backend: {args.backend}")

# ----------------------------
# Network definition
# ----------------------------
sources = ["A", "B"]
sinks = {"C": 1, "D": 1}
battery = "E"

costs = {"A": 2.0, "B": 3.0}
capacities = {"A": 1, "B": 1}

bqm, var_names = build_network_qubo(
    sources,
    sinks,
    battery,
    costs,
    capacities,
    penalty=50.0   # IMPORTANT for hardware
)

# ----------------------------
# QAOA setup
# ----------------------------
p = 1
shots = 512

def objective(params):
    qc = build_qaoa_circuit(bqm, var_names, params, p)
    _, E = backend.run(qc, bqm, var_names)
    print("params:", params, "-> E:", round(E, 4))
    return E

init = [0.4] * (2 * p)

print("Starting optimization...")
res = minimize(
    objective,
    init,
    method="COBYLA",
    options={"maxiter": 6 if args.backend != "sim" else 20}
)

print("\nOptimal parameters:", res.x)

# ----------------------------
# Final run & decode
# ----------------------------
qc = build_qaoa_circuit(bqm, var_names, res.x, p)
counts, E = backend.run(qc, bqm, var_names)

best = max(counts, key=counts.get)
sample = {var_names[i]: int(best[i]) for i in range(len(var_names))}

print("\nBest bitstring:", best)
print("Energy:", bqm.energy(sample))

print("\nActive flows:")
for v, val in sample.items():
    if val == 1:
        print(" ", v)
