--- qiskit-ignis/qiskit-ignis#466/after/pulse_schedules.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#466/before/pulse_schedules.py	2022-01-10 16:02:54.000000000 +0000
@@ -21,7 +21,7 @@
 import qiskit.pulse as pulse
 import qiskit.pulse.library as pulse_lib
 from qiskit.exceptions import QiskitError
-from qiskit.pulse.macros import measure
+from qiskit.scheduler import measure
 
 
 def rabi_schedules(amp_list, qubits, pulse_width, pulse_sigma=None,
@@ -148,7 +148,7 @@
                                           name='drag_pulse_%d_%d' % (index, qubit))
             sched += pulse.Play(drag_pulse_p, drives[qubit])
             sched += pulse.Play(drag_pulse_m, drives[qubit])
-        sched += measure(qubits, inst_map=inst_map, meas_map=meas_map).shift(2*pulse_width)
+        sched += measure(qubits, inst_map=inst_map, meas_map=meas_map).shift(pulse_width)
         drag_scheds.append(sched)
 
     return drag_scheds, xdata
