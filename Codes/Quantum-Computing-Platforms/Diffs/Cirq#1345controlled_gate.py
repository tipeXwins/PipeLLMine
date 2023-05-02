118,129c118
<         sub_args = protocols.CircuitDiagramInfoArgs(
<             known_qubit_count=(args.known_qubit_count - 1
<                                if args.known_qubit_count is not None else None),
<             known_qubits=(args.known_qubits[1:]
<                           if args.known_qubits is not None else None),
<             use_unicode_characters=args.use_unicode_characters,
<             precision=args.precision,
<             qubit_map=args.qubit_map
<         )
<         sub_info = protocols.circuit_diagram_info(self.sub_gate,
<                                                   sub_args,
<                                                   None)
---
>         sub_info = protocols.circuit_diagram_info(self.sub_gate, args, None)
