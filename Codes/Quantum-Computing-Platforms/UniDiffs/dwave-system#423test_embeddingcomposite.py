--- dwave-system/dwave-system#423/after/test_embeddingcomposite.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#423/before/test_embeddingcomposite.py	2022-01-10 16:02:54.000000000 +0000
@@ -18,7 +18,7 @@
 
 import dimod
 
-from dwave.cloud.exceptions import ConfigFileError, SolverNotFoundError
+from dwave.cloud.exceptions import ConfigFileError
 
 from dwave.system import DWaveSampler, EmbeddingComposite
 
@@ -31,7 +31,7 @@
         try:
             cls.qpu = DWaveSampler(
                 solver=dict(initial_state=True, anneal_schedule=True))
-        except (ValueError, ConfigFileError, SolverNotFoundError):
+        except (ValueError, ConfigFileError):
             raise unittest.SkipTest("no qpu available")
 
     @classmethod
