--- pennylane/pennylane#1243/after/amplitude.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1243/before/amplitude.py	2022-01-10 16:02:54.000000000 +0000
@@ -143,11 +143,6 @@
         features = self._preprocess(features, wires, pad_with, normalize)
         super().__init__(features, wires=wires, do_queue=do_queue)
 
-    def adjoint(self):  # pylint: disable=arguments-differ
-        return qml.adjoint(qml.templates.MottonenStatePreparation)(
-            self.parameters[0], wires=self.wires
-        )
-
     def expand(self):
 
         with qml.tape.QuantumTape() as tape:
