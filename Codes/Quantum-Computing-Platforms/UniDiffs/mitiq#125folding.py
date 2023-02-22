--- mitiq/mitiq#125/after/folding.py	2022-01-10 16:02:54.000000000 +0000
+++ mitiq/mitiq#125/before/folding.py	2022-01-10 16:02:54.000000000 +0000
@@ -593,7 +593,7 @@
 
     # Fold remaining gates until the stretch is reached
     ops = list(base_circuit.all_operations())
-    num_to_fold = int(round(fractional_stretch * len(ops) / 2))
+    num_to_fold = int(round(fractional_stretch * len(ops)))
 
     if num_to_fold > 0:
         folded += Circuit([inverse(ops[-num_to_fold:])], [ops[-num_to_fold:]])
