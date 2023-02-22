--- qiskit-terra/qiskit-terra#5034/after/pubsub.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#5034/before/pubsub.py	2022-01-10 16:02:54.000000000 +0000
@@ -52,7 +52,7 @@
             """Overrides the default implementation"""
             if isinstance(other, self.__class__):
                 return self.event == other.event and \
-                       id(self.callback) == id(other.callback)  # Allow 1:N subscribers
+                       self.callback.__name__ == other.callback.__name__
             return False
 
     def subscribe(self, event, callback):
