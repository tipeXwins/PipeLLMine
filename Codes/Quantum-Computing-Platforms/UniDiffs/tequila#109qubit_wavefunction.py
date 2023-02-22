--- tequila/tequila#109/after/qubit_wavefunction.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#109/before/qubit_wavefunction.py	2022-01-10 16:02:54.000000000 +0000
@@ -27,11 +27,7 @@
         self.n_qubits = keymap.n_qubits
         mapped_state = dict()
         for k, v in self.state.items():
-            mapped_key=keymap(input_state=k, initial_state=initial_state)
-            if mapped_key in mapped_state:
-                mapped_state[mapped_key] += v
-            else:
-                mapped_state[mapped_key] = v
+            mapped_state[keymap(input_state=k, initial_state=initial_state)] = v
 
         self.state = mapped_state
         return self
