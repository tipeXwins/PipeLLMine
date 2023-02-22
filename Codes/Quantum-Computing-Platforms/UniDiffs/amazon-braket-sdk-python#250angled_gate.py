--- amazon-braket-sdk-python/amazon-braket-sdk-python#250/after/angled_gate.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#250/before/angled_gate.py	2022-01-10 16:02:54.000000000 +0000
@@ -12,7 +12,7 @@
 # language governing permissions and limitations under the License.
 
 import math
-from typing import Optional, Sequence
+from typing import Sequence
 
 from braket.circuits.gate import Gate
 
@@ -22,7 +22,7 @@
     Class `AngledGate` represents a quantum gate that operates on N qubits and an angle.
     """
 
-    def __init__(self, angle: float, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
+    def __init__(self, angle: float, qubit_count: int, ascii_symbols: Sequence[str]):
         """
         Args:
             angle (float): The angle of the gate in radians.
