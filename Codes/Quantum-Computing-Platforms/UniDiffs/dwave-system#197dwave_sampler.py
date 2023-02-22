--- dwave-system/dwave-system#197/after/dwave_sampler.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#197/before/dwave_sampler.py	2022-01-10 16:02:54.000000000 +0000
@@ -271,10 +271,7 @@
         num_variables = len(active_variables)
 
         # developer note: in the future we should probably catch exceptions
-        nodes = self.solver.nodes
-        edges = self.solver.edges
-        if not (all(v in nodes for v in h) and
-                all((u, v) in edges or (v, u) in edges for u, v in J)):
+        if not self.solver.check_problem(h, J):
             msg = "Problem graph incompatible with solver."
             raise BinaryQuadraticModelStructureError(msg)
 
@@ -322,10 +319,7 @@
         num_variables = len(active_variables)
 
         # developer note: in the future we should probably catch exceptions
-        nodes = self.solver.nodes
-        edges = self.solver.edges
-        if not all(u in nodes if u == v else ((u, v) in edges or (v, u) in edges)
-                   for u, v in Q):
+        if not self.solver.check_problem({}, Q):
             msg = "Problem graph incompatible with solver."
             raise BinaryQuadraticModelStructureError(msg)
 
