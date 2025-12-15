import os
from iqm.qiskit_iqm import IQMProvider
from qiskit.primitives import Sampler

class IQMBackend:
    def __init__(self, shots=1024):
        url = os.environ["IQM_URL"]
        device = os.environ["IQM_DEVICE"]
        token = os.environ.get("IQM_TOKEN", None)

        provider = IQMProvider(
            url=url,
            token=token
        )

        self.backend = provider.get_backend(device)
        self.sampler = Sampler(backend=self.backend)
        self.shots = shots

        print(f"Connected to IQM backend: {self.backend.name()}")

    def run(self, qc, bqm, var_names):
        job = self.sampler.run(
            circuits=[qc],
            shots=self.shots
        )
        result = job.result()

        counts = result.quasi_dists[0]
        energy = bqm.energy_from_samples(counts, var_names)

        return counts, energy
