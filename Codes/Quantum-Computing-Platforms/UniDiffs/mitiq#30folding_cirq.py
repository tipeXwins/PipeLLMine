--- mitiq/mitiq#30/after/folding_cirq.py	2022-01-10 16:02:54.000000000 +0000
+++ mitiq/mitiq#30/before/folding_cirq.py	2022-01-10 16:02:54.000000000 +0000
@@ -100,8 +100,6 @@
     _fold_moments(circuit, list(range(len(circuit))))
 
 
-def _get_num_to_fold(stretch: float, ngates: int) -> int:
-    return round(ngates * (stretch - 1.0) / 2.0)
 def fold_gates_from_left(circuit: Circuit, stretch: float) -> Circuit:
     """Returns a new folded circuit by applying the map G -> G G^dag G to a subset of gates of the input circuit,
     starting with gates at the left (beginning) of the circuit.
@@ -125,9 +123,7 @@
         raise ValueError("The stretch factor must be a real number between 1 and 3.")
 
     ngates = len(list(folded.all_operations()))
-    num_to_fold = _get_num_to_fold(stretch, ngates)
-    if num_to_fold == 0:
-        return folded
+    num_to_fold = int(ngates * (stretch - 1.0) / 2.0)
     num_folded = 0
     moment_shift = 0
 
@@ -217,7 +213,7 @@
         np.random.seed(seed)
 
     ngates = len(list(folded.all_operations()))
-    num_to_fold = _get_num_to_fold(stretch, ngates)
+    num_to_fold = int(ngates * (stretch - 1.0) / 2.0)
 
     # Keep track of where moments are in the folded circuit
     moment_indices = {i: i for i in range(len(circuit))}
@@ -314,4 +310,4 @@
     if fractional_depth != 0:
         eye += inverse(circuit[-fractional_depth:]) + circuit[-fractional_depth:]
 
-    return circuit + eye
+    return circuit + eye
\ No newline at end of file
