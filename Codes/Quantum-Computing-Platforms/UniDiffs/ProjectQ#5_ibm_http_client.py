--- ProjectQ/ProjectQ#5/after/_ibm_http_client.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#5/before/_ibm_http_client.py	2022-01-10 16:02:54.000000000 +0000
@@ -20,7 +20,7 @@
 from requests.compat import urljoin
 
 
-_api_url = 'https://quantumexperience.ng.bluemix.net/api/'
+_api_url = 'https://qcwi-staging.mybluemix.net/api/'
 _api_url_status = 'https://quantumexperience.ng.bluemix.net/api/'
 
 class DeviceOfflineError(Exception):
