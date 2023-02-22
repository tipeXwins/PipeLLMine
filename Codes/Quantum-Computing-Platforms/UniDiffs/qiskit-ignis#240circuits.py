--- qiskit-ignis/qiskit-ignis#240/after/circuits.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#240/before/circuits.py	2022-01-10 16:02:54.000000000 +0000
@@ -65,13 +65,29 @@
     if qubit_list is None:
         qubit_list = range(len(qr))
 
+    cal_circuits = []
     nqubits = len(qubit_list)
 
+    # create classical bit registers
+    if cr is None:
+        cr = ClassicalRegister(nqubits)
+
     # labels for 2**n qubit states
     state_labels = count_keys(nqubits)
 
-    cal_circuits, _ = tensored_meas_cal([qubit_list],
-                                        qr, cr, circlabel)
+    for basis_state in state_labels:
+        qc_circuit = QuantumCircuit(qr, cr,
+                                    name='%scal_%s' % (circlabel, basis_state))
+        for qind, _ in enumerate(basis_state):
+            if int(basis_state[nqubits-qind-1]):
+                # the index labeling of the label is backwards with
+                # the list
+                qc_circuit.x(qr[qubit_list[qind]])
+
+            # add measurements
+            qc_circuit.measure(qr[qubit_list[qind]], cr[qind])
+
+        cal_circuits.append(qc_circuit)
 
     return cal_circuits, state_labels
 
