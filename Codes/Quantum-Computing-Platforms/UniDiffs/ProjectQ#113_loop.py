--- ProjectQ/ProjectQ#113/after/_loop.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#113/before/_loop.py	2022-01-10 16:02:54.000000000 +0000
@@ -147,8 +147,6 @@
             # Loop tag is supported, send everything with a LoopTag
             # Don't check is_meta_tag_supported anymore
             self._next_engines_support_loop_tag = True
-            if self._tag.num == 0:
-                return
             for cmd in command_list:
                 if cmd.gate == Allocate:
                     self._allocated_qubit_ids.add(cmd.qubits[0][0].id)
@@ -233,14 +231,10 @@
                     Rz(M_PI/3.) | qb
         """
         self.engine = engine
-        if not isinstance(num, int):
-            raise TypeError("Number of loop iterations must be an int.")
-        if num < 0:
-            raise ValueError("Number of loop iterations must be >=0.")
         self.num = num
 
     def __enter__(self):
-        if self.num != 1:
+        if self.num > 1:
             loop_eng = LoopEngine(self.num)
             loop_eng.main_engine = self.engine.main_engine
             oldnext = self.engine.next_engine
@@ -249,7 +243,7 @@
             self._loop_eng = loop_eng
 
     def __exit__(self, type, value, traceback):
-        if self.num != 1:
+        if self.num > 1:
             # remove loop handler from engine list (i.e. skip it)
             self._loop_eng.run()
             oldnext = self._loop_eng.next_engine
