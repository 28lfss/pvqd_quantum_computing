from dataclasses import dataclass

@dataclass
class PVQDConfig:
    """PVQD simulation config."""
    # Hamiltonian parameters
    interaction_strength: float = 0.5  # J
    transverse_field: float = 0.1      # h_x
    # Simulation parameters
    num_qubits: int = 2
    num_timesteps: int = 10
    total_time: float = 1.0
    # Ansatz parameters
    ansatz_reps: int = 1
    ansatz_entanglement: str = "linear"
    # Optimizer parameters
    optimizer_maxfun: int = 20


