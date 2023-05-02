14c14
< from typing import List, Tuple
---
> from typing import List
70,90d69
<     @staticmethod
<     def _ascii_moment_group_instructions(
<         instructions: List[Instruction],
<     ) -> List[Tuple[QubitSet, List[Instruction]]]:
<         groupings = []
<         for instr in instructions:
<             if not isinstance(instr.operator, Gate):
<                 continue
<             qubit_range = QubitSet(range(min(instr.target), max(instr.target) + 1))
<             found_grouping = False
<             for group in groupings:
<                 qubits_added = group[0]
<                 instr_group = group[1]
<                 if not qubits_added.intersection(set(qubit_range)):
<                     instr_group.append(instr)
<                     qubits_added.update(qubit_range)
<                     found_grouping = True
<                     break
<             if not found_grouping:
<                 groupings.append((qubit_range, [instr]))
<         return groupings
102,125d80
<         groupings = AsciiCircuitDiagram._ascii_moment_group_instructions(instructions)
<         column_strs = [
<             AsciiCircuitDiagram._ascii_diagram_moment_column(circuit_qubits, grouping[1])
<             for grouping in groupings
<         ]
<         lines = column_strs[0].split("\n")
<         for column_str in column_strs[1:]:
<             for i, moment_line in enumerate(column_str.split("\n")):
<                 lines[i] += moment_line
<         time_width = len(str(time))
<         symbols_width = len(lines[0]) - 1
<         if symbols_width < time_width:
<             diff = time_width - symbols_width
<             for i in range(len(lines) - 1):
<                 if lines[i].endswith("-"):
<                     lines[i] += "-" * diff
<                 else:
<                     lines[i] += " "
<         first_line = "{:^{width}}|\n".format(str(time), width=len(lines[0]) - 1)
<         return first_line + "\n".join(lines)
<     @staticmethod
<     def _ascii_diagram_moment_column(
<         circuit_qubits: QubitSet, instructions: List[Instruction]
<     ) -> str:
129a85,86
>             if not isinstance(instr.operator, Gate):
>                 continue
149c106
<         symbols_width = max([len(symbol) for symbol in symbols.values()])
---
>         symbols_width = max([len(symbol) for symbol in symbols.values()] + [len(str(time))])
151c108
<         output = ""
---
>         output = "{0:{width}}|\n".format(str(time), width=symbols_width)
