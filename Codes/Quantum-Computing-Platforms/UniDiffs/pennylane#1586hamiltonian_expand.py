--- pennylane/pennylane#1586/after/hamiltonian_expand.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1586/before/hamiltonian_expand.py	2022-01-10 16:02:54.000000000 +0000
@@ -134,8 +134,8 @@
         if hamiltonian.grouping_indices is None:
             hamiltonian.compute_grouping()
 
-        coeff_groupings = [
-            qml.math.stack([hamiltonian.data[i] for i in indices])
+        coeffs = [
+            qml.math.squeeze(qml.math.take(hamiltonian.coeffs, indices, axis=0))
             for indices in hamiltonian.grouping_indices
         ]
         obs_groupings = [
@@ -154,26 +154,20 @@
 
             new_tape = new_tape.expand(stop_at=lambda obj: True)
             tapes.append(new_tape)
+    else:
+        coeffs = hamiltonian.coeffs
 
-        def processing_fn(res_groupings):
-            dot_products = [
-                qml.math.dot(r_group, c_group)
-                for c_group, r_group in zip(coeff_groupings, res_groupings)
-            ]
-            return qml.math.sum(qml.math.stack(dot_products), axis=0)
-
-        return tapes, processing_fn
-
-    coeffs = hamiltonian.data
-    tapes = []
-    for o in hamiltonian.ops:
-        with tape.__class__() as new_tape:
-            for op in tape.operations:
-                op.queue()
-            qml.expval(o)
-        tapes.append(new_tape)
+        tapes = []
+        for o in hamiltonian.ops:
+            with tape.__class__() as new_tape:
+                for op in tape.operations:
+                    op.queue()
+                qml.expval(o)
+
+            tapes.append(new_tape)
 
     def processing_fn(res):
+
         dot_products = [qml.math.dot(qml.math.squeeze(r), c) for c, r in zip(coeffs, res)]
         return qml.math.sum(qml.math.stack(dot_products), axis=0)
 
