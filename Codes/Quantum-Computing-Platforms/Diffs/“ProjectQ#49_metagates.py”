189a190
>         n = self._n
192,196c193,197
<         adding_to_controls = True
<         for reg in qubits:
<             if adding_to_controls:
<                 ctrl += reg
<                 adding_to_controls = len(ctrl) < self._n
---
>         added_ctrl_qubits = 0
>         for qureg in qubits:
>             if added_ctrl_qubits < n:
>                 ctrl = ctrl + qureg
>                 added_ctrl_qubits += len(qureg)
198,199c199,200
<                 gate_quregs.append(reg)
<         # Test that there were enough control quregs and that that
---
>                 gate_quregs.append(qureg)
>         # Test that there were enough control qubits and that that
201c202
<         if len(ctrl) != self._n:
---
>         if added_ctrl_qubits != n:
204c205
<                                     "the required number of control quregs.")
---
>                                     "the required number of control qubits.")
