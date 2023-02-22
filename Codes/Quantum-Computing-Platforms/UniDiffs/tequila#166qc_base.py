--- tequila/tequila#166/after/qc_base.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#166/before/qc_base.py	2022-01-10 16:02:54.000000000 +0000
@@ -1418,7 +1418,7 @@
             raise TequilaException("make_uccsd_ansatz currently only for closed shell systems")
 
         nocc = self.n_electrons // 2
-        nvirt = self.n_orbitals - nocc
+        nvirt = self.n_orbitals // 2 - nocc
 
         Uref = QCircuit()
         if include_reference_ansatz:
