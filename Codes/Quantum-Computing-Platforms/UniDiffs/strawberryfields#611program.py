--- strawberryfields/strawberryfields#611/after/program.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#611/before/program.py	2022-01-10 16:02:54.000000000 +0000
@@ -138,6 +138,7 @@
     def __init__(self, num_subsystems, name=None):
         #: str: program name
         self.name = name
+        self.type = None
         #: list[Command]: Commands constituting the quantum circuit in temporal order
         self.circuit = []
         #: bool: if True, no more Commands can be appended to the Program
