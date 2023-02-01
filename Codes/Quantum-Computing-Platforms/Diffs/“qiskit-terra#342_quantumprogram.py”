45,47d44
< from . import Measure
< from . import Gate
< from .extensions.standard.barrier import Barrier
1113,1125d1109
<             if not backend_conf['simulator']:
<                 measured_qubits = []
<                 qasm_idx = []
<                 for i, instruction in enumerate(circuit.data):
<                     if isinstance(instruction, Measure):
<                         measured_qubits.append(instruction.arg[0])
<                         qasm_idx.append(i)
<                     elif isinstance(instruction, Gate) and bool(set(instruction.arg) &
<                                                                 set(measured_qubits)):
<                         raise QISKitError('backend "{0}" rejects gate after '
<                                           'measurement in circuit "{1}"'.format(backend, name))
<                 for i, qubit in zip(qasm_idx, measured_qubits):
<                     circuit.data.insert(i, Barrier([qubit], circuit))
