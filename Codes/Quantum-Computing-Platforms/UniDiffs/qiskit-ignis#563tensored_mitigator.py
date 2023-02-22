--- qiskit-ignis/qiskit-ignis#563/after/tensored_mitigator.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#563/before/tensored_mitigator.py	2022-01-10 16:02:54.000000000 +0000
@@ -102,10 +102,10 @@
             counts, clbits=clbits, return_shots=True)
         num_qubits = int(np.log2(probs.shape[0]))
 
-        # Get qubit mitigation matrix and mitigate probs
-        if qubits is None:
-            qubits = range(num_qubits)
-        ainvs = self._mitigation_mats[list(qubits)]
+        if qubits is not None:
+            ainvs = self._mitigation_mats[list(qubits)]
+        else:
+            ainvs = self._mitigation_mats
 
         # Get operator coeffs
         if diagonal is None:
