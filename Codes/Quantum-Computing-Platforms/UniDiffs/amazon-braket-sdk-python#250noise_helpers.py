--- amazon-braket-sdk-python/amazon-braket-sdk-python#250/after/noise_helpers.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#250/before/noise_helpers.py	2022-01-10 16:02:54.000000000 +0000
@@ -62,16 +62,10 @@
 
     if noise.qubit_count > 1:
         for g in target_gates:
-            fixed_qubit_count = g.fixed_qubit_count()
-            if fixed_qubit_count is NotImplemented:
+            if g != Gate.Unitary and g().qubit_count != noise.qubit_count:
                 raise ValueError(
-                    f"Target gate {g} can be instantiated on a variable number of qubits,"
-                    " but noise can only target gates with fixed qubit counts."
-                )
-            if fixed_qubit_count != noise.qubit_count:
-                raise ValueError(
-                    f"Target gate {g} acts on {fixed_qubit_count} qubits,"
-                    f" but {noise} acts on {noise.qubit_count} qubits."
+                    "The target_targets must be gates that have the same number of \
+qubits as defined by the multi-qubit noise channel."
                 )
 
 
