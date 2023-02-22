--- tequila/tequila#1/after/simulator_base.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#1/before/simulator_base.py	2022-01-10 16:02:54.000000000 +0000
@@ -48,7 +48,7 @@
     def qubits(self) -> typing.Iterable[numbers.Integral]:
         return tuple(self._qubits)
 
-    def __init__(self, abstract_circuit: QCircuit, variables, noise=None,device=None,
+    def __init__(self, abstract_circuit: QCircuit, variables, noise=None,
                  use_mapping=True, optimize_circuit=True, *args, **kwargs):
         self._variables = tuple(abstract_circuit.extract_variables())
         self.use_mapping = use_mapping
@@ -91,8 +91,6 @@
 
         self.noise = noise
 
-        self.check_device(device)
-        self.device = self.retrieve_device(device)
     def __call__(self,
                  variables: typing.Dict[Variable, numbers.Real] = None,
                  samples: int = None,
@@ -140,14 +138,6 @@
                     self.add_measurement(g, result, *args, **kwargs)
         return result
 
-    def check_device(self,device):
-        if device is not None:
-            TequilaException('Devices not enabled for {}'.format(str(type(self))))
-    def retrieve_device(self,device):
-        if device is None:
-            return device
-        else:
-            TequilaException('Devices not enabled for {}'.format(str(type(self))))
     def add_parametrized_gate(self, gate, circuit, *args, **kwargs):
         TequilaException("Backend Handler needs to be overwritten for supported simulators")
 
@@ -323,8 +313,8 @@
             result = self.U.extract_variables()
         return result
 
-    def __init__(self, E, variables, noise, device):
-        self._U = self.initialize_unitary(E.U, variables=variables, noise=noise, device=device)
+    def __init__(self, E, variables, noise):
+        self._U = self.initialize_unitary(E.U, variables, noise)
         self._H = self.initialize_hamiltonian(E.H)
         self._abstract_hamiltonians = E.H
         self._variables = E.extract_variables()
@@ -368,8 +358,8 @@
     def initialize_hamiltonian(self, H):
         return tuple(H)
 
-    def initialize_unitary(self, U, variables, noise, device):
-        return self.BackendCircuitType(abstract_circuit=U, variables=variables, device=device, use_mapping=self.use_mapping,
+    def initialize_unitary(self, U, variables, noise):
+        return self.BackendCircuitType(abstract_circuit=U, variables=variables, use_mapping=self.use_mapping,
                                        noise=noise)
 
     def update_variables(self, variables):
