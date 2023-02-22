--- OpenQL/OpenQL#428/after/build.cc	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#428/before/build.cc	2022-01-10 16:02:54.000000000 +0000
@@ -164,12 +164,8 @@
         } else if (auto dyn = stmt->as_dynamic_loop()) {
             add_expression(ir::prim::OperandMode::READ, dyn->condition);
             if (auto forl = stmt->as_for_loop()) {
-                if (!forl->initialize.empty()) {
-                    add_statement(forl->initialize);
-                }
-                if (!forl->update.empty()) {
-                    add_statement(forl->update);
-                }
+                add_statement(forl->initialize);
+                add_statement(forl->update);
             } else if (stmt->as_repeat_until_loop()) {
                 // no further dependencies
             } else {
@@ -454,9 +450,6 @@
         // Gather the object access events for this statement.
         gatherer.reset();
         gatherer.add_statement(statement);
-        if (gatherer.get().empty()) {
-            gatherer.add_reference(ir::prim::OperandMode::BARRIER, {});
-        }
 
         // Process the events.
         for (const auto &event : gatherer.get()) {
@@ -533,4 +526,4 @@
 
 } // namespace ddg
 } // namespace com
-} // namespace ql
+} // namespace ql
\ No newline at end of file
