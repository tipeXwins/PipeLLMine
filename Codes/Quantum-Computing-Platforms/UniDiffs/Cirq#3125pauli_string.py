--- Cirq/Cirq#3125/after/pauli_string.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#3125/before/pauli_string.py	2022-01-10 16:02:54.000000000 +0000
@@ -679,8 +679,8 @@
             from cirq.ops import pauli_string_phasor
             return pauli_string_phasor.PauliStringPhasor(
                 PauliString(qubit_pauli_map=self._qubit_pauli_map),
-                exponent_neg=+half_turns / 2,
-                exponent_pos=-half_turns / 2)
+                exponent_neg=+half_turns / 4,
+                exponent_pos=-half_turns / 4)
         return NotImplemented
 
     def map_qubits(self, qubit_map: Dict[raw_types.Qid, raw_types.Qid]
