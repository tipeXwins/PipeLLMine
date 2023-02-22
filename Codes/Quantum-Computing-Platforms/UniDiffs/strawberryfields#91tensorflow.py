--- strawberryfields/strawberryfields#91/after/tensorflow.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#91/before/tensorflow.py	2022-01-10 16:02:54.000000000 +0000
@@ -26,8 +26,8 @@
     primitives = {
         # meta operations
         "All",
-        "_New_modes",
-        "_Delete",
+        "New_modes",
+        "Delete",
         # state preparations
         "Vacuum",
         "Coherent",
@@ -65,4 +65,4 @@
         "S2gate": {},
         "CXgate": {},
         "CZgate": {},
-    }	
+    }
