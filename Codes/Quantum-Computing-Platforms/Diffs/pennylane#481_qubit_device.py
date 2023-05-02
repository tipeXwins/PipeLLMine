22d21
< import itertools
74a74,75
>         self._wires_measured = set()
>         """set[int]: wires acted on by quantum operations and observables"""
102a104
>         self._wires_measured = set()
131a134,135
>         # determine the wires that are measured by the circuit
>         self._wires_measured = QubitDevice.active_wires(circuit.observables)
193c197,201
<             wires.extend(op.wires)
---
>             for wire in op.wires:
>                 if isinstance(wire, int):
>                     wires.append(wire)
>                 else:
>                     wires.extend(wire)
247,248c255,256
<         number_of_states = 2 ** self.num_wires
<         rotated_prob = self.probability()
---
>         number_of_states = 2 ** len(self._wires_measured)
>         rotated_prob = self.probability(self._wires_measured)
250c258
<         self._samples = QubitDevice.states_to_binary(samples, self.num_wires)
---
>         self._samples = QubitDevice.states_to_binary(samples, number_of_states)
