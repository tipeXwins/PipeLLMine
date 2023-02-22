--- tequila/tequila#8/after/qubit_hamiltonian.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#8/before/qubit_hamiltonian.py	2022-01-10 16:02:54.000000000 +0000
@@ -539,7 +539,7 @@
 
         for k, v in self.qubit_operator.terms.items():
             mk = tuple([(qubit_map[x[0]], x[1]) for x in k])
-            mapped_terms[mk] = v
+            mapped_terms[k] = v
 
         mapped = QubitOperator.zero()
         mapped.terms = mapped_terms
