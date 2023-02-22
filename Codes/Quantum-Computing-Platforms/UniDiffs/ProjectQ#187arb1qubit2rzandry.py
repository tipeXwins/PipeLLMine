--- ProjectQ/ProjectQ#187/after/arb1qubit2rzandry.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#187/before/arb1qubit2rzandry.py	2022-01-10 16:02:54.000000000 +0000
@@ -34,7 +34,7 @@
 import numpy
 
 from projectq.cengines import DecompositionRule
-from projectq.meta import Control, get_control_count
+from projectq.meta import Control
 from projectq.ops import BasicGate, Ph, Ry, Rz
 
 
@@ -45,7 +45,7 @@
     """ Recognize an arbitrary one qubit gate which has a matrix property."""
     try:
         m = cmd.gate.matrix
-        if len(m) == 2 and get_control_count(cmd) == 0:
+        if len(m) == 2:
             return True
         else:
             return False
