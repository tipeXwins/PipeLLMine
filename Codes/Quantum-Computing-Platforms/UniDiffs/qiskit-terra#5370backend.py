--- qiskit-terra/qiskit-terra#5370/after/backend.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#5370/before/backend.py	2022-01-10 16:02:54.000000000 +0000
@@ -112,7 +112,7 @@
                 options
         """
         for field in fields:
-            if not hasattr(self._options, field):
+            if not hasattr(field, self._options):
                 raise AttributeError(
                     "Options field %s is not valid for this "
                     "backend" % field)
