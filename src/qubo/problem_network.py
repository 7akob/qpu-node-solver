import itertools
import dimod

"""
General scalable network QUBO builder.
Initial version = 2 sources, 2 sinks, 1 battery.
Later, increase number of sources/sinks/batteries dynamically.
"""

def build_network_qubo(sources, sinks, battery, costs, capacities, penalty=8.0):
    """
    sources: list of source node names, e.g. ["A", "B"]
    sinks: dict of sink nodes and their demand, e.g. {"C":1, "D":1}
    battery: str, name of battery node, e.g. "E"
    costs: dict cost[source]
    capacities: dict Gmax[source]

    Returns: bqm, var_names
    """

    nodes = sources + list(sinks.keys()) + [battery]

    # Valid arcs for minimal network solver
    valid_arcs = [
        (i, j)
        for i in nodes
        for j in nodes
        if i != j and (
            (i in sources and j in sinks.keys()) or    # source -> sink
            (i in sources and j == battery) or         # source -> battery
            (i == battery and j in sinks.keys())       # battery -> sink
        )
    ]

    var_names = [f"f_{i}_{j}" for (i, j) in valid_arcs]
    linear, quadratic = {}, {}

    # --- Cost terms ---
    for v in var_names:
        src = v.split('_')[1]
        if src in sources:
            linear[v] = linear.get(v, 0) + costs[src]

    # --- Demand constraints (each sink must receive exactly demand units) ---
    for sink, demand in sinks.items():
        incoming = [v for v in var_names if v.endswith("_" + sink)]

        # (sum incoming - demand)^2
        for v in incoming:
            linear[v] = linear.get(v, 0) + penalty - 2 * penalty * demand

        for v1, v2 in itertools.combinations(incoming, 2):
            quadratic[(v1, v2)] = quadratic.get((v1, v2), 0) + 2 * penalty

    # --- Capacity constraints for sources ---
    for src in sources:
        outgoing = [v for v in var_names if v.startswith(f"f_{src}_")]
        cap = capacities[src]

        # Penalize > cap
        for v in outgoing:
            linear[v] = linear.get(v, 0) + penalty - 2 * penalty * cap

        for v1, v2 in itertools.combinations(outgoing, 2):
            quadratic[(v1, v2)] = quadratic.get((v1, v2), 0) + 2 * penalty

    # Build the BQM
    bqm = dimod.BinaryQuadraticModel(linear, quadratic, 0, dimod.BINARY)
    return bqm, var_names
