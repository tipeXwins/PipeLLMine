--- xacc/xacc#370_B/after/IBMAccelerator.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#370_B/before/IBMAccelerator.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -856,7 +856,7 @@
 
     if (cmd_def_name == "u3") {
       cmd_def->addVariables({"P0", "P1", "P2"});
-    } else if ((cmd_def_name == "u1") || (cmd_def_name == "rz")) {
+    } else if (cmd_def_name == "u1") {
       cmd_def->addVariables({"P0"});
     } else if (cmd_def_name == "u2") {
       cmd_def->addVariables({"P0", "P1"});
