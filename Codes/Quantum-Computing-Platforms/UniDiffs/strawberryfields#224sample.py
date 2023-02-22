--- strawberryfields/strawberryfields#224/after/sample.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#224/before/sample.py	2022-01-10 16:02:54.000000000 +0000
@@ -160,10 +160,7 @@
         else:
             sf.ops.MeasureFock() | q
 
-    s = eng.run(p, run_options={"shots": n_samples}).samples
-    if n_samples == 1:
-        return [s]
-    return s.tolist()
+    return eng.run(p, run_options={"shots": n_samples}).samples.tolist()
 
 
 def postselect(samples: list, min_count: int, max_count: int) -> list:
