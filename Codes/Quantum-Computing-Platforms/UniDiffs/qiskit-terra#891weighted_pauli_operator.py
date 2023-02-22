--- qiskit-terra/qiskit-terra#891/after/weighted_pauli_operator.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#891/before/weighted_pauli_operator.py	2022-01-10 16:02:54.000000000 +0000
@@ -365,8 +365,9 @@
                         break
             for idx in indices:
                 new_idx = old_to_new_indices[idx]
-                if new_idx is not None and new_idx not in new_indices:
+                if new_idx is not None:
                     new_indices.append(new_idx)
+            new_indices = list(set(new_indices))
             if new_indices and not found:
                 new_basis.append((basis, new_indices))
         op._basis = new_basis
