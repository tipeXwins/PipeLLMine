--- amazon-braket-sdk-python/amazon-braket-sdk-python#268/after/circuit.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#268/before/circuit.py	2022-01-10 16:02:54.000000000 +0000
@@ -349,7 +349,7 @@
         self,
         instruction: Instruction,
         target: QubitSetInput = None,
-        target_mapping: Dict[QubitInput, QubitInput] = None,
+        target_mapping: Dict[QubitInput, QubitInput] = {},
     ) -> Circuit:
         """
         Add an instruction to `self`, returns `self` for chaining ability.
@@ -363,7 +363,7 @@
             target_mapping (dictionary[int or Qubit, int or Qubit], optional): A dictionary of
                 qubit mappings to apply to the `instruction.target`. Key is the qubit in
                 `instruction.target` and the value is what the key will be changed to.
-                Default = `None`.
+                Default = `{}`.
 
         Returns:
             Circuit: self
@@ -418,7 +418,7 @@
         self,
         circuit: Circuit,
         target: QubitSetInput = None,
-        target_mapping: Dict[QubitInput, QubitInput] = None,
+        target_mapping: Dict[QubitInput, QubitInput] = {},
     ) -> Circuit:
         """
         Add a `circuit` to self, returns self for chaining ability.
@@ -431,7 +431,7 @@
                 Default = `None`.
             target_mapping (dictionary[int or Qubit, int or Qubit], optional): A dictionary of
                 qubit mappings to apply to the qubits of `circuit.instructions`. Key is the qubit
-                to map, and the value is what to change it to. Default = `None`.
+                to map, and the value is what to change it to. Default = `{}`.
 
         Returns:
             Circuit: self
