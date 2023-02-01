51c51
<     def __init__(self, abstract_circuit: QCircuit, variables, noise=None,device=None,
---
>     def __init__(self, abstract_circuit: QCircuit, variables, noise=None,
94,95d93
<         self.check_device(device)
<         self.device = self.retrieve_device(device)
143,150d140
<     def check_device(self,device):
<         if device is not None:
<             TequilaException('Devices not enabled for {}'.format(str(type(self))))
<     def retrieve_device(self,device):
<         if device is None:
<             return device
<         else:
<             TequilaException('Devices not enabled for {}'.format(str(type(self))))
326,327c316,317
<     def __init__(self, E, variables, noise, device):
<         self._U = self.initialize_unitary(E.U, variables=variables, noise=noise, device=device)
---
>     def __init__(self, E, variables, noise):
>         self._U = self.initialize_unitary(E.U, variables, noise)
371,372c361,362
<     def initialize_unitary(self, U, variables, noise, device):
<         return self.BackendCircuitType(abstract_circuit=U, variables=variables, device=device, use_mapping=self.use_mapping,
---
>     def initialize_unitary(self, U, variables, noise):
>         return self.BackendCircuitType(abstract_circuit=U, variables=variables, use_mapping=self.use_mapping,
