--- pennylane/pennylane#1232/after/_device.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1232/before/_device.py	2022-01-10 16:02:54.000000000 +0000
@@ -296,10 +296,6 @@
         """
         return self._shot_vector
 
-    def _has_partitioned_shots(self):
-        return self._shot_vector is not None and (
-            len(self._shot_vector) > 1 or self._shot_vector[0].copies > 1
-        )
     def define_wire_map(self, wires):
         """Create the map from user-provided wire labels to the wire labels used by the device.
 
