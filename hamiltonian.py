from qiskit.quantum_info import SparsePauliOp
from config import PVQDConfig

def create_ising_hamiltonian(config: PVQDConfig) -> SparsePauliOp:
    """
    Build an N-qubit 1D Ising Hamiltonian:
        H = J * sum_{i} Z_i Z_{i+1} + h_x * sum_{i} X_i
    """
    J = config.interaction_strength
    h_x = config.transverse_field
    n = config.num_qubits

    paulis = []
    coeffs = []

    # ZZ nearest-neighbor couplings
    for i in range(n - 1):
        zstring = ["I"] * n
        zstring[i] = "Z"
        zstring[i + 1] = "Z"
        paulis.append("".join(zstring))
        coeffs.append(J)

    # Transverse field X terms
    for i in range(n):
        xstring = ["I"] * n
        xstring[i] = "X"
        paulis.append("".join(xstring))
        coeffs.append(h_x)

    return SparsePauliOp(paulis, coeffs)

def create_zz_observable(config: PVQDConfig) -> SparsePauliOp:
    """
    Return sum of nearest-neighbor ZZ terms:
        O_ZZ = sum_i Z_i Z_{i+1}
    """
    n = config.num_qubits
    paulis = []
    coeffs = []

    for i in range(n - 1):
        zstring = ["I"] * n
        zstring[i] = "Z"
        zstring[i + 1] = "Z"
        paulis.append("".join(zstring))
        coeffs.append(1.0)

    return SparsePauliOp(paulis, coeffs)
