30,31d29
< from qiskit.pulse.channels import MemorySlot
< from qiskit.pulse.commands import AcquireInstruction
145c143
<     qubit_mem_slots = {}  # Map measured qubit index to classical bit index
---
>     measured_qubits = set()  # Collect qubits that would like to be measured
152,153c150,151
<         for qubit in qubit_mem_slots:
<             measures.add(tuple(schedule_config.meas_map[qubit]))
---
>         for q in measured_qubits:
>             measures.add(tuple(schedule_config.meas_map[q]))
156,172c154,155
<             unused_mem_slots = set(qubits) - set(qubit_mem_slots.values())
<             default_sched = cmd_def.get('measure', qubits)
<             for time, inst in default_sched.instructions:
<                 if isinstance(inst, AcquireInstruction):
<                     mem_slots = []
<                     for channel in inst.acquires:
<                         if channel.index in qubit_mem_slots.keys():
<                             mem_slots.append(MemorySlot(qubit_mem_slots[channel.index]))
<                         else:
<                             mem_slots.append(MemorySlot(unused_mem_slots.pop()))
<                     new_acquire = AcquireInstruction(command=inst.command,
<                                                      acquires=inst.acquires,
<                                                      mem_slots=mem_slots)
<                     sched._union((time, new_acquire))
<                 elif inst.channels[0].index in qubit_mem_slots.keys():
<                     sched._union((time, inst))
<         qubit_mem_slots.clear()
---
>             sched |= cmd_def.get('measure', qubits)
>         measured_qubits.clear()
175c158
<     for inst, qubits, clbits in circuit.data:
---
>     for inst, qubits, _ in circuit.data:
177c160
<         if any(q in qubit_mem_slots for q in inst_qubits):
---
>         if any(q in measured_qubits for q in inst_qubits):
183,187c166
<             if (len(inst_qubits) != 1 and len(clbits) != 1):
<                 raise QiskitError("Qubit '{0}' or classical bit '{1}' errored because the "
<                                   "circuit Measure instruction only takes one of "
<                                   "each.".format(inst_qubits, clbits))
<             qubit_mem_slots[inst_qubits[0]] = clbits[0].index
---
>             measured_qubits.update(inst_qubits)
197c176
<     if qubit_mem_slots:
---
>     if measured_qubits:
