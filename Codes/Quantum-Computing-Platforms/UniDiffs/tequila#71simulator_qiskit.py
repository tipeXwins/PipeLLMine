--- tequila/tequila#71/after/simulator_qiskit.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#71/before/simulator_qiskit.py	2022-01-10 16:02:54.000000000 +0000
@@ -173,7 +173,7 @@
         self.counter = 0
 
         if qubit_map is None:
-            n_qubits = len(abstract_circuit.qubits)
+            n_qubits = abstract_circuit.n_qubits
         else:
             n_qubits = max(qubit_map.values()) + 1
 
