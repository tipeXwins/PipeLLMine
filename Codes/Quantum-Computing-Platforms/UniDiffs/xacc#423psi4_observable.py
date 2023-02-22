--- xacc/xacc#423/after/psi4_observable.py	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#423/before/psi4_observable.py	2022-01-10 16:02:54.000000000 +0000
@@ -20,8 +20,6 @@
     def observe(self, program):
         return self.observable.observe(program)
 
-    def postProcess(self, buffer, post_process_task, extra_data):
-        return self.observable.postProcess(buffer, post_process_task, extra_data)  
     def nBits(self):
         return self.observable.nBits()
 
