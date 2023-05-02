22c22
< from qiskit.quantum_info import state_fidelity, Statevector
---
> from qiskit.quantum_info import state_fidelity
28c28,29
<     psi = Statevector.from_instruction(circuit)
---
>     job = qiskit.execute(circuit, Aer.get_backend('statevector_simulator'))
>     psi = job.result().get_statevector(circuit)
67c68
<         F_bell_cvx = state_fidelity(psi, rho_cvx, validate=False)
---
>         F_bell_cvx = state_fidelity(psi, rho_cvx)
69c70
<         F_bell_mle = state_fidelity(psi, rho_mle, validate=False)
---
>         F_bell_mle = state_fidelity(psi, rho_mle)
80c81
<         F_bell_cvx = state_fidelity(psi, rho_cvx, validate=False)
---
>         F_bell_cvx = state_fidelity(psi, rho_cvx)
82c83
<         F_bell_mle = state_fidelity(psi, rho_mle, validate=False)
---
>         F_bell_mle = state_fidelity(psi, rho_mle)
91c92
<         F_bell_cvx = state_fidelity(psi, rho_cvx, validate=False)
---
>         F_bell_cvx = state_fidelity(psi, rho_cvx)
93c94
<         F_bell_mle = state_fidelity(psi, rho_mle, validate=False)
---
>         F_bell_mle = state_fidelity(psi, rho_mle)
107c108
<         F_bell_cvx = state_fidelity(psi, rho_cvx, validate=False)
---
>         F_bell_cvx = state_fidelity(psi, rho_cvx)
109c110
<         F_bell_mle = state_fidelity(psi, rho_mle, validate=False)
---
>         F_bell_mle = state_fidelity(psi, rho_mle)
