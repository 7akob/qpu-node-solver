"""
Ultra-simple network flow problem (classical QUBO).

Nodes:
Sources:
  A (capacity 1, cost 2)
  B (capacity 1, cost 3)

Sinks:
  C (demand 1)
  D (demand 1)

Battery / relay:
  E (optional)

Binary decision variables:
  f_A_C, f_A_D
  f_B_C, f_B_D
  f_A_E, f_B_E
  f_E_C, f_E_D

Goal:
  Minimize cost
  while satisfying:
    - source capacities
    - sink demands
    - battery flow conservation
"""

# Reference classical solver
# Used to validate all quantum results

import itertools

var_names = [
    "f_A_C", "f_A_D",
    "f_B_C", "f_B_D",
    "f_A_E", "f_B_E",
    "f_E_C", "f_E_D",
]

costs = {
    "f_A_C": 2,
    "f_A_D": 2,
    "f_A_E": 2,
    "f_B_C": 3,
    "f_B_D": 3,
    "f_B_E": 3,
}

P = 50  # penalty weight

def cost_term(sample):
    return sum(c * sample[v] for v, c in costs.items())

def sink_penalty(sample):
    C_in = sample["f_A_C"] + sample["f_B_C"] + sample["f_E_C"]
    D_in = sample["f_A_D"] + sample["f_B_D"] + sample["f_E_D"]
    return P * (1 - C_in)**2 + P * (1 - D_in)**2

def source_penalty(sample):
    A_out = sample["f_A_C"] + sample["f_A_D"] + sample["f_A_E"]
    B_out = sample["f_B_C"] + sample["f_B_D"] + sample["f_B_E"]
    return P * max(0, A_out - 1)**2 + P * max(0, B_out - 1)**2

def battery_penalty(sample):
    E_in = sample["f_A_E"] + sample["f_B_E"]
    E_out = sample["f_E_C"] + sample["f_E_D"]
    return P * (E_in - E_out)**2 + 0.5 * (sample["f_A_E"] + sample["f_B_E"])

def energy(sample):
    return (
        cost_term(sample)
        + sink_penalty(sample)
        + source_penalty(sample)
        + battery_penalty(sample)
    )


if __name__ == "__main__":
    best_E = float("inf")
    best_sample = None

    for bits in itertools.product([0, 1], repeat=len(var_names)):
        sample = dict(zip(var_names, bits))
        E = energy(sample)

        if E < best_E:
            best_E = E
            best_sample = sample

    print("Best energy:", best_E)
    print("Best solution:")
    for v, val in best_sample.items():
        if val == 1:
            print(" ", v)

    print("\nTotal cost:", cost_term(best_sample))

    print("\nConstraint check:")
    print("A out:", best_sample["f_A_C"] + best_sample["f_A_D"] + best_sample["f_A_E"])
    print("B out:", best_sample["f_B_C"] + best_sample["f_B_D"] + best_sample["f_B_E"])
    print("C in:", best_sample["f_A_C"] + best_sample["f_B_C"] + best_sample["f_E_C"])
    print("D in:", best_sample["f_A_D"] + best_sample["f_B_D"] + best_sample["f_E_D"])
    print("E in:", best_sample["f_A_E"] + best_sample["f_B_E"])
    print("E out:", best_sample["f_E_C"] + best_sample["f_E_D"])

