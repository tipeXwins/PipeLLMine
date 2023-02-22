--- Cirq/Cirq#3125/after/pauli_string_phasor.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#3125/before/pauli_string_phasor.py	2022-01-10 16:02:54.000000000 +0000
@@ -172,7 +172,9 @@
     def __str__(self) -> str:
         if self.exponent_pos == -self.exponent_neg:
             sign = '-' if self.exponent_pos < 0 else ''
-            exponent = str(abs(self.exponent_pos))
+            exponent = str(abs(self.exponent_pos * 2))
+            if abs(self.exponent_relative) == 1:
+                exponent = ''
             return f'exp({sign}iπ{exponent}*{self.pauli_string})'
         return f'({self.pauli_string})**{self.exponent_relative}'
 
