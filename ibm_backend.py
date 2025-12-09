import os
from typing import Optional, Tuple
from dotenv import load_dotenv
from qiskit import transpile
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import (
    QiskitRuntimeService,
    EstimatorV2 as IBMEstimator,
)

def setup_ibm_backend() -> Tuple[IBMEstimator, object]:
    load_dotenv()
    api_key = os.getenv("IBM_API_KEY")

    if api_key is None:
        raise RuntimeError(
            "IBM_API_KEY not found in environment (.env). "
            "Set it or disable IBM evaluation."
        )

    service = QiskitRuntimeService(
        channel="ibm_quantum_platform",
        token=api_key,
    )

    backend = service.least_busy(
        operational=True,
        simulator=False,
        min_num_qubits=2,
    )
    ibm_estimator = IBMEstimator(mode=backend)
    return ibm_estimator, backend

def compute_ibm_expectation_values(
    ibm_estimator: IBMEstimator,
    backend,
    evolved_state,
    hamiltonian: SparsePauliOp,
    zz_observable: SparsePauliOp,
) -> Tuple[float, float]:
    basis_gates = sorted(list(backend.target.operation_names))

    transpiled_circuit = transpile(
        evolved_state,
        basis_gates=basis_gates,
        optimization_level=1,
    )

    pubs = [
        (transpiled_circuit, [hamiltonian, zz_observable], None, None)
    ]

    ibm_job = ibm_estimator.run(pubs)
    results = ibm_job.result()
    pub_result = results[0]

    ibm_H, ibm_ZZ = pub_result.data.evs

    return float(ibm_H), float(ibm_ZZ)


def run_ibm_evaluation(
    evolved_state,
    hamiltonian: SparsePauliOp,
    zz_observable: SparsePauliOp,
) -> Optional[Tuple[float, float]]:
    try:
        ibm_estimator, backend = setup_ibm_backend()
        ibm_H, ibm_ZZ = compute_ibm_expectation_values(
            ibm_estimator,
            backend,
            evolved_state,
            hamiltonian,
            zz_observable,
        )

        print(f"\nIBM backend: {backend.name}")
        print(f"IBM <H>  = {ibm_H: .6f}")
        print(f"IBM <ZZ> = {ibm_ZZ: .6f}")

        return ibm_H, ibm_ZZ

    except Exception as e:
        print(f"\nWarning: IBM backend evaluation failed: {e}")
        return None
