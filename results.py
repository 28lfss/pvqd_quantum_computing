from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator

class ResultsProcessor:
    def __init__(self, estimator: StatevectorEstimator):
        """Store estimator used for recomputation."""
        self.estimator = estimator
    
    def display_results(self, result, hamiltonian: SparsePauliOp, zz_observable: SparsePauliOp):
        """Print core PVQD outputs."""
        print("\n=== Results ===")
        print(f"Times: {result.times}")
        print(f"Final parameters ({len(result.parameters[-1])}): {result.parameters[-1]}")
        print(f"Fidelities: {result.fidelities}")
        
        print("\nObservables per timestep [<H>, <ZZ>]:")
        for t, obs in zip(result.times, result.observables):
            print(f"t = {t:.3f}:  <H> = {obs[0]: .6f}, <ZZ> = {obs[1]: .6f}")
        
        evolved_state = result.evolved_state
        print("\nFinal evolved circuit:")
        print(evolved_state.decompose().draw())
        
        self._recompute_expectation_values(evolved_state, hamiltonian, zz_observable)
    
    def _recompute_expectation_values(self, evolved_state, hamiltonian: SparsePauliOp, 
                                      zz_observable: SparsePauliOp):
        """Recompute expectations locally as a quick check."""
        print("\nLocal check on final state:")
        
        pubs = [
            (evolved_state, [hamiltonian]),      # <H>
            (evolved_state, [zz_observable]),    # <ZZ>
        ]
        
        job = self.estimator.run(pubs)
        primitive_result = job.result()
        
        final_H = primitive_result[0].data.evs[0]
        final_ZZ = primitive_result[1].data.evs[0]
        
        print(f"<H> (final, recomputed)  = {final_H: .6f}")
        print(f"<ZZ> (final, recomputed) = {final_ZZ: .6f}")



