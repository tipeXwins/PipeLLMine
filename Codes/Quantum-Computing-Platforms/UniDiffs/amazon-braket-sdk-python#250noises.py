--- amazon-braket-sdk-python/amazon-braket-sdk-python#250/after/noises.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#250/before/noises.py	2022-01-10 16:02:54.000000000 +0000
@@ -73,7 +73,7 @@
     def __init__(self, probability: float):
         super().__init__(
             probability=probability,
-            qubit_count=None,
+            qubit_count=1,
             ascii_symbols=["BF({:.2g})".format(probability)],
         )
 
@@ -86,9 +86,6 @@
         return [K0, K1]
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def bit_flip(target: QubitSetInput, probability: float) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -141,7 +138,7 @@
     def __init__(self, probability: float):
         super().__init__(
             probability=probability,
-            qubit_count=None,
+            qubit_count=1,
             ascii_symbols=["PF({:.2g})".format(probability)],
         )
 
@@ -154,9 +151,6 @@
         return [K0, K1]
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def phase_flip(target: QubitSetInput, probability: float) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -227,7 +221,7 @@
             probX=probX,
             probY=probY,
             probZ=probZ,
-            qubit_count=None,
+            qubit_count=1,
             ascii_symbols=["PC({:.2g},{:.2g},{:.2g})".format(probX, probY, probZ)],
         )
 
@@ -244,9 +238,6 @@
         return [K0, K1, K2, K3]
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def pauli_channel(
         target: QubitSetInput, probX: float, probY: float, probZ: float
@@ -320,7 +311,7 @@
     def __init__(self, probability: float):
         super().__init__(
             probability=probability,
-            qubit_count=None,
+            qubit_count=1,
             ascii_symbols=["DEPO({:.2g})".format(probability)],
         )
 
@@ -335,9 +326,6 @@
         return [K0, K1, K2, K3]
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def depolarizing(target: QubitSetInput, probability: float) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -411,7 +399,7 @@
     def __init__(self, probability: float):
         super().__init__(
             probability=probability,
-            qubit_count=None,
+            qubit_count=2,
             ascii_symbols=["DEPO({:.2g})".format(probability)] * 2,
         )
 
@@ -437,9 +425,6 @@
         return K_list
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def two_qubit_depolarizing(
         target1: QubitInput, target2: QubitInput, probability: float
@@ -498,7 +483,7 @@
     def __init__(self, probability: float):
         super().__init__(
             probability=probability,
-            qubit_count=None,
+            qubit_count=2,
             ascii_symbols=["DEPH({:.2g})".format(probability)] * 2,
         )
 
@@ -519,9 +504,6 @@
         return [K0, K1, K2, K3]
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def two_qubit_dephasing(
         target1: QubitInput, target2: QubitInput, probability: float
@@ -573,7 +555,7 @@
     def __init__(self, gamma: float):
         super().__init__(
             gamma=gamma,
-            qubit_count=None,
+            qubit_count=1,
             ascii_symbols=["AD({:.2g})".format(gamma)],
         )
 
@@ -586,9 +568,6 @@
         return [K0, K1]
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def amplitude_damping(target: QubitSetInput, gamma: float) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -654,7 +633,7 @@
         super().__init__(
             gamma=gamma,
             probability=probability,
-            qubit_count=None,
+            qubit_count=1,
             ascii_symbols=["GAD({:.2g},{:.2g})".format(gamma, probability)],
         )
 
@@ -675,9 +654,6 @@
         return [K0, K1, K2, K3]
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def generalized_amplitude_damping(
         target: QubitSetInput, gamma: float, probability: float
@@ -736,7 +712,7 @@
     def __init__(self, gamma: float):
         super().__init__(
             gamma=gamma,
-            qubit_count=None,
+            qubit_count=1,
             ascii_symbols=["PD({:.2g})".format(gamma)],
         )
 
@@ -747,9 +723,6 @@
         K0 = np.array([[1.0, 0.0], [0.0, np.sqrt(1 - self.gamma)]], dtype=complex)
         K1 = np.array([[0.0, 0.0], [0.0, np.sqrt(self.gamma)]], dtype=complex)
         return [K0, K1]
-    @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
 
     @staticmethod
     @circuit.subroutine(register=True)
