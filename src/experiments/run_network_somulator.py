import numpy as np
from scipy.optimize import minimize

from src.qubo.problem_network import build_network_qubo
from src.qaoa.qaoa_circuit import build_qaoa_circuit
from src.backends.backend_simulator import SimulatorBackend

# Initial minimal version = 2 sources, 2 sinks, 1 battery
sources = ["A", "B"]
sinks = {"C": 1, "D": 1}
battery = "E"
costs = {"A": 2.0, "B": 3.0}
capacities = {"A": 1, "B": 1}

bqm, var_names = build_network_qubo(sources, sinks, battery, costs, capacities)
backend = SimulatorBackend()

p = 1

def objective(params):
    qc = build_qaoa_circuit(bqm, var_names, params, p)
    counts, E = backend.run(qc, bqm, var_names)
    print(params, "->", E)
    return E

init = [0.4] * (2*p)
result = minimize(objective, init, method="COBYLA", options={"maxiter": 20})
print("Optimal:", result.x)

# After optimization
best_params = result.x
qc = build_qaoa_circuit(bqm, var_names, best_params, p)
counts, E = backend.run(qc, bqm, var_names)

best = max(counts, key=counts.get)
print("\nBest bitstring:", best)

sample = {var_names[i]: int(best[i]) for i in range(len(var_names))}
print("Energy:", bqm.energy(sample))

print("\nActive flows:")
for v, val in sample.items():
    if val == 1:
        print(" ", v)
