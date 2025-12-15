import os
from dotenv import load_dotenv
from qiskit import transpile
from qiskit_ionq import IonQProvider

load_dotenv()


class IonQBackend:
    def __init__(self, shots=512, use_qpu=False):
        token = os.getenv("IONQ_API_KEY")
        if not token:
            raise RuntimeError("IONQ_API_KEY not set")

        provider = IonQProvider(token=token)

        if use_qpu:
            self.backend = provider.get_backend("ionq_qpu")
        else:
            self.backend = provider.get_backend("ionq_simulator")

        self.shots = shots
        print("Connected to IonQ backend:", self.backend.name())

    def run(self, qc, bqm, var_names):
        qc_t = transpile(qc, backend=self.backend, optimization_level=1)
        job = self.backend.run(qc_t, shots=self.shots)
        result = job.result()
        counts = result.get_counts()

        # energy calculation (same as before)
        total = sum(counts.values())
        energy = 0.0
        for bitstr, cnt in counts.items():
            sample = {v: int(bitstr[i]) for i, v in enumerate(var_names)}
            energy += (cnt / total) * bqm.energy(sample)

        return counts, energy
