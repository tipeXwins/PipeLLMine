--- qiskit-terra/qiskit-terra#342/after/_coupling.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#342/before/_coupling.py	2022-01-10 16:02:54.000000000 +0000
@@ -109,7 +109,7 @@
         return len(self.qubits)
 
     def get_qubits(self):
-        return sorted(list(self.qubits.keys()))
+        return list(self.qubits.keys())
 
     def get_edges(self):
         """Return a list of edges in the coupling graph.
