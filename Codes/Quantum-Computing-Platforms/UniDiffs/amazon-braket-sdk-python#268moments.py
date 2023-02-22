--- amazon-braket-sdk-python/amazon-braket-sdk-python#268/after/moments.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#268/before/moments.py	2022-01-10 16:02:54.000000000 +0000
@@ -106,13 +106,13 @@
             Value: Instruction('operator': H, 'target': QubitSet([Qubit(1)]))
     """
 
-    def __init__(self, instructions: Iterable[Instruction] = None):
+    def __init__(self, instructions: Iterable[Instruction] = []):
         self._moments: OrderedDict[MomentsKey, Instruction] = OrderedDict()
         self._max_times: Dict[Qubit, int] = {}
         self._qubits = QubitSet()
         self._depth = 0
 
-        self.add(instructions or [])
+        self.add(instructions)
 
     @property
     def depth(self) -> int:
