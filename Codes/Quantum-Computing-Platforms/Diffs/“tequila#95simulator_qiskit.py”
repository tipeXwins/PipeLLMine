174,175d173
<             qubit_map = {q: i for i, q in enumerate(abstract_circuit.qubits)}
<         if qubit_map is None:
263c261
<         opts = {}
---
>         opts = None
274c272
<                                         **opts).result()
---
>                                         backend_options=opts).result()
301c299
<         if qiskit_backend in qiskit.Aer.backends() or str(qiskit_backend).lower() in ["ibmq_qasm_simulator", "quasm_simulator"] or isinstance(qiskit_backend, qiskit.providers.aer.backends.qasm_simulator.QasmSimulator):
---
>         if qiskit_backend in qiskit.Aer.backends() or str(qiskit_backend).lower() == "ibmq_qasm_simulator":
324c322
<                                                                 parameter_binds=[self.resolver]), target_qubits=read_out_qubits)
---
>                                                                 parameter_binds=[self.resolver]))
