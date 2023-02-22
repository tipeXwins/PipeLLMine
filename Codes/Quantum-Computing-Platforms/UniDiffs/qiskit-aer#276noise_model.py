--- qiskit-aer/qiskit-aer#276/after/noise_model.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#276/before/noise_model.py	2022-01-10 16:02:54.000000000 +0000
@@ -424,7 +424,7 @@
             qs_str = self._qubits2str(qubits)
             nqs_str = self._qubits2str(noise_qubits)
             if qs_str in gate_qubit_dict:
-                noise_qubit_dict = gate_qubit_dict[qs_str]
+                noise_qubit_dict = gate_qubit_dict[nqs_str]
                 if nqs_str in noise_qubit_dict:
                     new_error = noise_qubit_dict[nqs_str].compose(error)
                     noise_qubit_dict[nqs_str] = new_error
