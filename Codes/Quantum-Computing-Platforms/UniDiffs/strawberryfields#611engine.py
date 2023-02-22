--- strawberryfields/strawberryfields#611/after/engine.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#611/before/engine.py	2022-01-10 16:02:54.000000000 +0000
@@ -664,7 +664,7 @@
         kwargs.update(self._backend_options)
 
         device = self.device_spec
-        if isinstance(program, TDMProgram) and not device.layout_is_formatted():
+        if isinstance(program.type, TDMProgram) and not device.layout_is_formatted():
             device.fill_template(program)
 
         compiler_name = compile_options.get("compiler", device.default_compiler)
