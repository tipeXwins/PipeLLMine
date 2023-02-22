--- qiskit-terra/qiskit-terra#5034/after/progressbar.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#5034/before/progressbar.py	2022-01-10 16:02:54.000000000 +0000
@@ -153,8 +153,6 @@
                                   (pbar, 0, '/', self.iter, ''))
 
     def update(self, n):
-        if not self.touched or n > self.iter:
-            return
         filled_length = int(round(50 * n / self.iter))
         pbar = '█' * filled_length + '-' * (50 - filled_length)
         time_left = self.time_remaining_est(n)
