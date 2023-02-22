--- qiskit-terra/qiskit-terra#4887/after/quantumcircuit.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#4887/before/quantumcircuit.py	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,6 @@
 from qiskit.util import is_main_process
 from qiskit.circuit.instruction import Instruction
 from qiskit.circuit.gate import Gate
-from qiskit.circuit.parameter import Parameter
 from qiskit.qasm.qasm import Qasm
 from qiskit.circuit.exceptions import CircuitError
 from .parameterexpression import ParameterExpression
@@ -823,10 +822,6 @@
                                'have a to_instruction() method.')
         if not isinstance(instruction, Instruction) and hasattr(instruction, "to_instruction"):
             instruction = instruction.to_instruction()
-        if hasattr(instruction, 'params'):
-            is_parameter = any([isinstance(param, Parameter) for param in instruction.params])
-            if is_parameter:
-                instruction = copy.deepcopy(instruction)
 
         expanded_qargs = [self.qbit_argument_conversion(qarg) for qarg in qargs or []]
         expanded_cargs = [self.cbit_argument_conversion(carg) for carg in cargs or []]
