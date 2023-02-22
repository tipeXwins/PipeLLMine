--- OpenQL/OpenQL#427/after/build.cc	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#427/before/build.cc	2022-01-10 16:02:54.000000000 +0000
@@ -266,9 +266,7 @@
          * returns true when the events are caused by the same node.
          */
         utils::Bool commutes_with(const EventNodePair &enp) const {
-            if (node == enp.node) {
-                return true;
-            }
+            if (node == enp.node) return true;
             return event.commutes_with(enp.event);
         }
 
@@ -392,7 +390,7 @@
         // from the commuting list.
         auto it = commuting.begin();
         while (it != commuting.end()) {
-            if (!it->commutes_with(incoming)) {
+            if (!it->event.commutes_with(incoming.event)) {
                 evict_from_commuting(it);
             } else {
                 ++it;
@@ -521,4 +519,4 @@
 
 } // namespace ddg
 } // namespace com
-} // namespace ql
+} // namespace ql
\ No newline at end of file
