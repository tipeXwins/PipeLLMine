--- pennylane/pennylane#1451/after/qubit.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1451/before/qubit.py	2022-01-10 16:02:54.000000000 +0000
@@ -2646,8 +2646,6 @@
 
         return decomp_ops
 
-    def adjoint(self):
-        return QFT(wires=self.wires).inv()
 
 # =============================================================================
 # Quantum chemistry
