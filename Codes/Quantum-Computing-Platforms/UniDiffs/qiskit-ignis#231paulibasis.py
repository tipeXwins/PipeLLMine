--- qiskit-ignis/qiskit-ignis#231/after/paulibasis.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#231/before/paulibasis.py	2022-01-10 16:02:54.000000000 +0000
@@ -41,7 +41,7 @@
         A QuantumCircuit object.
     """
 
-    circ = QuantumCircuit(qubit.register, clbit.register)
+    circ = QuantumCircuit(qubit[0], clbit[0])
     if op == 'X':
         circ.h(qubit)
         circ.measure(qubit, clbit)
@@ -68,7 +68,7 @@
         A QuantumCircuit object.
     """
 
-    circ = QuantumCircuit(qubit.register)
+    circ = QuantumCircuit(qubit[0])
     if op == 'Xp':
         circ.h(qubit)
     if op == 'Xm':
