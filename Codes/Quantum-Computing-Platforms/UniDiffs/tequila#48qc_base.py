--- tequila/tequila#48/after/qc_base.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#48/before/qc_base.py	2022-01-10 16:02:54.000000000 +0000
@@ -580,10 +580,6 @@
         else:
             self.reference = reference
 
-        self.transformation = self._initialize_transformation(transformation=transformation, *args, **kwargs)
-        self._rdm1 = None
-        self._rdm2 = None
-    def _initialize_transformation(self, transformation, *args, **kwargs):
         # filter out arguments to the transformation
         trafo_args = {k.split("__")[1]: v for k, v in kwargs.items() if
                       (hasattr(k, "lower") and "transformation__" in k.lower())}
@@ -605,7 +601,6 @@
                 trafo_args["active_orbitals"] = self.n_orbitals * 2
             if "active_fermions" not in trafo_args:
                 trafo_args["active_fermions"] = self.n_electrons
-            print("trafo_args = ", trafo_args)
             trafo = openfermion.symmetry_conserving_bravyi_kitaev
 
         elif hasattr(transformation, "lower"):
@@ -614,7 +609,9 @@
             assert (callable(transformation))
             trafo = transformation
 
-        return self._QubitEncoding(transformation=trafo, **trafo_args)
+        self.transformation = self._QubitEncoding(transformation=trafo, **trafo_args)
+        self._rdm1 = None
+        self._rdm2 = None
 
     def _make_active_space_data(self, active_orbitals, reference=None):
         """
