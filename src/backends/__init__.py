from src.backends.backend_simulator import SimulatorBackend
from src.backends.backend_ionq import IonQBackend
from src.backends.backend_iqm import IQMBackend

def get_backend(name: str):
    name = name.lower()

    if name in ("sim", "simulator", "aer"):
        return SimulatorBackend()
    elif name == "ionq":
        return IonQBackend()
    elif name == "iqm":
        return IQMBackend()
    else:
        raise ValueError(
            f"Unknown backend '{name}'. "
            "Choose from: sim | ionq | iqm"
        )
