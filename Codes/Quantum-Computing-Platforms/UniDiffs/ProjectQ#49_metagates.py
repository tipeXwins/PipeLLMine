--- ProjectQ/ProjectQ#49/after/_metagates.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#49/before/_metagates.py	2022-01-10 16:02:54.000000000 +0000
@@ -187,21 +187,22 @@
                 the gate.
         """
         qubits = BasicGate.make_tuple_of_qureg(qubits)
+        n = self._n
         ctrl = []
         gate_quregs = []
-        adding_to_controls = True
-        for reg in qubits:
-            if adding_to_controls:
-                ctrl += reg
-                adding_to_controls = len(ctrl) < self._n
+        added_ctrl_qubits = 0
+        for qureg in qubits:
+            if added_ctrl_qubits < n:
+                ctrl = ctrl + qureg
+                added_ctrl_qubits += len(qureg)
             else:
-                gate_quregs.append(reg)
-        # Test that there were enough control quregs and that that
+                gate_quregs.append(qureg)
+        # Test that there were enough control qubits and that that
         # the last control qubit was the last qubit in a qureg.
-        if len(ctrl) != self._n:
+        if added_ctrl_qubits != n:
             raise ControlQubitError("Wrong number of control qubits. "
                                     "First qureg(s) need to contain exactly "
-                                    "the required number of control quregs.")
+                                    "the required number of control qubits.")
         import projectq.meta
         with projectq.meta.Control(gate_quregs[0][0].engine, ctrl):
             self._gate | tuple(gate_quregs)
