24c24
< from qiskit.pulse.macros import measure
---
> from qiskit.scheduler import measure
151c151
<         sched += measure(qubits, inst_map=inst_map, meas_map=meas_map).shift(2*pulse_width)
---
>         sched += measure(qubits, inst_map=inst_map, meas_map=meas_map).shift(pulse_width)
