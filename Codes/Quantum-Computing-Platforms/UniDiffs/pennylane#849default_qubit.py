--- pennylane/pennylane#849/after/default_qubit.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#849/before/default_qubit.py	2022-01-10 16:02:54.000000000 +0000
@@ -414,7 +414,7 @@
 
         if (
             len(device_wires) == self.num_wires
-            and sorted(device_wires.labels) == device_wires.tolist()
+            and sorted(device_wires.labels) == device_wires.labels
         ):
             # Initialize the entire wires with the state
             self._state = self._reshape(state, [2] * self.num_wires)
