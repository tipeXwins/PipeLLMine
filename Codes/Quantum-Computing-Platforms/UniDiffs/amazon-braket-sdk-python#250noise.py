--- amazon-braket-sdk-python/amazon-braket-sdk-python#250/after/noise.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#250/before/noise.py	2022-01-10 16:02:54.000000000 +0000
@@ -11,7 +11,7 @@
 # ANY KIND, either express or implied. See the License for the specific
 # language governing permissions and limitations under the License.
 
-from typing import Any, Optional, Sequence
+from typing import Any, Sequence
 
 from braket.circuits.quantum_operator import QuantumOperator
 from braket.circuits.qubit_set import QubitSet
@@ -26,10 +26,14 @@
     the metadata that defines what the noise channel is and what it does.
     """
 
-    def __init__(self, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
+    def __init__(
+        self,
+        qubit_count: int,
+        ascii_symbols: Sequence[str],
+    ):
         """
         Args:
-            qubit_count (int, optional): Number of qubits this noise channel interacts with.
+            qubit_count (int): Number of qubits this noise channel interacts with.
             ascii_symbols (Sequence[str]): ASCII string symbols for this noise channel. These
                 are used when printing a diagram of circuits. Length must be the same as
                 `qubit_count`, and index ordering is expected to correlate with target ordering
@@ -39,7 +43,15 @@
             ValueError: `qubit_count` is less than 1, `ascii_symbols` are None, or
                 length of `ascii_symbols` is not equal to `qubit_count`
         """
-        super().__init__(qubit_count=qubit_count, ascii_symbols=ascii_symbols)
+        if qubit_count < 1:
+            raise ValueError(f"qubit_count, {qubit_count}, must be greater than zero")
+        self._qubit_count = qubit_count
+        if ascii_symbols is None:
+            raise ValueError("ascii_symbols must not be None")
+        if len(ascii_symbols) != qubit_count:
+            msg = f"ascii_symbols, {ascii_symbols}, length must equal qubit_count, {qubit_count}"
+            raise ValueError(msg)
+        self._ascii_symbols = tuple(ascii_symbols)
 
     @property
     def name(self) -> str:
@@ -93,9 +105,7 @@
     parameterized by a single probability.
     """
 
-    def __init__(
-        self, probability: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]
-    ):
+    def __init__(self, probability: float, qubit_count: int, ascii_symbols: Sequence[str]):
         """
         Args:
             probability (float): The probability that the noise occurs.
@@ -135,9 +145,7 @@
     channels parameterized by a single probability.
     """
 
-    def __init__(
-        self, probability: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]
-    ):
+    def __init__(self, probability: float, qubit_count: int, ascii_symbols: Sequence[str]):
         """
         Args:
             probability (float): The probability that the noise occurs.
@@ -177,9 +185,7 @@
     parameterized by a single probability.
     """
 
-    def __init__(
-        self, probability: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]
-    ):
+    def __init__(self, probability: float, qubit_count: int, ascii_symbols: Sequence[str]):
         """
         Args:
             probability (float): The probability that the noise occurs.
@@ -224,7 +230,7 @@
         probX: float,
         probY: float,
         probZ: float,
-        qubit_count: Optional[int],
+        qubit_count: int,
         ascii_symbols: Sequence[str],
     ):
         """
@@ -298,7 +304,7 @@
     on N qubits parameterized by gamma.
     """
 
-    def __init__(self, gamma: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
+    def __init__(self, gamma: float, qubit_count: int, ascii_symbols: Sequence[str]):
         """
         Args:
             gamma (float): Probability of damping.
@@ -339,11 +345,7 @@
     """
 
     def __init__(
-        self,
-        gamma: float,
-        probability: float,
-        qubit_count: Optional[int],
-        ascii_symbols: Sequence[str],
+        self, gamma: float, probability: float, qubit_count: int, ascii_symbols: Sequence[str]
     ):
         """
         Args:
