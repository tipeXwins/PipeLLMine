--- qiskit-terra/qiskit-terra#5910/after/quantumcircuit.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#5910/before/quantumcircuit.py	2022-01-10 16:02:54.000000000 +0000
@@ -566,9 +566,6 @@
         for instruction_context in itertools.chain(self.data, rhs.data):
             circuit._append(*instruction_context)
         circuit.global_phase = self.global_phase + rhs.global_phase
-        for gate, cals in rhs.calibrations.items():
-            for key, sched in cals.items():
-                circuit.add_calibration(gate, qubits=key[0], schedule=sched, params=key[1])
         return circuit
 
     def extend(self, rhs):
@@ -613,9 +610,6 @@
         for instruction_context in data:
             self._append(*instruction_context)
         self.global_phase += rhs.global_phase
-        for gate, cals in rhs.calibrations.items():
-            for key, sched in cals.items():
-                self.add_calibration(gate, qubits=key[0], schedule=sched, params=key[1])
         return self
 
     def compose(self, other, qubits=None, clbits=None, front=False, inplace=False):
