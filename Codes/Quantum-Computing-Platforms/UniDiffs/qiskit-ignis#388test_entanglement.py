--- qiskit-ignis/qiskit-ignis#388/after/test_entanglement.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#388/before/test_entanglement.py	2022-01-10 16:02:54.000000000 +0000
@@ -42,7 +42,7 @@
         self.assertTrue(counts.get('00000', 0) + counts.get('11111', 0) == 1024)
 
         # test MQC
-        circ, delta = get_ghz_mqc_para(qn)
+        circ, delta = get_ghz_mqc_para(qn, measure='full')
         theta_range = np.linspace(0, 2 * np.pi, 16)
         circuits = [circ.bind_parameters({delta: theta_val})
                     for theta_val in theta_range]
@@ -52,18 +52,19 @@
                             (counts.get('00000', 0) + counts.get('00001', 0)) == 1024)
 
         # test parity oscillations
-        circ, params = get_ghz_po_para(qn)
+        circ, params = get_ghz_po_para(qn, measure='full')
         theta_range = np.linspace(0, 2 * np.pi, 16)
         circuits = [circ.bind_parameters({params[0]: theta_val,
                                           params[1]: -theta_val})
                     for theta_val in theta_range]
+        gap_factor = 2.0/3
         for circ in circuits:
             counts = execute(circ, sim, shots=1024).result().get_counts(circ)
             even_counts = sum(key.count('1') % 2 == 0 for key in counts.keys())
             odd_counts = sum(key.count('1') % 2 == 1 for key in counts.keys())
 
-        self.assertTrue(even_counts in (0, 16))
-        self.assertTrue(odd_counts in (0, 16))
+        self.assertTrue((even_counts > gap_factor*1024) or
+                        odd_counts > gap_factor*1024)
 
 
 if __name__ == '__main__':
