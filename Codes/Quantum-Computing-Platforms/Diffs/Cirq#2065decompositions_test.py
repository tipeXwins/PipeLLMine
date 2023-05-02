238c238,239
<     gates = cirq.single_qubit_matrix_to_phased_x_z(intended_effect, atol=1e-6)
---
>     gates = cirq.single_qubit_matrix_to_phased_x_z(
>         intended_effect, atol=0.0001)
240c241
<     assert_gates_implement_unitary(gates, intended_effect, atol=1e-5)
---
>     assert_gates_implement_unitary(gates, intended_effect, atol=1e-8)
