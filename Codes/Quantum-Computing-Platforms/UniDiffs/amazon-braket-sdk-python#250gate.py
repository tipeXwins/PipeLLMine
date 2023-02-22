--- amazon-braket-sdk-python/amazon-braket-sdk-python#250/after/gate.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#250/before/gate.py	2022-01-10 16:02:54.000000000 +0000
@@ -11,7 +11,7 @@
 # ANY KIND, either express or implied. See the License for the specific
 # language governing permissions and limitations under the License.
 
-from typing import Any, Optional, Sequence
+from typing import Any, Sequence
 
 from braket.circuits.quantum_operator import QuantumOperator
 from braket.circuits.qubit_set import QubitSet
@@ -24,7 +24,7 @@
     the metadata that defines what a gate is and what it does.
     """
 
-    def __init__(self, qubit_count: Optional[int], ascii_symbols: Sequence[str]):
+    def __init__(self, qubit_count: int, ascii_symbols: Sequence[str]):
         """
         Args:
             qubit_count (int): Number of qubits this gate interacts with.
