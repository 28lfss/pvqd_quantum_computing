import numpy as np
from qiskit.circuit.library import efficient_su2
from config import PVQDConfig

def create_ansatz(config: PVQDConfig):
    """Build the variational ansatz."""
    ansatz = efficient_su2(
        num_qubits=config.num_qubits,
        reps=config.ansatz_reps,
        entanglement=config.ansatz_entanglement,
    )
    return ansatz

def get_initial_parameters(ansatz) -> np.ndarray:
    """Return zeroed initial parameters."""
    return np.zeros(ansatz.num_parameters)


