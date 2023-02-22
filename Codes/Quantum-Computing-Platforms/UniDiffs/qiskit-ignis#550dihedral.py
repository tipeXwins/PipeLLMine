--- qiskit-ignis/qiskit-ignis#550/after/dihedral.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#550/before/dihedral.py	2022-01-10 16:02:54.000000000 +0000
@@ -401,7 +401,8 @@
             self.shift = elem.shift
 
         # Initialize BaseOperator
-        super().__init__(num_qubits=self._num_qubits)
+        dims = self._num_qubits * (2,)
+        super().__init__(dims, dims)
 
         # Validate the CNOTDihedral element
         if validate and not self.is_cnotdihedral():
@@ -590,7 +591,7 @@
             circuit = circuit.to_instruction()
 
         # Initialize an identity CNOTDihedral object
-        elem = CNOTDihedral(self._num_qubits)
+        elem = CNOTDihedral(self.num_qubits)
         append_circuit(elem, circuit)
         return elem
 
