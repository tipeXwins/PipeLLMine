--- amazon-braket-sdk-python/amazon-braket-sdk-python#174/after/aws_quantum_task.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#174/before/aws_quantum_task.py	2022-01-10 16:02:54.000000000 +0000
@@ -227,7 +227,7 @@
             If `use_cached_value` is `True`, Amazon Braket is not called and the most recently
             retrieved value is used.
         """
-        if not use_cached_value or not self._metadata:
+        if not use_cached_value:
             self._metadata = self._aws_session.get_quantum_task(self._arn)
         return self._metadata
 
@@ -254,10 +254,6 @@
         if not use_cached_value and status in self.NO_RESULT_TERMINAL_STATES:
             self._logger.warning(f"Task is in terminal state {status} and no result is available")
         return status
-    def _update_status_if_nonterminal(self):
-        metadata_absent = self._metadata is None
-        cached = self._status(True)
-        return cached if cached in self.TERMINAL_STATES else self._status(metadata_absent)
 
     def result(self) -> Union[GateModelQuantumTaskResult, AnnealingQuantumTaskResult]:
         """
@@ -297,7 +293,7 @@
             self._future.done()
             and not self._future.cancelled()
             and self._result is None
-            and self._update_status_if_nonterminal() not in self.NO_RESULT_TERMINAL_STATES
+            and self._status() not in self.NO_RESULT_TERMINAL_STATES  # timed out and no result
         ):
             self._future = asyncio.get_event_loop().run_until_complete(self._create_future())
         return self._future
@@ -353,8 +349,10 @@
                 )
                 continue
             # Used cached metadata if cached status is terminal
-            task_status = self._update_status_if_nonterminal()
-            current_metadata = self.metadata(True)
+            current_metadata = self.metadata(
+                self._status(False) not in AwsQuantumTask.TERMINAL_STATES
+            )
+            task_status = self._status(False)
             self._logger.debug(f"Task {self._arn}: task status {task_status}")
             if task_status in AwsQuantumTask.RESULTS_READY_STATES:
                 result_string = self._aws_session.retrieve_s3_object_body(
