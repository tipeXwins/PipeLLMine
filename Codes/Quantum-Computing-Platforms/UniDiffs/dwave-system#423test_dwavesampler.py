--- dwave-system/dwave-system#423/after/test_dwavesampler.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#423/before/test_dwavesampler.py	2022-01-10 16:02:54.000000000 +0000
@@ -19,9 +19,8 @@
 import numpy
 
 import dimod
-from dwave.cloud.exceptions import ConfigFileError, SolverNotFoundError
+from dwave.cloud.exceptions import ConfigFileError
 from dwave.cloud.client import Client
-from dwave_networkx.generators.pegasus import pegasus_graph
 
 from dwave.system.samplers import DWaveSampler
 
@@ -33,7 +32,7 @@
     def setUpClass(cls):
         try:
             cls.qpu = DWaveSampler()
-        except (ValueError, ConfigFileError, SolverNotFoundError):
+        except (ValueError, ConfigFileError):
             raise unittest.SkipTest("no qpu available")
 
     @classmethod
@@ -135,16 +134,8 @@
     @classmethod
     def setUpClass(cls):
         try:
-            with Client.from_config() as client:
-                solvers = client.get_solvers(qpu=True)
-            if not solvers:
-                raise unittest.SkipTest("no qpu found")
-            for solver in solvers:
-                if solver.num_active_qubits < solver.num_qubits:
-                    cls.qpu = DWaveSampler(solver=solver.id)
-                    return
-            raise unittest.SkipTest("no qpu with less than 100% yield found")
-        except (ValueError, ConfigFileError, SolverNotFoundError):
+            cls.qpu = DWaveSampler(solver=dict(num_active_qubits__lt=2048))
+        except (ValueError, ConfigFileError):
             raise unittest.SkipTest("no qpu available")
 
     @classmethod
@@ -154,13 +145,13 @@
     def test_sample_ising_h_list(self):
         sampler = self.qpu
 
-        h = [0 for _ in range(self.qpu.solver.num_qubits)]
+        h = [0 for _ in range(2048)]
         J = {edge: 0 for edge in sampler.edgelist}
 
         sampleset = sampler.sample_ising(h, J)
 
         self.assertEqual(set(sampleset.variables), set(sampler.nodelist))
-        self.assertLessEqual(len(sampleset.variables), self.qpu.solver.num_qubits)  # sanity check
+        assert len(sampleset.variables) < 2048  # sanity check
 
 
 @unittest.skipIf(os.getenv('SKIP_INT_TESTS'), "Skipping integration test.")
