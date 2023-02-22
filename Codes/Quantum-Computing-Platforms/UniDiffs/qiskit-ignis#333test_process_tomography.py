--- qiskit-ignis/qiskit-ignis#333/after/test_process_tomography.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#333/before/test_process_tomography.py	2022-01-10 16:02:54.000000000 +0000
@@ -46,9 +46,9 @@
         bell.cx(q2[0], q2[1])
 
         choi_cvx, choi_mle, choi_ideal = run_circuit_and_tomography(bell, q2)
-        F_bell_cvx = state_fidelity(choi_ideal/4, choi_cvx/4, validate=False)
+        F_bell_cvx = state_fidelity(choi_ideal/4, choi_cvx/4)
         self.assertAlmostEqual(F_bell_cvx, 1, places=1)
-        F_bell_mle = state_fidelity(choi_ideal/4, choi_mle/4, validate=False)
+        F_bell_mle = state_fidelity(choi_ideal/4, choi_mle/4)
         self.assertAlmostEqual(F_bell_mle, 1, places=1)
 
 
