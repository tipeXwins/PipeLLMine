--- pennylane/pennylane#1243/after/adjoint.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1243/before/adjoint.py	2022-01-10 16:02:54.000000000 +0000
@@ -76,6 +76,6 @@
             try:
                 op.adjoint()
             except NotImplementedError:
-                adjoint(op.expand)()
+                adjoint(op.decomposition)(wires=op.wires)
 
     return wrapper
