--- qiskit-ignis/qiskit-ignis#563/after/complete_mitigator.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#563/before/complete_mitigator.py	2022-01-10 16:02:54.000000000 +0000
@@ -17,6 +17,7 @@
 from typing import Optional, List, Dict, Tuple
 import numpy as np
 
+from qiskit.exceptions import QiskitError
 from .utils import (counts_probability_vector, _expval_with_stddev)
 from .base_meas_mitigator import BaseExpvalMeasMitigator
 
@@ -94,6 +95,8 @@
         # Get qubit mitigation matrix and mitigate probs
         if qubits is None:
             qubits = tuple(range(num_qubits))
+        if len(qubits) != num_qubits:
+            raise QiskitError("Num qubits does not match number of clbits.")
         mit_mat = self.mitigation_matrix(qubits)
 
         # Get operator coeffs
