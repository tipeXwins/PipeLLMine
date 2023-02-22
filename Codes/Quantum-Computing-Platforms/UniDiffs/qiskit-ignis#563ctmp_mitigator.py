--- qiskit-ignis/qiskit-ignis#563/after/ctmp_mitigator.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#563/before/ctmp_mitigator.py	2022-01-10 16:02:54.000000000 +0000
@@ -112,12 +112,12 @@
             which physical qubits these bit-values correspond to as
             ``circuit.measure(qubits, clbits)``.
         """
+        if qubits is None:
+            qubits = list(range(self._num_qubits))
         # Convert counts to probs
         probs, shots = counts_probability_vector(
-            counts, clbits=clbits, qubits=qubits, return_shots=True)
-        num_qubits = int(np.log2(probs.shape[0]))
-        if qubits is None:
-            qubits = list(range(num_qubits))
+            counts, clbits=clbits, qubits=qubits,
+            num_qubits=len(qubits), return_shots=True)
 
         # Ensure diagonal is a numpy vector so we can use fancy indexing
         if diagonal is None:
