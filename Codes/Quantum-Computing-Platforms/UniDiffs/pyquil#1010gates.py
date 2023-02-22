--- pyquil/pyquil#1010/after/gates.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#1010/before/gates.py	2022-01-10 16:02:54.000000000 +0000
@@ -58,7 +58,7 @@
     if isinstance(classical_reg2, int):
         raise TypeError("Left operand of comparison must be a memory address")
     classical_reg2 = unpack_classical_reg(classical_reg2)
-    if not isinstance(classical_reg3, int) and not isinstance(classical_reg3, float):
+    if not isinstance(classical_reg3, int):
         classical_reg3 = unpack_classical_reg(classical_reg3)
 
     return classical_reg1, classical_reg2, classical_reg3
@@ -639,14 +639,11 @@
     :param source: Source data. Can be either a MemoryReference or a constant.
     :return: A ClassicalStore instance.
     """
-    if not isinstance(source, int) and not isinstance(source, float):
-        source = unpack_classical_reg(source)
     return ClassicalStore(region_name, unpack_classical_reg(offset_reg), source)
 
 
 def CONVERT(classical_reg1, classical_reg2):
-    return ClassicalConvert(unpack_classical_reg(classical_reg1),
-                            unpack_classical_reg(classical_reg2))
+    return ClassicalConvert(classical_reg1, classical_reg2)
 
 
 def ADD(classical_reg, right):
