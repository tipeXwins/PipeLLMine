--- tequila/tequila#95/after/simulator_qiskit.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#95/before/simulator_qiskit.py	2022-01-10 16:02:54.000000000 +0000
@@ -171,8 +171,6 @@
         self.counter = 0
 
         if qubit_map is None:
-            qubit_map = {q: i for i, q in enumerate(abstract_circuit.qubits)}
-        if qubit_map is None:
             n_qubits = len(abstract_circuit.qubits)
         else:
             n_qubits = max(qubit_map.values()) + 1
@@ -260,7 +258,7 @@
         if "optimization_level" in kwargs:
             optimization_level = kwargs['optimization_level']
 
-        opts = {}
+        opts = None
         if initial_state != 0:
             array = numpy.zeros(shape=[2 ** self.n_qubits])
             i = BitStringLSB.from_binary(BitString.from_int(integer=initial_state, nbits=self.n_qubits).binary)
@@ -271,7 +269,7 @@
 
         backend_result = qiskit.execute(experiments=self.circuit, optimization_level=optimization_level,
                                         backend=qiskit_backend, parameter_binds=[self.resolver],
-                                        **opts).result()
+                                        backend_options=opts).result()
         return QubitWaveFunction.from_array(arr=backend_result.get_statevector(self.circuit), numbering=self.numbering)
 
     def do_sample(self, circuit: qiskit.QuantumCircuit, samples: int, read_out_qubits, *args, **kwargs) -> QubitWaveFunction:
@@ -298,7 +296,7 @@
             qiskit_backend = self.retrieve_device('qasm_simulator')
         else:
             qiskit_backend = self.device
-        if qiskit_backend in qiskit.Aer.backends() or str(qiskit_backend).lower() in ["ibmq_qasm_simulator", "quasm_simulator"] or isinstance(qiskit_backend, qiskit.providers.aer.backends.qasm_simulator.QasmSimulator):
+        if qiskit_backend in qiskit.Aer.backends() or str(qiskit_backend).lower() == "ibmq_qasm_simulator":
             return self.convert_measurements(qiskit.execute(circuit, backend=qiskit_backend, shots=samples,
                                                             basis_gates=full_basis,
                                                             optimization_level=optimization_level,
@@ -321,7 +319,7 @@
                     print("WARNING: There are no noise models when running on real machines!")
                 return self.convert_measurements(qiskit.execute(circuit, backend=qiskit_backend, shots=samples,
                                                                 optimization_level=optimization_level,
-                                                                parameter_binds=[self.resolver]), target_qubits=read_out_qubits)
+                                                                parameter_binds=[self.resolver]))
 
     def convert_measurements(self, backend_result, target_qubits=None) -> QubitWaveFunction:
         """
