--- amazon-braket-sdk-python/amazon-braket-sdk-python#199/after/aws_quantum_task.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#199/before/aws_quantum_task.py	2022-01-10 16:02:54.000000000 +0000
@@ -274,7 +274,7 @@
             return self._result
         try:
             async_result = self.async_result()
-            return async_result.get_loop().run_until_complete(async_result)
+            return asyncio.get_event_loop().run_until_complete(async_result)
         except asyncio.CancelledError:
             # Future was cancelled, return whatever is in self._result if anything
             self._logger.warning("Task future was cancelled")
