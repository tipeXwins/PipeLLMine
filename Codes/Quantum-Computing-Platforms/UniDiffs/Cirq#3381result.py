--- Cirq/Cirq#3381/after/result.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#3381/before/result.py	2022-01-10 16:02:54.000000000 +0000
@@ -22,7 +22,7 @@
 import pandas as pd
 
 from cirq import value, ops
-from cirq._compat import proper_repr, deprecated_class
+from cirq._compat import deprecated, proper_repr
 from cirq.study import resolver
 
 if TYPE_CHECKING:
@@ -323,9 +323,7 @@
             })
 
 
-@deprecated_class(deadline='v0.11',
-                  fix='Use cirq.Result instead.',
-                  name="cirq.TrialResult")
+@deprecated(deadline='v0.11', fix='Use cirq.Result instead.')
 class TrialResult(Result):
     pass
 
