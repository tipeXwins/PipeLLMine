--- tequila/tequila#48/after/psi4_interface.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#48/before/psi4_interface.py	2022-01-10 16:02:54.000000000 +0000
@@ -224,7 +224,12 @@
             self.compute_energy(method="hf", recompute=True)
             self.ref_wfn = self.logs["hf"].wfn
 
-        self.transformation = self._initialize_transformation(transformation=transformation, *args, **kwargs)
+    @property
+    def n_orbitals(self) -> int:
+        if self.active_space is not None:
+            return len(self.active_space.active_orbitals)
+        else:
+            return super().n_orbitals
 
     @property
     def point_group(self):
@@ -610,4 +615,4 @@
                 rdm2 = NBodyTensor(elems=rdm2, scheme='chem')
                 rdm2.reorder(to='phys')  # RDMs in physics ordering (cp. to NBodyTensor in qc_base.py)
                 rdm2 = 2*rdm2.elems  # Factor 2 since psi4 normalizes 2-rdm by 1/2
-                self._rdm2 = rdm2
+                self._rdm2 = rdm2
\ No newline at end of file
