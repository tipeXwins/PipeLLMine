--- amazon-braket-sdk-python/amazon-braket-sdk-python#250/after/quantum_operator.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#250/before/quantum_operator.py	2022-01-10 16:02:54.000000000 +0000
@@ -12,7 +12,7 @@
 # language governing permissions and limitations under the License.
 from __future__ import annotations
 
-from typing import Any, List, Optional, Sequence
+from typing import Any, List, Sequence
 
 import numpy as np
 
@@ -22,7 +22,7 @@
 class QuantumOperator(Operator):
     """A quantum operator is the definition of a quantum operation for a quantum device."""
 
-    def __init__(self, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
+    def __init__(self, qubit_count: int, ascii_symbols: Sequence[str]):
         """
         Args:
             qubit_count (int): Number of qubits this quantum operator interacts with.
@@ -39,36 +39,18 @@
                 `ascii_symbols` length != `qubit_count`
         """
 
-        fixed_qubit_count = self.fixed_qubit_count()
-        if fixed_qubit_count is NotImplemented:
-            self._qubit_count = qubit_count
-        else:
-            if qubit_count and qubit_count != fixed_qubit_count:
-                raise ValueError(
-                    f"Provided qubit count {qubit_count}"
-                    "does not equal fixed qubit count {fixed_qubit_count}"
-                )
-            self._qubit_count = fixed_qubit_count
-        if not isinstance(self._qubit_count, int):
-            raise TypeError(f"qubit_count, {self._qubit_count}, must be an integer")
-        if self._qubit_count < 1:
-            raise ValueError(f"qubit_count, {self._qubit_count}, must be greater than zero")
+        if qubit_count < 1:
+            raise ValueError(f"qubit_count, {qubit_count}, must be greater than zero")
+        self._qubit_count = qubit_count
 
         if ascii_symbols is None:
             raise ValueError("ascii_symbols must not be None")
 
-        if len(ascii_symbols) != self._qubit_count:
-            msg = (
-                f"ascii_symbols, {ascii_symbols},"
-                f" length must equal qubit_count, {self._qubit_count}"
-            )
+        if len(ascii_symbols) != qubit_count:
+            msg = f"ascii_symbols, {ascii_symbols}, length must equal qubit_count, {qubit_count}"
             raise ValueError(msg)
         self._ascii_symbols = tuple(ascii_symbols)
 
-    @staticmethod
-    def fixed_qubit_count() -> int:
-        return NotImplemented
-
     @property
     def qubit_count(self) -> int:
         """int: Returns number of qubits this quantum operator interacts with."""
