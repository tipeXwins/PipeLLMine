--- amazon-braket-sdk-python/amazon-braket-sdk-python#268/after/instruction.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#268/before/instruction.py	2022-01-10 16:02:54.000000000 +0000
@@ -90,7 +90,7 @@
         return self._operator.to_ir([int(qubit) for qubit in self._target])
 
     def copy(
-        self, target_mapping: Dict[QubitInput, QubitInput] = None, target: QubitSetInput = None
+        self, target_mapping: Dict[QubitInput, QubitInput] = {}, target: QubitSetInput = None
     ) -> Instruction:
         """
         Return a shallow copy of the instruction.
@@ -129,7 +129,7 @@
         elif target is not None:
             return Instruction(self._operator, target)
         else:
-            return Instruction(self._operator, self._target.map(target_mapping or {}))
+            return Instruction(self._operator, self._target.map(target_mapping))
 
     def __repr__(self):
         return f"Instruction('operator': {self._operator}, 'target': {self._target})"
