--- OpenQL/OpenQL#44/after/cc_light_scheduler.h	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#44/before/cc_light_scheduler.h	2022-01-10 16:02:54.000000000 +0000
@@ -307,7 +307,7 @@
 
 
     std::stringstream ssbundles;
-    size_t curr_cycle=0; // first instruction should be with pre-interval 1, 'bs 1'
+    size_t curr_cycle=1;
 
     for (Bundle & abundle : bundles)
     {
