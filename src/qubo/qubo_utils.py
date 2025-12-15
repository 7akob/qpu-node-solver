def decode_sample(bitstring, var_names):
    """Convert measurement bitstring (e.g. '1010') → dict var -> 0/1"""
    return {var_names[i]: int(bitstring[i]) for i in range(len(var_names))}

def expected_energy(counts, bqm, var_names):
    total = sum(counts.values())
    E = 0
    for bitstring, c in counts.items():
        sample = decode_sample(bitstring, var_names)
        E += (c/total) * bqm.energy(sample)
    return E
