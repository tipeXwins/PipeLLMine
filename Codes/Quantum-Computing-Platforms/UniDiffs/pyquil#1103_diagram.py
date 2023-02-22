--- pyquil/pyquil#1103/after/_diagram.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#1103/before/_diagram.py	2022-01-10 16:02:54.000000000 +0000
@@ -465,11 +465,10 @@
                              f"qubits.")
 
         for q in control_qubits:
-            offset = target_qubits[0] - q
-            self.diagram.append(q, TIKZ_CONTROL(q, offset))
+            self.diagram.append(q, TIKZ_CONTROL(q, target_qubits[0]))
 
         # we put the gate on the first target line, and nop on the others
-        self.diagram.append(target_qubits[0], TIKZ_GATE(instr.name, size=len(target_qubits),
+        self.diagram.append(target_qubits[0], TIKZ_GATE(instr.name, size=len(qubits),
                                                         params=instr.params, dagger=dagger))
         for q in target_qubits[1:]:
             self.diagram.append(q, TIKZ_NOP())
