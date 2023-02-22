--- strawberryfields/strawberryfields#611/after/devicespec.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#611/before/devicespec.py	2022-01-10 16:02:54.000000000 +0000
@@ -23,7 +23,6 @@
 
 import strawberryfields as sf
 from strawberryfields.compilers import Ranges
-from strawberryfields.tdm.tdmprogram import TDMProgram
 
 
 class DeviceSpec:
@@ -110,7 +109,7 @@
         if self.layout_is_formatted():
             return
 
-        if isinstance(program, TDMProgram):
+        if program.type == "tdm":
             self._spec["layout"] = self._spec["layout"].format(
                 target=self.target, tm=program.timebins
             )
