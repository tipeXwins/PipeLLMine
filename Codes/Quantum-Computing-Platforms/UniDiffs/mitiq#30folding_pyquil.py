--- mitiq/mitiq#30/after/folding_pyquil.py	2022-01-10 16:02:54.000000000 +0000
+++ mitiq/mitiq#30/before/folding_pyquil.py	2022-01-10 16:02:54.000000000 +0000
@@ -2,7 +2,7 @@
 import numpy as np
 from pyquil import Program
 
-from mitiq.folding_cirq import _get_num_to_fold
+
 
 
 # Gate level folding
@@ -28,7 +28,7 @@
         np.random.seed(seed)
 
     ngates = len(circuit)
-    num_to_fold = _get_num_to_fold(stretch, ngates)
+    num_to_fold = int(ngates * (stretch - 1) / 2)
     sub_indices = np.random.choice(range(ngates), num_to_fold, replace=False)
     return fold_gates(circuit, sub_indices)
 
@@ -51,7 +51,7 @@
         raise ValueError("The stretch factor must be a real number within 1 and 3.")
 
     ngates = len(circuit)
-    num_to_fold = _get_num_to_fold(stretch, ngates)
+    num_to_fold = int(ngates * (stretch - 1) / 2)
     sub_indices = list(range(num_to_fold))
     return fold_gates(circuit, sub_indices)
 
@@ -125,7 +125,7 @@
 
     # partial circuit folding.
     ngates = len(circuit)
-    num_to_fold = _get_num_to_fold(stretch, ngates)
+    num_to_fold = int(ngates * fractional_stretch / 2)
     if num_to_fold != 0:
         out += circuit[-num_to_fold:].dagger() + circuit[-num_to_fold:]
 
