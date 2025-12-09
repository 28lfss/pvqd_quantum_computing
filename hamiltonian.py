from qiskit.quantum_info import SparsePauliOp
from config import PVQDConfig

def create_ising_hamiltonian(config: PVQDConfig) -> SparsePauliOp:
    """
    Build a 2-qubit Ising Hamiltonian.
    H = J*ZZ + h_x*(IX + XI)
    """
    J = config.interaction_strength
    h_x = config.transverse_field
    
    hamiltonian = J * SparsePauliOp(["ZZ"]) + h_x * (
        SparsePauliOp(["IX"]) + SparsePauliOp(["XI"])
    )
    
    return hamiltonian

def create_zz_observable() -> SparsePauliOp:
    """Return the ZZ observable."""
    return SparsePauliOp(["ZZ"])


