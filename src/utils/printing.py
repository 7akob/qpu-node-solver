def print_solution(counts, var_names):
    """Print the most likely bitstring + decoded variables."""
    best = max(counts, key=counts.get)
    print("\nBest bitstring:", best)
    for i, var in enumerate(var_names):
        print(f"  {var} = {best[i]}")
