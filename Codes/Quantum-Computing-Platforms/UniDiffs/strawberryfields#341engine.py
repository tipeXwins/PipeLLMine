--- strawberryfields/strawberryfields#341/after/engine.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#341/before/engine.py	2022-01-10 16:02:54.000000000 +0000
@@ -577,7 +577,7 @@
         # TODO: this should be provided by the chip API, rather
         # than built-in to Strawberry Fields.
         compile_options = compile_options or {}
-        kwargs.update(self._backend_options)
+        kwargs = kwargs.update(self._backend_options)
 
         if program.target is None or (program.target.split("_")[0] != self.target.split("_")[0]):
             # Program is either:
