--- pennylane/pennylane#1243/after/particle_conserving_u1.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1243/before/particle_conserving_u1.py	2022-01-10 16:02:54.000000000 +0000
@@ -266,7 +266,7 @@
 
         with qml.tape.QuantumTape() as tape:
 
-            qml.templates.BasisEmbedding(self.init_state, wires=self.wires)
+            qml.BasisState(self.init_state, wires=self.wires)
 
             for l in range(self.n_layers):
                 for i, wires_ in enumerate(nm_wires):
