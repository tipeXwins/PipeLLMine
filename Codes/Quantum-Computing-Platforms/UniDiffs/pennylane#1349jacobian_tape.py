--- pennylane/pennylane#1349/after/jacobian_tape.py	2022-01-10 16:02:54.000000000 +0000
+++ pennylane/pennylane#1349/before/jacobian_tape.py	2022-01-10 16:02:54.000000000 +0000
@@ -93,10 +93,6 @@
         self.jacobian_options = {}
         self.hessian_options = {}
 
-    def copy(self, copy_operations=False, tape_cls=None):
-        copied_tape = super().copy(copy_operations=copy_operations, tape_cls=tape_cls)
-        copied_tape.jacobian_options = self.jacobian_options
-        return copied_tape
     def _grad_method(self, idx, use_graph=True, default_method="F"):
         """Determine the correct partial derivative computation method for each gate parameter.
 
