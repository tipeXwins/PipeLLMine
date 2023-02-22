--- Cirq/Cirq#4288/after/merge_interactions.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#4288/before/merge_interactions.py	2022-01-10 16:02:54.000000000 +0000
@@ -55,9 +55,16 @@
 
         switch_to_new = False
         switch_to_new |= any(
-            len(old_op.qubits) == 2 and not self._may_keep_old_op(old_op)
+            len(old_op.qubits) == 2 and not isinstance(old_op.gate, ops.CZPowGate)
             for old_op in old_operations
         )
+        if not self.allow_partial_czs:
+            switch_to_new |= any(
+                isinstance(old_op, ops.GateOperation)
+                and isinstance(old_op.gate, ops.CZPowGate)
+                and old_op.gate.exponent != 1
+                for old_op in old_operations
+            )
 
         # This point cannot be optimized using this method
         if not switch_to_new and old_interaction_count <= 1:
@@ -81,10 +88,6 @@
             clear_qubits=op.qubits,
             new_operations=new_operations,
         )
-    def _may_keep_old_op(self, old_op: 'cirq.Operation') -> bool:
-        if self.allow_partial_czs:
-            return isinstance(old_op.gate, ops.CZPowGate)
-        return isinstance(old_op.gate, ops.CZPowGate) and old_op.gate.exponent == 1
 
     def _op_to_matrix(
         self, op: ops.Operation, qubits: Tuple['cirq.Qid', ...]
