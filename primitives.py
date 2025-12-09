from qiskit.primitives import StatevectorSampler, StatevectorEstimator
from qiskit_algorithms.state_fidelities import ComputeUncompute

def setup_primitives():
    """Configure statevector sampler, estimator, and fidelity helper."""
    sampler = StatevectorSampler()
    estimator = StatevectorEstimator()
    fidelity = ComputeUncompute(sampler)
    
    return sampler, estimator, fidelity


