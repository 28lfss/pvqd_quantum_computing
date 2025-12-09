from qiskit_algorithms.optimizers import L_BFGS_B
from qiskit_algorithms.time_evolvers import PVQD, TimeEvolutionProblem
from config import PVQDConfig
from circuit import create_ansatz, get_initial_parameters
from primitives import setup_primitives

class PVQDSolver:
    """Projected Variational Quantum Dynamics solver."""
    
    def __init__(self, config: PVQDConfig):
        """Create a solver from config."""
        self.config = config
        self.sampler, self.estimator, self.fidelity = setup_primitives()
        self.ansatz = create_ansatz(config)
        self.initial_parameters = get_initial_parameters(self.ansatz)
        self.optimizer = L_BFGS_B(maxfun=config.optimizer_maxfun)
        
        self.pvqd = PVQD(
            fidelity=self.fidelity,
            ansatz=self.ansatz,
            initial_parameters=self.initial_parameters,
            estimator=self.estimator,
            optimizer=self.optimizer,
            num_timesteps=config.num_timesteps,
        )
    
    def solve(self, hamiltonian, aux_operators=None):
        """Run PVQD time evolution."""
        time_evolution_problem = TimeEvolutionProblem(
            hamiltonian=hamiltonian,
            time=self.config.total_time,
            aux_operators=aux_operators,
        )
        
        result = self.pvqd.evolve(time_evolution_problem)
        return result



