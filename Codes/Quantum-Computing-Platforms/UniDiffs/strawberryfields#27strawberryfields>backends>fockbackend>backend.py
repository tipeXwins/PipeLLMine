--- strawberryfields/strawberryfields#27/after/strawberryfields>backends>fockbackend>backend.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#27/before/strawberryfields>backends>fockbackend>backend.py	2022-01-10 16:02:54.000000000 +0000
@@ -214,8 +214,6 @@
         self.circuit.squeeze(abs(z), phase(z), self._remap_modes(mode))
 
     def beamsplitter(self, t, r, mode1, mode2):
-        if isinstance(t, complex):
-            raise ValueError("Beamsplitter transmittivity t must be a float.")
         self.circuit.beamsplitter(t, abs(r), phase(r), self._remap_modes(mode1), self._remap_modes(mode2))
 
     def kerr_interaction(self, kappa, mode):
