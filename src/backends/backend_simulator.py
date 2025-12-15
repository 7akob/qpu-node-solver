from qiskit_aer import AerSimulator
from src.qubo.qubo_utils import expected_energy

class SimulatorBackend:
    def __init__(self):
        self.backend = AerSimulator()

    def run(self, qc, bqm, var_names, shots=2048):
        job = self.backend.run(qc, shots=shots)
        result = job.result()
        counts = result.get_counts()
        energy = expected_energy(counts, bqm, var_names)
        return counts, energy
