--- qiskit-terra/qiskit-terra#6554/after/quasi.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#6554/before/quasi.py	2022-01-10 16:02:54.000000000 +0000
@@ -26,7 +26,7 @@
 class QuasiDistribution(dict):
     """A dict-like class for representing qasi-probabilities."""
 
-    _bitstring_regex = re.compile(r"^[01]+$")
+    bitstring_regex = re.compile(r"^[01]+$")
 
     def __init__(self, data, shots=None):
         """Builds a quasiprobability distribution object.
@@ -58,7 +58,7 @@
                 elif first_key.startswith("0b"):
                     bin_raw = data
                     data = {int(key, 0): value for key, value in bin_raw.items()}
-                elif self._bitstring_regex.search(first_key):
+                elif self.bitstring_regex.search(first_key):
                     bin_raw = data
                     data = {int("0b" + key, 0): value for key, value in bin_raw.items()}
                 else:
@@ -104,10 +104,9 @@
             return ProbDistribution(new_probs, self.shots), sqrt(diff)
         return ProbDistribution(new_probs, self.shots)
 
-    def binary_probabilities(self, num_bits=None):
+    def binary_probabilities(self):
 
-        n = len(bin(max(self.keys(), default=0))) - 2 if num_bits is None else num_bits
-        return {format(key, "b").zfill(n): value for key, value in self.items()}
+        return {bin(key)[2:]: value for key, value in self.items()}
 
     def hex_probabilities(self):
         return {hex(key): value for key, value in self.items()}
