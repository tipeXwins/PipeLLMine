58c58
<             len(old_op.qubits) == 2 and not self._may_keep_old_op(old_op)
---
>             len(old_op.qubits) == 2 and not isinstance(old_op.gate, ops.CZPowGate)
60a61,67
>         if not self.allow_partial_czs:
>             switch_to_new |= any(
>                 isinstance(old_op, ops.GateOperation)
>                 and isinstance(old_op.gate, ops.CZPowGate)
>                 and old_op.gate.exponent != 1
>                 for old_op in old_operations
>             )
84,87d90
<     def _may_keep_old_op(self, old_op: 'cirq.Operation') -> bool:
<         if self.allow_partial_czs:
<             return isinstance(old_op.gate, ops.CZPowGate)
<         return isinstance(old_op.gate, ops.CZPowGate) and old_op.gate.exponent == 1
