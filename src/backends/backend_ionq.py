import os
from dotenv import load_dotenv
from qiskit import transpile
from qiskit_ionq import IonQProvider
from src.qubo.qubo_utils import expected_energy

load_dotenv()

class IonQBackend:
    def __init__(self, shots=512):
        api_key = os.getenv("IONQ_API_KEY")
        if not api_key:
            raise RuntimeError("IONQ_API_KEY not set")

        provider = IonQProvider(token=api_key)
        self.backend = provider.get_backend("ionq_qpu")  # or simulator
        self.shots = shots

    def run(self, qc, bqm, var_names):
        qc_t = transpile(qc, backend=self.backend, optimization_level=1)
        job = self.backend.run(qc_t, shots=self.shots)
        result = job.result()
        counts = result.get_counts()
        energy = expected_energy(counts, bqm, var_names)
        return counts, energy
