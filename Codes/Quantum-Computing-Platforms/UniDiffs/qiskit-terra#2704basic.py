--- qiskit-terra/qiskit-terra#2704/after/basic.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#2704/before/basic.py	2022-01-10 16:02:54.000000000 +0000
@@ -27,8 +27,6 @@
 from qiskit.extensions.standard.barrier import Barrier
 from qiskit.pulse.exceptions import PulseError
 from qiskit.pulse.schedule import Schedule
-from qiskit.pulse.channels import MemorySlot
-from qiskit.pulse.commands import AcquireInstruction
 
 from qiskit.scheduler.config import ScheduleConfig
 
@@ -142,49 +140,30 @@
     circ_pulse_defs = []
 
     cmd_def = schedule_config.cmd_def
-    qubit_mem_slots = {}  # Map measured qubit index to classical bit index
+    measured_qubits = set()  # Collect qubits that would like to be measured
 
     def get_measure_schedule() -> CircuitPulseDef:
         """Create a schedule to measure the qubits queued for measuring."""
         measures = set()
         all_qubits = set()
         sched = Schedule()
-        for qubit in qubit_mem_slots:
-            measures.add(tuple(schedule_config.meas_map[qubit]))
+        for q in measured_qubits:
+            measures.add(tuple(schedule_config.meas_map[q]))
         for qubits in measures:
             all_qubits.update(qubits)
-            unused_mem_slots = set(qubits) - set(qubit_mem_slots.values())
-            default_sched = cmd_def.get('measure', qubits)
-            for time, inst in default_sched.instructions:
-                if isinstance(inst, AcquireInstruction):
-                    mem_slots = []
-                    for channel in inst.acquires:
-                        if channel.index in qubit_mem_slots.keys():
-                            mem_slots.append(MemorySlot(qubit_mem_slots[channel.index]))
-                        else:
-                            mem_slots.append(MemorySlot(unused_mem_slots.pop()))
-                    new_acquire = AcquireInstruction(command=inst.command,
-                                                     acquires=inst.acquires,
-                                                     mem_slots=mem_slots)
-                    sched._union((time, new_acquire))
-                elif inst.channels[0].index in qubit_mem_slots.keys():
-                    sched._union((time, inst))
-        qubit_mem_slots.clear()
+            sched |= cmd_def.get('measure', qubits)
+        measured_qubits.clear()
         return CircuitPulseDef(schedule=sched, qubits=list(all_qubits))
 
-    for inst, qubits, clbits in circuit.data:
+    for inst, qubits, _ in circuit.data:
         inst_qubits = [qubit.index for qubit in qubits]  # We want only the indices of the qubits
-        if any(q in qubit_mem_slots for q in inst_qubits):
+        if any(q in measured_qubits for q in inst_qubits):
             # If we are operating on a qubit that was scheduled to be measured, process that first
             circ_pulse_defs.append(get_measure_schedule())
         if isinstance(inst, Barrier):
             circ_pulse_defs.append(CircuitPulseDef(schedule=inst, qubits=inst_qubits))
         elif isinstance(inst, Measure):
-            if (len(inst_qubits) != 1 and len(clbits) != 1):
-                raise QiskitError("Qubit '{0}' or classical bit '{1}' errored because the "
-                                  "circuit Measure instruction only takes one of "
-                                  "each.".format(inst_qubits, clbits))
-            qubit_mem_slots[inst_qubits[0]] = clbits[0].index
+            measured_qubits.update(inst_qubits)
         else:
             try:
                 circ_pulse_defs.append(
@@ -194,7 +173,7 @@
                 raise QiskitError("Operation '{0}' on qubit(s) {1} not supported by the backend "
                                   "command definition. Did you remember to transpile your input "
                                   "circuit for the same backend?".format(inst.name, inst_qubits))
-    if qubit_mem_slots:
+    if measured_qubits:
         circ_pulse_defs.append(get_measure_schedule())
 
     return circ_pulse_defs
