--- qiskit-ignis/qiskit-ignis#231/after/qiskit>ignis>verification>tomography>basis>circuits.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#231/before/qiskit>ignis>verification>tomography>basis>circuits.py	2022-01-10 16:02:54.000000000 +0000
@@ -263,14 +263,14 @@
         raise QiskitError(
             "prepared_qubits and measured_qubits are different length.")
     num_qubits = len(meas_qubits)
-    meas_qubit_registers = set(q.register for q in meas_qubits)
+    meas_qubit_registers = set(q[0] for q in meas_qubits)
     # Check qubits being measured are defined in circuit
     for reg in meas_qubit_registers:
         if reg not in circuit.qregs:
             logger.warning('WARNING: circuit does not contain '
                            'measured QuantumRegister: %s', reg.name)
 
-    prep_qubit_registers = set(q.register for q in prep_qubits)
+    prep_qubit_registers = set(q[0] for q in prep_qubits)
     # Check qubits being measured are defined in circuit
     for reg in prep_qubit_registers:
         if reg not in circuit.qregs:
