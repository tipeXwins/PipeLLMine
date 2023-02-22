--- qiskit-terra/qiskit-terra#6554/after/probability.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#6554/before/probability.py	2022-01-10 16:02:54.000000000 +0000
@@ -22,7 +22,7 @@
 class ProbDistribution(dict):
     """A generic dict-like class for probability distributions."""
 
-    _bitstring_regex = re.compile(r"^[01]+$")
+    bitstring_regex = re.compile(r"^[01]+$")
 
     def __init__(self, data, shots=None):
         """Builds a probability distribution object.
@@ -54,7 +54,7 @@
                 elif first_key.startswith("0b"):
                     bin_raw = data
                     data = {int(key, 0): value for key, value in bin_raw.items()}
-                elif self._bitstring_regex.search(first_key):
+                elif self.bitstring_regex.search(first_key):
                     bin_raw = data
                     data = {int("0b" + key, 0): value for key, value in bin_raw.items()}
                 else:
@@ -67,15 +67,14 @@
                 raise TypeError("Input data's keys are of invalid type, must be str or int")
         super().__init__(data)
 
-    def binary_probabilities(self, num_bits=None):
+    def binary_probabilities(self):
         """Build a probabilities dictionary with binary string keys
 
         Returns:
             dict: A dictionary where the keys are binary strings in the format
                 ``"0110"``
         """
-        n = len(bin(max(self.keys(), default=0))) - 2 if num_bits is None else num_bits
-        return {format(key, "b").zfill(n): value for key, value in self.items()}
+        return {bin(key)[2:]: value for key, value in self.items()}
 
     def hex_probabilities(self):
         """Build a probabilities dictionary with hexadecimal string keys
