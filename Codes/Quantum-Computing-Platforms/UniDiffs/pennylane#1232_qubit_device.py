--- pennylane/pennylane#1232/after/_qubit_device.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1232/before/_qubit_device.py	2022-01-10 16:02:54.000000000 +0000
@@ -187,7 +187,6 @@
         if self.shots is not None or circuit.is_sampled:
             self._samples = self.generate_samples()
 
-        multiple_sampled_jobs = circuit.is_sampled and self._has_partitioned_shots()
         # compute the required statistics
         if not self.analytic and self._shot_vector is not None:
 
@@ -204,17 +203,16 @@
                 if shot_tuple.copies > 1:
                     results.extend(r.T)
                 else:
-                    results.append(r.T)
+                    results.append(r)
 
                 s1 = s2
 
-            if not multiple_sampled_jobs:
-                results = qml.math.stack(results)
+            results = qml.math.stack(results)
 
         else:
             results = self.statistics(circuit.observables)
 
-        if (circuit.all_sampled or not circuit.is_sampled) and not multiple_sampled_jobs:
+        if circuit.all_sampled or not circuit.is_sampled:
             results = self._asarray(results)
         else:
             results = tuple(self._asarray(r) for r in results)
