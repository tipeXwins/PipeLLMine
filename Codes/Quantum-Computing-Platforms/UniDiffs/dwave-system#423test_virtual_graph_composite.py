--- dwave-system/dwave-system#423/after/test_virtual_graph_composite.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#423/before/test_virtual_graph_composite.py	2022-01-10 16:02:54.000000000 +0000
@@ -19,7 +19,7 @@
 import minorminer
 import dimod.testing as dtest
 
-from dwave.cloud.exceptions import ConfigFileError, SolverNotFoundError
+from dwave.cloud.exceptions import ConfigFileError
 
 from dwave.system.composites import VirtualGraphComposite
 from dwave.system.samplers import DWaveSampler
@@ -32,7 +32,7 @@
     def setUpClass(cls):
         try:
             cls.qpu = DWaveSampler(solver=dict(flux_biases=True))
-        except (ValueError, ConfigFileError, SolverNotFoundError):
+        except (ValueError, ConfigFileError):
             raise unittest.SkipTest("no qpu available")
 
     @classmethod
