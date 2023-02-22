--- amazon-braket-sdk-python/amazon-braket-sdk-python#44/after/ascii_circuit_diagram.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#44/before/ascii_circuit_diagram.py	2022-01-10 16:02:54.000000000 +0000
@@ -11,7 +11,7 @@
 # ANY KIND, either express or implied. See the License for the specific
 # language governing permissions and limitations under the License.
 
-from typing import List, Tuple
+from typing import List
 
 from braket.circuits.circuit_diagram import CircuitDiagram
 from braket.circuits.gate import Gate
@@ -67,27 +67,6 @@
         lines.append(lines[0])
 
         return "\n".join(lines)
-    @staticmethod
-    def _ascii_moment_group_instructions(
-        instructions: List[Instruction],
-    ) -> List[Tuple[QubitSet, List[Instruction]]]:
-        groupings = []
-        for instr in instructions:
-            if not isinstance(instr.operator, Gate):
-                continue
-            qubit_range = QubitSet(range(min(instr.target), max(instr.target) + 1))
-            found_grouping = False
-            for group in groupings:
-                qubits_added = group[0]
-                instr_group = group[1]
-                if not qubits_added.intersection(set(qubit_range)):
-                    instr_group.append(instr)
-                    qubits_added.update(qubit_range)
-                    found_grouping = True
-                    break
-            if not found_grouping:
-                groupings.append((qubit_range, [instr]))
-        return groupings
 
     @staticmethod
     def _ascii_diagram_moment(
@@ -99,34 +78,12 @@
         Returns:
             str: An ASCII string diagram for the specified moment in time.
         """
-        groupings = AsciiCircuitDiagram._ascii_moment_group_instructions(instructions)
-        column_strs = [
-            AsciiCircuitDiagram._ascii_diagram_moment_column(circuit_qubits, grouping[1])
-            for grouping in groupings
-        ]
-        lines = column_strs[0].split("\n")
-        for column_str in column_strs[1:]:
-            for i, moment_line in enumerate(column_str.split("\n")):
-                lines[i] += moment_line
-        time_width = len(str(time))
-        symbols_width = len(lines[0]) - 1
-        if symbols_width < time_width:
-            diff = time_width - symbols_width
-            for i in range(len(lines) - 1):
-                if lines[i].endswith("-"):
-                    lines[i] += "-" * diff
-                else:
-                    lines[i] += " "
-        first_line = "{:^{width}}|\n".format(str(time), width=len(lines[0]) - 1)
-        return first_line + "\n".join(lines)
-    @staticmethod
-    def _ascii_diagram_moment_column(
-        circuit_qubits: QubitSet, instructions: List[Instruction]
-    ) -> str:
         symbols = {qubit: "-" for qubit in circuit_qubits}
         margins = {qubit: " " for qubit in circuit_qubits}
 
         for instr in instructions:
+            if not isinstance(instr.operator, Gate):
+                continue
 
             qubits = circuit_qubits.intersection(
                 set(range(min(instr.target), max(instr.target) + 1))
@@ -146,9 +103,9 @@
                 if qubit != min(instr.target):
                     margins[qubit] = "|"
 
-        symbols_width = max([len(symbol) for symbol in symbols.values()])
+        symbols_width = max([len(symbol) for symbol in symbols.values()] + [len(str(time))])
 
-        output = ""
+        output = "{0:{width}}|\n".format(str(time), width=symbols_width)
         for qubit in circuit_qubits:
             output += "{0:{width}}\n".format(margins[qubit], width=symbols_width + 1)
             output += "{0:{fill}{align}{width}}\n".format(
