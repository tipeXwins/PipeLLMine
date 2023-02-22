--- qiskit-terra/qiskit-terra#342/after/_quantumprogram.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#342/before/_quantumprogram.py	2022-01-10 16:02:54.000000000 +0000
@@ -42,9 +42,6 @@
 from . import QISKitError
 from . import JobProcessor
 from . import QuantumJob
-from . import Measure
-from . import Gate
-from .extensions.standard.barrier import Barrier
 from ._logging import set_qiskit_logger, unset_qiskit_logger
 
 # Beta Modules
@@ -1110,19 +1107,6 @@
                 coupling_map = None
             if coupling_map == 'all-to-all':
                 coupling_map = None
-            if not backend_conf['simulator']:
-                measured_qubits = []
-                qasm_idx = []
-                for i, instruction in enumerate(circuit.data):
-                    if isinstance(instruction, Measure):
-                        measured_qubits.append(instruction.arg[0])
-                        qasm_idx.append(i)
-                    elif isinstance(instruction, Gate) and bool(set(instruction.arg) &
-                                                                set(measured_qubits)):
-                        raise QISKitError('backend "{0}" rejects gate after '
-                                          'measurement in circuit "{1}"'.format(backend, name))
-                for i, qubit in zip(qasm_idx, measured_qubits):
-                    circuit.data.insert(i, Barrier([qubit], circuit))
             dag_circuit, final_layout = openquantumcompiler.compile(
                 circuit.qasm(),
                 basis_gates=basis_gates,
