--- pennylane/pennylane#1349/after/autograd.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1349/before/autograd.py	2022-01-10 16:02:54.000000000 +0000
@@ -119,7 +119,7 @@
                 qml.RY(0.543, wires=0)
                 qml.CNOT(wires=[0, 'a'])
                 qml.RX(0.133, wires='a')
-                qml.expval(qml.PauliZ(wires=[0]))
+                expval(qml.PauliZ(wires=[0]))
 
         By default, all parameters are trainable and will be returned:
 
