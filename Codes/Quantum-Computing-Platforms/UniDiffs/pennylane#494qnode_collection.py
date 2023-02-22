--- pennylane/pennylane#494/after/qnode_collection.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#494/before/qnode_collection.py	2022-01-10 16:02:54.000000000 +0000
@@ -263,7 +263,7 @@
         if interface in ("autograd", "numpy"):
             from autograd import numpy as np
 
-            return np.stack(results)
+            return np.vstack(results)
 
         return results
 
