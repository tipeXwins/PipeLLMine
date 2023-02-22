--- strawberryfields/strawberryfields#336/after/connection.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#336/before/connection.py	2022-01-10 16:02:54.000000000 +0000
@@ -16,6 +16,7 @@
 """
 from datetime import datetime
 import io
+import json
 import logging
 from typing import List, Optional
 
@@ -153,7 +154,7 @@
 
         path = "/jobs"
         response = requests.post(
-            self._url(path), headers=self._headers, json={"circuit": circuit},
+            self._url(path), headers=self._headers, data=json.dumps({"circuit": circuit}),
         )
         if response.status_code == 201:
             if self._verbose:
@@ -243,7 +244,7 @@
         """
         path = "/jobs/{}".format(job_id)
         response = requests.patch(
-            self._url(path), headers=self._headers, json={"status": JobStatus.CANCELLED.value},
+            self._url(path), headers=self._headers, data={"status": JobStatus.CANCELLED.value},
         )
         if response.status_code == 204:
             if self._verbose:
