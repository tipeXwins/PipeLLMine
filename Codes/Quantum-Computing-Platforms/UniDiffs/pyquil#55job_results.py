--- pyquil/pyquil#55/after/job_results.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#55/before/job_results.py	2022-01-10 16:02:54.000000000 +0000
@@ -100,7 +100,7 @@
     """
     num_octets = len(coef_string)
     num_addresses = len(classical_addresses)
-    num_memory_octets = _round_to_next_multiple(num_addresses, 8) // 8
+    num_memory_octets = int(_round_to_next_multiple(num_addresses, 8) / 8)
     num_wavefunction_octets = num_octets - num_memory_octets
 
     # Parse the classical memory
@@ -112,7 +112,7 @@
     mem = mem[0:num_addresses]
 
     # Parse the wavefunction
-    wf = np.zeros(num_wavefunction_octets // OCTETS_PER_COMPLEX_DOUBLE, dtype=np.cfloat)
+    wf = np.zeros(int(num_wavefunction_octets / OCTETS_PER_COMPLEX_DOUBLE), dtype=np.cfloat)
     for i, p in enumerate(range(num_memory_octets, num_octets, OCTETS_PER_COMPLEX_DOUBLE)):
         re_be = coef_string[p: p + OCTETS_PER_DOUBLE_FLOAT]
         im_be = coef_string[p + OCTETS_PER_DOUBLE_FLOAT: p + OCTETS_PER_COMPLEX_DOUBLE]
