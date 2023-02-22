--- ProjectQ/ProjectQ#361/after/_plot.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#361/before/_plot.py	2022-01-10 16:02:54.000000000 +0000
@@ -223,13 +223,11 @@
 
     gate_grid = np.array([0] * (depth + 1), dtype=float)
 
-    gate_grid[0] = plot_params['labels_margin']
-    if depth > 0:
-        gate_grid[0] += width_list[0] * 0.5
-        for idx in range(1, depth):
-            gate_grid[idx] = gate_grid[idx - 1] + column_spacing + (
-                width_list[idx] + width_list[idx - 1]) * 0.5
-        gate_grid[-1] = gate_grid[-2] + column_spacing + width_list[-1] * 0.5
+    gate_grid[0] = plot_params['labels_margin'] + (width_list[0]) * 0.5
+    for idx in range(1, depth):
+        gate_grid[idx] = gate_grid[idx - 1] + column_spacing + (
+            width_list[idx] + width_list[idx - 1]) * 0.5
+    gate_grid[-1] = gate_grid[-2] + column_spacing + width_list[-1] * 0.5
     return gate_grid
 
 
