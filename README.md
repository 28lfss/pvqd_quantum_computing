# PVQD Quantum Computing

A Python implementation of Projected Variational Quantum Dynamics (PVQD) for simulating quantum time evolution using Qiskit. This project demonstrates variational quantum algorithms for solving time-dependent quantum problems on both local simulators and IBM Quantum hardware.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Examples](#examples)
- [Requirements](#requirements)
- [IBM Quantum Integration](#ibm-quantum-integration)

## Overview

Projected Variational Quantum Dynamics (PVQD) is a variational algorithm for simulating quantum time evolution. This implementation uses Qiskit's algorithms library to solve time evolution problems by projecting the exact evolution onto a parameterized quantum circuit (ansatz).

The project focuses on:
- Simulating time evolution of quantum systems using variational methods
- Computing expectation values of observables during evolution
- Supporting both local statevector simulation and IBM Quantum hardware
- Demonstrating PVQD on Ising model Hamiltonians

## Features

- **PVQD Solver**: Implementation of the Projected Variational Quantum Dynamics algorithm
- **Ising Model Support**: Built-in Ising Hamiltonian construction with configurable parameters
- **Flexible Ansatz**: Uses Qiskit's EfficientSU2 ansatz with customizable depth and entanglement
- **Local Simulation**: Fast statevector-based simulation for development and testing
- **IBM Quantum Integration**: Optional support for running evaluations on IBM Quantum hardware
- **Results Processing**: Comprehensive results display including fidelities, observables, and expectation values

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pvqd_quantum_computing
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) For IBM Quantum integration, create a `.env` file:
```
IBM_API_KEY=your_api_key_here
```

## Configuration

The project uses a configuration class (`PVQDConfig`) to manage simulation parameters. Default values can be modified in `config.py`:

```python
@dataclass
class PVQDConfig:
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
```

### Configuration Parameters

- **interaction_strength** (J): Strength of the ZZ interaction term in the Ising Hamiltonian
- **transverse_field** (h_x): Strength of the transverse field (IX + XI terms)
- **num_qubits**: Number of qubits in the system
- **num_timesteps**: Number of time steps for the evolution
- **total_time**: Total evolution time
- **ansatz_reps**: Number of repetitions in the ansatz circuit
- **ansatz_entanglement**: Entanglement pattern ("linear", "full", etc.)
- **optimizer_maxfun**: Maximum number of function evaluations for the optimizer

## Usage

### Basic Usage

Run the main script to execute a PVQD simulation:

```bash
python main.py
```

This will:
1. Create an Ising Hamiltonian based on the configuration
2. Initialize a variational ansatz circuit
3. Run PVQD time evolution
4. Display results including fidelities, observables, and expectation values

### Programmatic Usage

```python
from config import PVQDConfig
from hamiltonian import create_ising_hamiltonian, create_zz_observable
from circuit import create_ansatz
from pvqd_solver import PVQDSolver
from results import ResultsProcessor

# Create configuration
config = PVQDConfig(
    num_qubits=2,
    num_timesteps=10,
    total_time=1.0
)

# Build Hamiltonian and observables
hamiltonian = create_ising_hamiltonian(config)
zz_observable = create_zz_observable()

# Create solver and run
solver = PVQDSolver(config)
result = solver.solve(
    hamiltonian=hamiltonian,
    aux_operators=[hamiltonian, zz_observable]
)

# Process and display results
results_processor = ResultsProcessor(solver.estimator)
results_processor.display_results(result, hamiltonian, zz_observable)
```

## Project Structure

```
pvqd_quantum_computing/
├── main.py                 # Main entry point
├── config.py               # Configuration dataclass
├── hamiltonian.py          # Hamiltonian construction
├── circuit.py              # Ansatz circuit creation
├── pvqd_solver.py          # PVQD solver implementation
├── primitives.py           # Qiskit primitives setup
├── results.py              # Results processing and display
├── ibm_backend.py          # IBM Quantum integration (optional)
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── presentation/           # Presentation materials
    ├── slides.tex         # LaTeX presentation
    └── code_images/       # Code screenshots
```

## API Documentation

### PVQDConfig

Configuration dataclass for PVQD simulation parameters.

**Attributes:**
- `interaction_strength` (float): Ising interaction strength J
- `transverse_field` (float): Transverse field strength h_x
- `num_qubits` (int): Number of qubits
- `num_timesteps` (int): Number of time steps
- `total_time` (float): Total evolution time
- `ansatz_reps` (int): Ansatz repetition count
- `ansatz_entanglement` (str): Entanglement pattern
- `optimizer_maxfun` (int): Optimizer maximum function evaluations

### PVQDSolver

Main solver class for PVQD time evolution.

**Methods:**
- `__init__(config: PVQDConfig)`: Initialize solver with configuration
- `solve(hamiltonian, aux_operators=None)`: Run PVQD evolution and return result

**Returns:**
- `TimeEvolutionResult`: Contains evolved state, parameters, fidelities, times, and observables

### create_ising_hamiltonian

Creates a 2-qubit Ising Hamiltonian: H = J*ZZ + h_x*(IX + XI)

**Parameters:**
- `config` (PVQDConfig): Configuration with interaction_strength and transverse_field

**Returns:**
- `SparsePauliOp`: Ising Hamiltonian operator

### create_ansatz

Creates a variational ansatz circuit using Qiskit's EfficientSU2.

**Parameters:**
- `config` (PVQDConfig): Configuration with ansatz parameters

**Returns:**
- `QuantumCircuit`: Parameterized ansatz circuit

### ResultsProcessor

Processes and displays PVQD results.

**Methods:**
- `__init__(estimator)`: Initialize with a statevector estimator
- `display_results(result, hamiltonian, zz_observable)`: Print comprehensive results

### run_ibm_evaluation

(Optional) Run evaluation on IBM Quantum hardware.

**Parameters:**
- `evolved_state`: Final evolved quantum circuit
- `hamiltonian`: Hamiltonian operator
- `zz_observable`: ZZ observable operator

**Returns:**
- `Tuple[float, float]` or `None`: Expectation values (H, ZZ) or None if failed

## Examples

### Custom Configuration

```python
from config import PVQDConfig
from main import main

# Modify configuration
config = PVQDConfig(
    num_qubits=3,
    num_timesteps=20,
    total_time=2.0,
    interaction_strength=1.0,
    transverse_field=0.5,
    ansatz_reps=2,
    optimizer_maxfun=50
)
```

### IBM Quantum Evaluation

To enable IBM Quantum hardware evaluation, uncomment the relevant section in `main.py`:

```python
from ibm_backend import run_ibm_evaluation

ibm_result = run_ibm_evaluation(
    evolved_state=result.evolved_state,
    hamiltonian=hamiltonian,
    zz_observable=zz_observable
)
```

Ensure you have set `IBM_API_KEY` in your `.env` file.

## Requirements

The project requires the following Python packages:

- `qiskit`: Core quantum computing framework
- `qiskit-ibm-runtime`: IBM Quantum runtime integration (optional)
- `qiskit-algorithms`: Quantum algorithms including PVQD
- `python-dotenv`: Environment variable management

See `requirements.txt` for specific versions.

## IBM Quantum Integration

The project includes optional support for running evaluations on IBM Quantum hardware. To use this feature:

1. Obtain an IBM Quantum API key from [IBM Quantum](https://quantum.ibm.com/)
2. Create a `.env` file in the project root:
   ```
   IBM_API_KEY=your_api_key_here
   ```
3. Uncomment the IBM evaluation section in `main.py`

The IBM backend integration will:
- Automatically select the least busy available backend
- Transpile the circuit to match backend gates
- Compute expectation values on real quantum hardware
- Compare results with local simulation

Note: IBM Quantum integration requires an active account and may incur usage costs.

## License

[Add license information here]

## Contributing

[Add contributing guidelines here]

