--- OpenQL/OpenQL#107/after/cc_light_scheduler.h	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#107/before/cc_light_scheduler.h	2022-01-10 16:02:54.000000000 +0000
@@ -683,7 +683,7 @@
     Scheduler sched;
     sched.Init(nqubits, ckt, platform, verbose);
     // sched.PrintDot();
-    bundles1 = sched.GetBundlesScheduleASAP(rm, platform, verbose);
+    bundles1 = sched.GetBundlesScheduleALAP(rm, platform, verbose);
 
     // combine parallel instrcutions of same type from different sections
     // into a single section
