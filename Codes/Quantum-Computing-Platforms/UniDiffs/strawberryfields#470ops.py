--- strawberryfields/strawberryfields#470/after/ops.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#470/before/ops.py	2022-01-10 16:02:54.000000000 +0000
@@ -1088,11 +1088,9 @@
     else:
         batch_offset = 0
     num_modes = (num_indices - batch_offset) // 2  # always mixed
-    removed_cnt = 0
     for m in range(num_modes):
         if m != mode:
-            reduced_state = partial_trace(reduced_state, m - removed_cnt, False, batched)
-            removed_cnt += 1
+            reduced_state = partial_trace(reduced_state, m, False, batched)
     return reduced_state
 
 
