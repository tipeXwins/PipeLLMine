--- pyquil/pyquil#758/after/operator_estimation.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#758/before/operator_estimation.py	2022-01-10 16:02:54.000000000 +0000
@@ -448,20 +448,20 @@
         # measure (n_shots, n_qubits=2) obs_strings then the full operator value involves selecting
         # either the first column, second column, or both and multiplying along the row.
         for setting in settings:
-            assert setting.in_operator.coefficient == 1, 'in_operator should specify a state and ' \
-                                                         'therefore cannot have a coefficient'
-            coeff = complex(setting.out_operator.coefficient)
-            if not np.isclose(coeff.imag, 0):
-                raise ValueError(f"{setting}'s out_operator has a complex coefficient.")
-            coeff = coeff.real
             #     sense but should happen perfectly.
             if is_identity(setting.out_operator):
                 yield ExperimentResult(
                     setting=setting,
-                    expectation=coeff,
+                    expectation=1.0,
                     stddev=0.0,
                 )
                 continue
+            assert setting.in_operator.coefficient == 1, 'in_operator should specify a state and ' \
+                                                         'therefore cannot have a coefficient'
+            coeff = complex(setting.out_operator.coefficient)
+            if not np.isclose(coeff.imag, 0):
+                raise ValueError(f"{setting}'s out_operator has a complex coefficient.")
+            coeff = coeff.real
 
             # 3.4 Pick columns corresponding to qubits with a non-identity out_operation and stack
             #     into an array of shape (n_shots, n_measure_qubits)
