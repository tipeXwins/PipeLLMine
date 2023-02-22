--- amazon-braket-sdk-python/amazon-braket-sdk-python#44/after/moments.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#44/before/moments.py	2022-01-10 16:02:54.000000000 +0000
@@ -138,7 +138,7 @@
             self._add(instruction)
 
     def _add(self, instruction: Instruction) -> None:
-        qubit_range = instruction.target
+        qubit_range = range(min(instruction.target), max(instruction.target) + 1)
         time = max([self._max_time_for_qubit(qubit) for qubit in qubit_range]) + 1
 
         # Mark all qubits in the range to avoid another gate being placed in the overlap.
