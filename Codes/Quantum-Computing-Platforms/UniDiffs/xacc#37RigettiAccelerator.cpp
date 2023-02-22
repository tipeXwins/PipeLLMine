--- xacc/xacc#37/after/RigettiAccelerator.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#37/before/RigettiAccelerator.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -135,12 +135,7 @@
 	} else if (type == "pyquillow") {
 
 		// Gotta do a post, then a get for this one
-		jsonStr = "{\"machine\": \"QPU\", \"program\": {\"qcid\": 5, "
-				"\"stop\": 1.0, \"start\": 0.0, \"step\": 0.04, "
-				"\"experiment\": \"rabi\", \"time\": 100.0, \"type\": "
-				"\"pyquillow\", \"device_id\": \"Z12-13-C4a2\"}, "
-				"\"userId\": \""+userId+"\", \"results\": \"\", "
-						"\"jobId\": \"\"}";
+		jsonStr = "{\"machine\": \"QPU\", \"program\": {\"qcid\": 5, \"stop\": 1.0, \"start\": 0.0, \"step\": 0.04, \"experiment\": \"rabi\", \"time\": 100.0, \"type\": \"pyquillow\", \"device_id\": \"Z12-13-C4a2\"}, \"userId\": \""+userId+"\", \"results\": \"\", \"jobId\": \"\"}";
 
 	} else {
 
