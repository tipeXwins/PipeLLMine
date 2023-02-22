--- OpenQL/OpenQL#107/after/utils.h	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#107/before/utils.h	2022-01-10 16:02:54.000000000 +0000
@@ -29,7 +29,7 @@
 #define DOUT(content)
 #endif
 
-size_t MAX_CYCLE = std::numeric_limits<int>::max();
+auto MAX_CYCLE = std::numeric_limits<int>::max();
 
 namespace ql
 {
