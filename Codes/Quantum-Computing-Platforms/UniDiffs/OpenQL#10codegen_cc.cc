--- OpenQL/OpenQL#10/after/codegen_cc.cc	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#10/before/codegen_cc.cc	2022-01-10 16:02:54.000000000 +0000
@@ -553,7 +553,7 @@
 {
     comment(SS2S("# FOR_START(" << iterations << ")"));
     // FIXME: reserve register
-    emit("", "move", SS2S(iterations << ",R62"), "# R62 is the 'for loop counter'");        // FIXME: fixed reg, no nested loops
+    emit("", "move", SS2S(iterations << ",R63"), "# R63 is the 'for loop counter'");        // FIXME: fixed reg, no nested loops
     emit((label+":").c_str(), "", SS2S(""), "# ");        // just a label
 }
 
@@ -561,7 +561,7 @@
 {
     comment("# FOR_END");
     // FIXME: free register
-    emit("", "loop", SS2S("R62,@" << label), "# R62 is the 'for loop counter'");        // FIXME: fixed reg, no nested loops
+    emit("", "loop", SS2S("R63,@" << label), "# R63 is the 'for loop counter'");        // FIXME: fixed reg, no nested loops
 }
 
 void codegen_cc::do_while_start(const std::string &label)
