--- strawberryfields/strawberryfields#91/after/ops.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#91/before/ops.py	2022-01-10 16:02:54.000000000 +0000
@@ -1236,7 +1236,7 @@
         super().__init__(par=[])
 
 
-class _Delete(MetaOperation):
+class Delete(MetaOperation):
     """Deletes one or more existing modes.
     Also accessible via the shortcut variable ``Del``.
 
@@ -1272,11 +1272,11 @@
     # create RegRefs for the new modes
     refs = Program._current_context._add_subsystems(n)
     # append the actual Operation to the Program
-    Program._current_context.append(_New_modes(n), refs)
+    Program._current_context.append(New_modes(n), refs)
     return refs
 
 
-class _New_modes(MetaOperation):
+class New_modes(MetaOperation):
     """Used internally for adding new modes to the system in a deferred way.
 
     This class cannot be used with the :meth:`__or__` syntax since it would be misleading.
@@ -1630,7 +1630,7 @@
 #=======================================================================
 # Shorthands, e.g. pre-constructed singleton-like objects
 
-Del = _Delete()
+Del = Delete()
 Vac = Vacuum()
 Measure = MeasureFock()
 MeasureX = MeasureHomodyne(0)
