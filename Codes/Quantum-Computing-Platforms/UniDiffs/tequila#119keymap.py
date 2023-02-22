--- tequila/tequila#119/after/keymap.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#119/before/keymap.py	2022-01-10 16:02:54.000000000 +0000
@@ -58,8 +58,8 @@
         return self.make_complement()
 
     def __init__(self, subregister: typing.List[int], register: typing.List[int]):
-        self._subregister = sorted(subregister)
-        self._register = sorted(register)
+        self._subregister = subregister
+        self._register = register
 
     def make_complement(self):
         return [i for i in self._register if i not in self._subregister]
