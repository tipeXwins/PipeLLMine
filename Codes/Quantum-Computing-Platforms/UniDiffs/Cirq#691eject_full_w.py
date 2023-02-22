--- Cirq/Cirq#691/after/eject_full_w.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#691/before/eject_full_w.py	2022-01-10 16:02:54.000000000 +0000
@@ -17,9 +17,10 @@
 
 from typing import Optional, cast, TYPE_CHECKING, Iterable
 
-from cirq import circuits, ops, extension, value
+from cirq import circuits, ops, extension
 from cirq.google import decompositions
 from cirq.google.xmon_gates import ExpZGate, ExpWGate, Exp11Gate
+from cirq.value import Symbol
 
 if TYPE_CHECKING:
     # pylint: disable=unused-import
@@ -209,7 +210,7 @@
     b = cast(float, w.axis_half_turns)
     t = cast(float, w.half_turns)
     new_op = ExpWGate(half_turns=t,
-                      axis_half_turns=2*a-b).on(op.qubits[0])
+                      axis_half_turns=b-2*a).on(op.qubits[0])
     state.deletions.append((moment_index, op))
     state.inline_intos.append((moment_index, new_op))
 
@@ -301,7 +302,7 @@
             not isinstance(op.gate, (Exp11Gate, ops.Rot11Gate))):
         return None
     h = op.gate.half_turns
-    if isinstance(h, value.Symbol):
+    if isinstance(h, Symbol):
         return None
     return h
 
@@ -309,8 +310,8 @@
 def _try_get_known_w(op: ops.Operation) -> Optional[ExpWGate]:
     if (not isinstance(op, ops.GateOperation) or
             not isinstance(op.gate, ExpWGate) or
-            isinstance(op.gate.half_turns, value.Symbol) or
-            isinstance(op.gate.axis_half_turns, value.Symbol)):
+            isinstance(op.gate.half_turns, Symbol) or
+            isinstance(op.gate.axis_half_turns, Symbol)):
         return None
     return op.gate
 
@@ -320,6 +321,6 @@
             not isinstance(op.gate, (ExpZGate, ops.RotZGate))):
         return None
     h = op.gate.half_turns
-    if isinstance(h, value.Symbol):
+    if isinstance(h, Symbol):
         return None
     return h
