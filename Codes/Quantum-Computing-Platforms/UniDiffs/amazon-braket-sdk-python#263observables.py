--- amazon-braket-sdk-python/amazon-braket-sdk-python#263/after/observables.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#263/before/observables.py	2022-01-10 16:02:54.000000000 +0000
@@ -181,16 +181,9 @@
         result of the tensor product of `ob1`, `ob2`, `ob3`, or `np.kron(np.kron(ob1.to_matrix(),
         ob2.to_matrix()), ob3.to_matrix())`.
         """
-        flattened_observables = []
-        for obs in observables:
-            if isinstance(obs, TensorProduct):
-                for nested_obs in obs.factors:
-                    flattened_observables.append(nested_obs)
-            else:
-                flattened_observables.append(obs)
-        self._factors = tuple(flattened_observables)
-        qubit_count = sum([obs.qubit_count for obs in flattened_observables])
-        display_name = "@".join([obs.ascii_symbols[0] for obs in flattened_observables])
+        self._factors = tuple(observables)
+        qubit_count = sum([obs.qubit_count for obs in observables])
+        display_name = "@".join([obs.ascii_symbols[0] for obs in observables])
         super().__init__(qubit_count=qubit_count, ascii_symbols=[display_name] * qubit_count)
         self._factor_dimensions = tuple(
             len(factor.to_matrix()) for factor in reversed(self._factors)
@@ -244,6 +237,16 @@
             product *= self._factors[-i - 1].eigenvalue(remainder)
         self._eigenvalue_indices[index] = product
         return self._eigenvalue_indices[index]
+    def __matmul__(self, other):
+        if isinstance(other, TensorProduct):
+            return TensorProduct(list(self.factors) + list(other.factors))
+        if isinstance(other, Observable):
+            return TensorProduct(list(self.factors) + [other])
+        raise ValueError("Can only perform tensor products between observables.")
+    def __rmatmul__(self, other):
+        if isinstance(other, Observable):
+            return TensorProduct([other] + list(self.factors))
+        raise ValueError("Can only perform tensor products between observables.")
 
     def __repr__(self):
         return "TensorProduct(" + ", ".join([repr(o) for o in self.factors]) + ")"
