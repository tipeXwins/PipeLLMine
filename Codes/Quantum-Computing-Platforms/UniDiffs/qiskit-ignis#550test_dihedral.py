--- qiskit-ignis/qiskit-ignis#550/after/test_dihedral.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#550/before/test_dihedral.py	2022-01-10 16:02:54.000000000 +0000
@@ -20,7 +20,7 @@
 import numpy as np
 from qiskit.circuit import QuantumCircuit
 from qiskit.quantum_info.operators import Operator
-from qiskit.quantum_info.operators import random
+from qiskit.quantum_info.operators.pauli import Pauli
 
 import qiskit
 # Import the dihedral_utils functions
@@ -480,7 +480,7 @@
         nseed = 999
         for qubit_num in range(1, 5):
             for i in range(samples):
-                pauli = random.random_pauli(qubit_num, seed=nseed + i)
+                pauli = Pauli.random(qubit_num, seed=nseed + i)
                 elem = CNOTDihedral(pauli)
                 value = Operator(pauli)
                 target = Operator(elem)
