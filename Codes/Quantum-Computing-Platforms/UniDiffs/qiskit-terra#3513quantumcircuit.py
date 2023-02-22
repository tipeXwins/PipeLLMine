--- qiskit-terra/qiskit-terra#3513/after/quantumcircuit.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#3513/before/quantumcircuit.py	2022-01-10 16:02:54.000000000 +0000
@@ -901,8 +901,6 @@
             reg_map[reg.name] = reg_offset
             reg_offset += reg.size
 
-        if reg_offset == 0:
-            return 0
         # A list that holds the height of each qubit
         # and classical bit.
         op_stack = [0] * reg_offset
