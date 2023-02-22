--- dwave-system/dwave-system#6/after/response.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#6/before/response.py	2022-01-10 16:02:54.000000000 +0000
@@ -67,7 +67,7 @@
         energies = future.energies
         num_occurrences = future.occurrences
 
-        nodes = future.solver.nodes
+        nodelist = future.solver._encoding_qubits
 
         sample_values = self.vartype.value
 
@@ -75,7 +75,7 @@
             for sample, energy, n_o in zip(samples, energies, num_occurrences):
                 datum = {}
 
-                sample = {v: sample[v] for v in nodes}
+                sample = dict(zip(nodelist, sample))
 
                 if sample_values is not None and not all(v in sample_values for v in sample.values()):
                     raise ValueError("expected the biases of 'sample' to be in {}".format(sample_values))
