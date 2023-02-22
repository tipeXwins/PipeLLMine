--- dwave-system/dwave-system#423/after/test_schedules.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#423/before/test_schedules.py	2022-01-10 16:02:54.000000000 +0000
@@ -15,7 +15,7 @@
 import os
 import unittest
 
-from dwave.cloud.exceptions import ConfigFileError, SolverNotFoundError
+from dwave.cloud.exceptions import ConfigFileError
 
 from dwave.system.schedules import ramp
 from dwave.system.samplers import DWaveSampler
@@ -27,7 +27,7 @@
     def setUpClass(cls):
         try:
             cls.qpu = DWaveSampler(solver=dict(h_gain_schedule=True))
-        except (ValueError, ConfigFileError, SolverNotFoundError):
+        except (ValueError, ConfigFileError):
             raise unittest.SkipTest("no qpu available")
 
     @classmethod
