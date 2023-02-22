--- strawberryfields/strawberryfields#470_B/after/ops.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#470_B/before/ops.py	2022-01-10 16:02:54.000000000 +0000
@@ -1077,9 +1077,7 @@
     return reduced_state
 
 
-def reduced_density_matrix(system, modes, state_is_pure, batched=False):
-    if isinstance(modes, int):
-        modes = [modes]
+def reduced_density_matrix(system, mode, state_is_pure, batched=False):
     if state_is_pure:
         reduced_state = mixed(system, batched)
     else:
@@ -1092,7 +1090,7 @@
     num_modes = (num_indices - batch_offset) // 2  # always mixed
     removed_cnt = 0
     for m in range(num_modes):
-        if m not in modes:
+        if m != mode:
             reduced_state = partial_trace(reduced_state, m - removed_cnt, False, batched)
             removed_cnt += 1
     return reduced_state
