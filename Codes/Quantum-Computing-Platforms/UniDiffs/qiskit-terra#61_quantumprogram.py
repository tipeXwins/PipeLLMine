--- qiskit-terra/qiskit-terra#61/after/_quantumprogram.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#61/before/_quantumprogram.py	2022-01-10 16:02:54.000000000 +0000
@@ -24,8 +24,8 @@
 import copy
 
 # use the external IBMQuantumExperience Library
-from IBMQuantumExperience import IBMQuantumExperience
-from IBMQuantumExperience import RegisterSizeError
+from IBMQuantumExperience.IBMQuantumExperience import IBMQuantumExperience
+from IBMQuantumExperience.IBMQuantumExperience import RegisterSizeError
 
 # Stable Modules
 from . import QuantumRegister
