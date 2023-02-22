--- pennylane/pennylane#1243/after/utils.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1243/before/utils.py	2022-01-10 16:02:54.000000000 +0000
@@ -305,8 +305,8 @@
             "Please use inv on the function including its arguments, as in inv(template(args))."
         )
     elif isinstance(operation_list, qml.tape.QuantumTape):
-        new_tape = operation_list.adjoint()
-        return new_tape
+        operation_list.inv()
+        return operation_list
     elif not isinstance(operation_list, Iterable):
         raise ValueError("The provided operation_list is not iterable.")
 
@@ -334,12 +334,13 @@
             # exist on the queuing context
             pass
 
-    def qfunc():
+    with qml.tape.QuantumTape() as tape:
         for o in operation_list:
             o.queue()
+            if o.inverse:
+                o.inv()
 
-    with qml.tape.QuantumTape() as tape:
-        qml.adjoint(qfunc)()
+    tape.inv()
     return tape
 
 
