from config import PVQDConfig
from hamiltonian import create_ising_hamiltonian, create_zz_observable
from circuit import create_ansatz
from pvqd_solver import PVQDSolver
from results import ResultsProcessor
# Optional: Uncomment to enable IBM backend integration
# from ibm_backend import run_ibm_evaluation

def main():
    """Run the PVQD demo."""
    config = PVQDConfig()
    print("PVQD: local statevector demo")
    print(
        f"Config: qubits={config.num_qubits}, steps={config.num_timesteps}, "
        f"T={config.total_time}, optimizer_maxfun={config.optimizer_maxfun}"
    )

    hamiltonian = create_ising_hamiltonian(config)
    zz_observable = create_zz_observable()

    ansatz = create_ansatz(config)
    print(f"Ansatz: {ansatz.num_parameters} parameters on {ansatz.num_qubits} qubits")

    solver = PVQDSolver(config)
    print("Running PVQD...")
    result = solver.solve(
        hamiltonian=hamiltonian,
        aux_operators=[hamiltonian, zz_observable],  # needed for layout handling
    )
    results_processor = ResultsProcessor(solver.estimator)
    results_processor.display_results(result, hamiltonian, zz_observable)

    # OPTIONAL: enable IBM backend for a single final evaluation
    """
    print("IBM backend evaluation")
    ibm_result = run_ibm_evaluation(
        evolved_state=result.evolved_state,
        hamiltonian=hamiltonian,
        zz_observable=zz_observable
    )
    if ibm_result is None:
        print("Skipping IBM comparison (no backend or error).")
    """

if __name__ == "__main__":
    main()



