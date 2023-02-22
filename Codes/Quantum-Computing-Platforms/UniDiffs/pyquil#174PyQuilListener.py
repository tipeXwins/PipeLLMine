--- pyquil/pyquil#174/after/PyQuilListener.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#174/before/PyQuilListener.py	2022-01-10 16:02:54.000000000 +0000
@@ -2,7 +2,6 @@
 from typing import Any, List
 
 import sys
-import numpy as np
 from antlr4 import *
 from antlr4.IntervalSet import IntervalSet
 from antlr4.Token import CommonToken
@@ -284,8 +283,6 @@
         return complex(0, _real(number.imaginaryN().realN()))
     elif number.I():
         return complex(0, 1)
-    elif number.PI():
-        return np.pi
     else:
         raise RuntimeError("Unexpected number: " + str(number))
 
