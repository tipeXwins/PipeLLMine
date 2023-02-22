--- Cirq/Cirq#1345/after/controlled_gate.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#1345/before/controlled_gate.py	2022-01-10 16:02:54.000000000 +0000
@@ -115,18 +115,7 @@
     def _circuit_diagram_info_(self,
                                args: protocols.CircuitDiagramInfoArgs
                                ) -> protocols.CircuitDiagramInfo:
-        sub_args = protocols.CircuitDiagramInfoArgs(
-            known_qubit_count=(args.known_qubit_count - 1
-                               if args.known_qubit_count is not None else None),
-            known_qubits=(args.known_qubits[1:]
-                          if args.known_qubits is not None else None),
-            use_unicode_characters=args.use_unicode_characters,
-            precision=args.precision,
-            qubit_map=args.qubit_map
-        )
-        sub_info = protocols.circuit_diagram_info(self.sub_gate,
-                                                  sub_args,
-                                                  None)
+        sub_info = protocols.circuit_diagram_info(self.sub_gate, args, None)
         if sub_info is None:
             return NotImplemented
         return protocols.CircuitDiagramInfo(
