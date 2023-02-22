--- tequila/tequila#97/after/simulator_base.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#97/before/simulator_base.py	2022-01-10 16:02:54.000000000 +0000
@@ -8,7 +8,7 @@
 from tequila.objective.objective import Variable, format_variable_dictionary
 from tequila.circuit import compiler
 
-import numbers, typing, numpy, copy
+import numbers, typing, numpy
 
 from dataclasses import dataclass
 
@@ -475,7 +475,7 @@
             basis_change += change_basis(target=idx, axis=p)
 
         # add basis change to the circuit
-        circuit = self.create_circuit(circuit=copy.deepcopy(self.circuit), abstract_circuit=basis_change)
+        circuit = self.create_circuit(circuit=self.circuit, abstract_circuit=basis_change)
         # run simulators
         counts = self.sample(samples=samples, circuit=circuit, read_out_qubits=qubits, variables=variables, *args,
                              **kwargs)
