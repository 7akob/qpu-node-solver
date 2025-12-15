import os
from dotenv import load_dotenv
from iqm.qiskit_iqm import IQMProvider, transpile_to_IQM
from src.qubo.qubo_utils import expected_energy

load_dotenv()

class IQMBackend:
    def __init__(self, shots=512):
        server = os.getenv("IQM_SERVER_URL") or os.getenv("SERVER_URL")
        token = os.getenv("IQM_API_TOKEN") or os.getenv("RESONANCE_API_TOKEN")

        if not server or not token:
            raise RuntimeError("IQM credentials not set")

        provider = IQMProvider(server, token=token)
        self.backend = provider.get_backend()
        self.shots = shots

    def run(self, qc, bqm, var_names):
        qc_iqm = transpile_to_IQM(qc, self.backend)
        job = self.backend.run(qc_iqm, shots=self.shots)
        result = job.result()
        counts = result.get_counts()
        energy = expected_energy(counts, bqm, var_names)
        return counts, energy
