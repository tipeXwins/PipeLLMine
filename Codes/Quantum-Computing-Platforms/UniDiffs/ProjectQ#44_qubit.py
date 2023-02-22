--- ProjectQ/ProjectQ#44/after/_qubit.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#44/before/_qubit.py	2022-01-10 16:02:54.000000000 +0000
@@ -83,10 +83,7 @@
         Args:
             other (BasicQubit): BasicQubit to which to compare this one
         """
-        if self.id == -1:
-            return self is other
-        return (isinstance(other, BasicQubit) and
-                self.id == other.id and
+        return (isinstance(other, self.__class__) and self.id == other.id and
                 self.engine == other.engine)
 
     def __ne__(self, other):
@@ -99,9 +96,7 @@
         Hash definition because of custom __eq__.
         Enables storing a qubit in, e.g., a set.
         """
-        if self.id == -1:
-            return object.__hash__(self)
-        return hash((self.engine, self.id))
+        return hash((self.id, self.engine, object.__hash__(self)))
 
 
 class Qubit(BasicQubit):
