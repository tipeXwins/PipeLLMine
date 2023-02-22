--- ProjectQ/ProjectQ#101/after/_time_evolution.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#101/before/_time_evolution.py	2022-01-10 16:02:54.000000000 +0000
@@ -74,7 +74,7 @@
         for term in hamiltonian.terms:
             if self.hamiltonian.terms[term].imag == 0:
                 self.hamiltonian.terms[term] = float(
-                    self.hamiltonian.terms[term].real)
+                    self.hamiltonian.terms[term])
             else:
                 raise NotHermitianOperatorError("hamiltonian must be "
                                                 "hermitian and hence only "
