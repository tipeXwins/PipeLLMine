--- amazon-braket-sdk-python/amazon-braket-sdk-python#250/after/gates.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#250/before/gates.py	2022-01-10 16:02:54.000000000 +0000
@@ -43,7 +43,7 @@
     """Hadamard gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["H"])
+        super().__init__(qubit_count=1, ascii_symbols=["H"])
 
     def to_ir(self, target: QubitSet):
         return ir.H.construct(target=target[0])
@@ -52,9 +52,6 @@
         return 1.0 / np.sqrt(2.0) * np.array([[1.0, 1.0], [1.0, -1.0]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def h(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -69,7 +66,7 @@
             >>> circ = Circuit().h(0)
             >>> circ = Circuit().h([0, 1, 2])
         """
-        return [Instruction(H(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.H(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(H)
@@ -79,7 +76,7 @@
     """Identity gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["I"])
+        super().__init__(qubit_count=1, ascii_symbols=["I"])
 
     def to_ir(self, target: QubitSet):
         return ir.I.construct(target=target[0])
@@ -88,9 +85,6 @@
         return np.eye(2, dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def i(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -105,7 +99,7 @@
             >>> circ = Circuit().i(0)
             >>> circ = Circuit().i([0, 1, 2])
         """
-        return [Instruction(I(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.I(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(I)
@@ -115,7 +109,7 @@
     """Pauli-X gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["X"])
+        super().__init__(qubit_count=1, ascii_symbols=["X"])
 
     def to_ir(self, target: QubitSet):
         return ir.X.construct(target=target[0])
@@ -124,9 +118,6 @@
         return np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def x(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -141,7 +132,7 @@
             >>> circ = Circuit().x(0)
             >>> circ = Circuit().x([0, 1, 2])
         """
-        return [Instruction(X(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.X(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(X)
@@ -151,7 +142,7 @@
     """Pauli-Y gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["Y"])
+        super().__init__(qubit_count=1, ascii_symbols=["Y"])
 
     def to_ir(self, target: QubitSet):
         return ir.Y.construct(target=target[0])
@@ -160,9 +151,6 @@
         return np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def y(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -177,7 +165,7 @@
             >>> circ = Circuit().y(0)
             >>> circ = Circuit().y([0, 1, 2])
         """
-        return [Instruction(Y(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.Y(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(Y)
@@ -187,7 +175,7 @@
     """Pauli-Z gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["Z"])
+        super().__init__(qubit_count=1, ascii_symbols=["Z"])
 
     def to_ir(self, target: QubitSet):
         return ir.Z.construct(target=target[0])
@@ -196,9 +184,6 @@
         return np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def z(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -213,7 +198,7 @@
             >>> circ = Circuit().z(0)
             >>> circ = Circuit().z([0, 1, 2])
         """
-        return [Instruction(Z(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.Z(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(Z)
@@ -223,7 +208,7 @@
     """S gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["S"])
+        super().__init__(qubit_count=1, ascii_symbols=["S"])
 
     def to_ir(self, target: QubitSet):
         return ir.S.construct(target=target[0])
@@ -233,9 +218,6 @@
         return np.array([[1.0, 0.0], [0.0, 1.0j]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def s(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -250,7 +232,7 @@
             >>> circ = Circuit().s(0)
             >>> circ = Circuit().s([0, 1, 2])
         """
-        return [Instruction(S(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.S(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(S)
@@ -260,7 +242,7 @@
     """Conjugate transpose of S gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["Si"])
+        super().__init__(qubit_count=1, ascii_symbols=["Si"])
 
     def to_ir(self, target: QubitSet):
         return ir.Si.construct(target=target[0])
@@ -269,9 +251,6 @@
         return np.array([[1, 0], [0, -1j]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def si(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -286,7 +265,7 @@
             >>> circ = Circuit().si(0)
             >>> circ = Circuit().si([0, 1, 2])
         """
-        return [Instruction(Si(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.Si(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(Si)
@@ -296,7 +275,7 @@
     """T gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["T"])
+        super().__init__(qubit_count=1, ascii_symbols=["T"])
 
     def to_ir(self, target: QubitSet):
         return ir.T.construct(target=target[0])
@@ -305,9 +284,6 @@
         return np.array([[1.0, 0.0], [0.0, np.exp(1j * np.pi / 4)]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def t(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -322,7 +298,7 @@
             >>> circ = Circuit().t(0)
             >>> circ = Circuit().t([0, 1, 2])
         """
-        return [Instruction(T(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.T(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(T)
@@ -332,7 +308,7 @@
     """Conjugate transpose of T gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["Ti"])
+        super().__init__(qubit_count=1, ascii_symbols=["Ti"])
 
     def to_ir(self, target: QubitSet):
         return ir.Ti.construct(target=target[0])
@@ -341,9 +317,6 @@
         return np.array([[1.0, 0.0], [0.0, np.exp(-1j * np.pi / 4)]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def ti(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -358,7 +331,7 @@
             >>> circ = Circuit().ti(0)
             >>> circ = Circuit().ti([0, 1, 2])
         """
-        return [Instruction(Ti(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.Ti(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(Ti)
@@ -368,7 +341,7 @@
     """Square root of not gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["V"])
+        super().__init__(qubit_count=1, ascii_symbols=["V"])
 
     def to_ir(self, target: QubitSet):
         return ir.V.construct(target=target[0])
@@ -377,9 +350,6 @@
         return np.array([[0.5 + 0.5j, 0.5 - 0.5j], [0.5 - 0.5j, 0.5 + 0.5j]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def v(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -394,7 +364,7 @@
             >>> circ = Circuit().v(0)
             >>> circ = Circuit().v([0, 1, 2])
         """
-        return [Instruction(V(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.V(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(V)
@@ -404,7 +374,7 @@
     """Conjugate transpose of square root of not gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["Vi"])
+        super().__init__(qubit_count=1, ascii_symbols=["Vi"])
 
     def to_ir(self, target: QubitSet):
         return ir.Vi.construct(target=target[0])
@@ -413,9 +383,6 @@
         return np.array(([[0.5 - 0.5j, 0.5 + 0.5j], [0.5 + 0.5j, 0.5 - 0.5j]]), dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
     def vi(target: QubitSetInput) -> Iterable[Instruction]:
         """Registers this function into the circuit class.
@@ -430,7 +397,7 @@
             >>> circ = Circuit().vi(0)
             >>> circ = Circuit().vi([0, 1, 2])
         """
-        return [Instruction(Vi(), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.Vi(), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(Vi)
@@ -447,7 +414,7 @@
     """
 
     def __init__(self, angle: float):
-        super().__init__(angle=angle, qubit_count=None, ascii_symbols=["Rx({:.3g})".format(angle)])
+        super().__init__(angle=angle, qubit_count=1, ascii_symbols=["Rx({:.3g})".format(angle)])
 
     def to_ir(self, target: QubitSet):
         return ir.Rx.construct(target=target[0], angle=self.angle)
@@ -458,11 +425,8 @@
         return np.array([[cos, -1j * sin], [-1j * sin, cos]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
-    def rx(target: QubitInput, angle: float) -> Iterable[Instruction]:
+    def rx(target: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
 
         Args:
@@ -470,12 +434,12 @@
             angle (float): Angle in radians.
 
         Returns:
-            Iterable[Instruction]: Rx instruction.
+            Instruction: Rx instruction.
 
         Examples:
             >>> circ = Circuit().rx(0, 0.15)
         """
-        return [Instruction(Rx(angle), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.Rx(angle), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(Rx)
@@ -489,7 +453,7 @@
     """
 
     def __init__(self, angle: float):
-        super().__init__(angle=angle, qubit_count=None, ascii_symbols=["Ry({:.3g})".format(angle)])
+        super().__init__(angle=angle, qubit_count=1, ascii_symbols=["Ry({:.3g})".format(angle)])
 
     def to_ir(self, target: QubitSet):
         return ir.Ry.construct(target=target[0], angle=self.angle)
@@ -500,11 +464,8 @@
         return np.array([[cos, -sin], [+sin, cos]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
-    def ry(target: QubitInput, angle: float) -> Iterable[Instruction]:
+    def ry(target: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
 
         Args:
@@ -512,12 +473,12 @@
             angle (float): Angle in radians.
 
         Returns:
-            Iterable[Instruction]: Ry instruction.
+            Instruction: Ry instruction.
 
         Examples:
             >>> circ = Circuit().ry(0, 0.15)
         """
-        return [Instruction(Ry(angle), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.Ry(angle), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(Ry)
@@ -531,7 +492,7 @@
     """
 
     def __init__(self, angle: float):
-        super().__init__(angle=angle, qubit_count=None, ascii_symbols=["Rz({:.3g})".format(angle)])
+        super().__init__(angle=angle, qubit_count=1, ascii_symbols=["Rz({:.3g})".format(angle)])
 
     def to_ir(self, target: QubitSet):
         return ir.Rz.construct(target=target[0], angle=self.angle)
@@ -542,11 +503,8 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
-    def rz(target: QubitInput, angle: float) -> Iterable[Instruction]:
+    def rz(target: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
 
         Args:
@@ -554,12 +512,12 @@
             angle (float): Angle in radians.
 
         Returns:
-            Iterable[Instruction]: Rz instruction.
+            Instruction: Rz instruction.
 
         Examples:
             >>> circ = Circuit().rz(0, 0.15)
         """
-        return [Instruction(Rz(angle), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.Rz(angle), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(Rz)
@@ -573,9 +531,7 @@
     """
 
     def __init__(self, angle: float):
-        super().__init__(
-            angle=angle, qubit_count=None, ascii_symbols=["PHASE({:.3g})".format(angle)]
-        )
+        super().__init__(angle=angle, qubit_count=1, ascii_symbols=["PHASE({:.3g})".format(angle)])
 
     def to_ir(self, target: QubitSet):
         return ir.PhaseShift.construct(target=target[0], angle=self.angle)
@@ -584,11 +540,8 @@
         return np.array([[1.0, 0.0], [0.0, np.exp(1j * self.angle)]], dtype=complex)
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 1
-    @staticmethod
     @circuit.subroutine(register=True)
-    def phaseshift(target: QubitInput, angle: float) -> Iterable[Instruction]:
+    def phaseshift(target: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
 
         Args:
@@ -596,12 +549,12 @@
             angle (float): Angle in radians.
 
         Returns:
-            Iterable[Instruction]: PhaseShift instruction.
+            Instruction: PhaseShift instruction.
 
         Examples:
             >>> circ = Circuit().phaseshift(0, 0.15)
         """
-        return [Instruction(PhaseShift(angle), target=qubit) for qubit in QubitSet(target)]
+        return [Instruction(Gate.PhaseShift(angle), target=qubit) for qubit in QubitSet(target)]
 
 
 Gate.register_gate(PhaseShift)
@@ -614,7 +567,7 @@
     """Controlled NOT gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["C", "X"])
+        super().__init__(qubit_count=2, ascii_symbols=["C", "X"])
 
     def to_ir(self, target: QubitSet):
         return ir.CNot.construct(control=target[0], target=target[1])
@@ -631,9 +584,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def cnot(control: QubitInput, target: QubitInput) -> Instruction:
         """Registers this function into the circuit class.
@@ -648,7 +598,7 @@
         Examples:
             >>> circ = Circuit().cnot(0, 1)
         """
-        return Instruction(CNot(), target=[control, target])
+        return Instruction(Gate.CNot(), target=[control, target])
 
 
 Gate.register_gate(CNot)
@@ -658,7 +608,7 @@
     """Swap gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["SWAP", "SWAP"])
+        super().__init__(qubit_count=2, ascii_symbols=["SWAP", "SWAP"])
 
     def to_ir(self, target: QubitSet):
         return ir.Swap.construct(targets=[target[0], target[1]])
@@ -675,9 +625,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def swap(target1: QubitInput, target2: QubitInput) -> Instruction:
         """Registers this function into the circuit class.
@@ -692,7 +639,7 @@
         Examples:
             >>> circ = Circuit().swap(0, 1)
         """
-        return Instruction(Swap(), target=[target1, target2])
+        return Instruction(Gate.Swap(), target=[target1, target2])
 
 
 Gate.register_gate(Swap)
@@ -702,7 +649,7 @@
     """ISwap gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["ISWAP", "ISWAP"])
+        super().__init__(qubit_count=2, ascii_symbols=["ISWAP", "ISWAP"])
 
     def to_ir(self, target: QubitSet):
         return ir.ISwap.construct(targets=[target[0], target[1]])
@@ -719,9 +666,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def iswap(target1: QubitInput, target2: QubitInput) -> Instruction:
         """Registers this function into the circuit class.
@@ -736,7 +680,7 @@
         Examples:
             >>> circ = Circuit().iswap(0, 1)
         """
-        return Instruction(ISwap(), target=[target1, target2])
+        return Instruction(Gate.ISwap(), target=[target1, target2])
 
 
 Gate.register_gate(ISwap)
@@ -752,7 +696,7 @@
     def __init__(self, angle: float):
         super().__init__(
             angle=angle,
-            qubit_count=None,
+            qubit_count=2,
             ascii_symbols=["PSWAP({:.3g})".format(angle), "PSWAP({:.3g})".format(angle)],
         )
 
@@ -771,9 +715,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def pswap(target1: QubitInput, target2: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -788,7 +729,7 @@
         Examples:
             >>> circ = Circuit().pswap(0, 1, 0.15)
         """
-        return Instruction(PSwap(angle), target=[target1, target2])
+        return Instruction(Gate.PSwap(angle), target=[target1, target2])
 
 
 Gate.register_gate(PSwap)
@@ -806,7 +747,7 @@
     def __init__(self, angle: float):
         super().__init__(
             angle=angle,
-            qubit_count=None,
+            qubit_count=2,
             ascii_symbols=["XY({:.3g})".format(angle), "XY({:.3g})".format(angle)],
         )
 
@@ -827,9 +768,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def xy(target1: QubitInput, target2: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -844,7 +782,7 @@
         Examples:
             >>> circ = Circuit().xy(0, 1, 0.15)
         """
-        return Instruction(XY(angle), target=[target1, target2])
+        return Instruction(Gate.XY(angle), target=[target1, target2])
 
 
 Gate.register_gate(XY)
@@ -859,7 +797,7 @@
 
     def __init__(self, angle: float):
         super().__init__(
-            angle=angle, qubit_count=None, ascii_symbols=["C", "PHASE({:.3g})".format(angle)]
+            angle=angle, qubit_count=2, ascii_symbols=["C", "PHASE({:.3g})".format(angle)]
         )
 
     def to_ir(self, target: QubitSet):
@@ -869,9 +807,6 @@
         return np.diag([1.0, 1.0, 1.0, np.exp(1j * self.angle)])
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def cphaseshift(control: QubitInput, target: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -887,7 +822,7 @@
         Examples:
             >>> circ = Circuit().cphaseshift(0, 1, 0.15)
         """
-        return Instruction(CPhaseShift(angle), target=[control, target])
+        return Instruction(Gate.CPhaseShift(angle), target=[control, target])
 
 
 Gate.register_gate(CPhaseShift)
@@ -902,7 +837,7 @@
 
     def __init__(self, angle: float):
         super().__init__(
-            angle=angle, qubit_count=None, ascii_symbols=["C", "PHASE00({:.3g})".format(angle)]
+            angle=angle, qubit_count=2, ascii_symbols=["C", "PHASE00({:.3g})".format(angle)]
         )
 
     def to_ir(self, target: QubitSet):
@@ -912,9 +847,6 @@
         return np.diag([np.exp(1j * self.angle), 1.0, 1.0, 1.0])
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def cphaseshift00(control: QubitInput, target: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -930,7 +862,7 @@
         Examples:
             >>> circ = Circuit().cphaseshift00(0, 1, 0.15)
         """
-        return Instruction(CPhaseShift00(angle), target=[control, target])
+        return Instruction(Gate.CPhaseShift00(angle), target=[control, target])
 
 
 Gate.register_gate(CPhaseShift00)
@@ -945,7 +877,7 @@
 
     def __init__(self, angle: float):
         super().__init__(
-            angle=angle, qubit_count=None, ascii_symbols=["C", "PHASE01({:.3g})".format(angle)]
+            angle=angle, qubit_count=2, ascii_symbols=["C", "PHASE01({:.3g})".format(angle)]
         )
 
     def to_ir(self, target: QubitSet):
@@ -955,9 +887,6 @@
         return np.diag([1.0, np.exp(1j * self.angle), 1.0, 1.0])
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def cphaseshift01(control: QubitInput, target: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -973,7 +902,7 @@
         Examples:
             >>> circ = Circuit().cphaseshift01(0, 1, 0.15)
         """
-        return Instruction(CPhaseShift01(angle), target=[control, target])
+        return Instruction(Gate.CPhaseShift01(angle), target=[control, target])
 
 
 Gate.register_gate(CPhaseShift01)
@@ -988,7 +917,7 @@
 
     def __init__(self, angle: float):
         super().__init__(
-            angle=angle, qubit_count=None, ascii_symbols=["C", "PHASE10({:.3g})".format(angle)]
+            angle=angle, qubit_count=2, ascii_symbols=["C", "PHASE10({:.3g})".format(angle)]
         )
 
     def to_ir(self, target: QubitSet):
@@ -998,9 +927,6 @@
         return np.diag([1.0, 1.0, np.exp(1j * self.angle), 1.0])
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def cphaseshift10(control: QubitInput, target: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -1016,7 +942,7 @@
         Examples:
             >>> circ = Circuit().cphaseshift10(0, 1, 0.15)
         """
-        return Instruction(CPhaseShift10(angle), target=[control, target])
+        return Instruction(Gate.CPhaseShift10(angle), target=[control, target])
 
 
 Gate.register_gate(CPhaseShift10)
@@ -1026,7 +952,7 @@
     """Controlled Pauli-Y gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["C", "Y"])
+        super().__init__(qubit_count=2, ascii_symbols=["C", "Y"])
 
     def to_ir(self, target: QubitSet):
         return ir.CY.construct(control=target[0], target=target[1])
@@ -1043,9 +969,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def cy(control: QubitInput, target: QubitInput) -> Instruction:
         """Registers this function into the circuit class.
@@ -1060,7 +983,7 @@
         Examples:
             >>> circ = Circuit().cy(0, 1)
         """
-        return Instruction(CY(), target=[control, target])
+        return Instruction(Gate.CY(), target=[control, target])
 
 
 Gate.register_gate(CY)
@@ -1070,7 +993,7 @@
     """Controlled Pauli-Z gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["C", "Z"])
+        super().__init__(qubit_count=2, ascii_symbols=["C", "Z"])
 
     def to_ir(self, target: QubitSet):
         return ir.CZ.construct(control=target[0], target=target[1])
@@ -1079,9 +1002,6 @@
         return np.diag([1.0, 1.0, 1.0, -1.0])
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def cz(control: QubitInput, target: QubitInput) -> Instruction:
         """Registers this function into the circuit class.
@@ -1096,7 +1016,7 @@
         Examples:
             >>> circ = Circuit().cz(0, 1)
         """
-        return Instruction(CZ(), target=[control, target])
+        return Instruction(Gate.CZ(), target=[control, target])
 
 
 Gate.register_gate(CZ)
@@ -1114,7 +1034,7 @@
     def __init__(self, angle: float):
         super().__init__(
             angle=angle,
-            qubit_count=None,
+            qubit_count=2,
             ascii_symbols=["XX({:.3g})".format(angle), "XX({:.3g})".format(angle)],
         )
 
@@ -1135,9 +1055,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def xx(target1: QubitInput, target2: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -1153,7 +1070,7 @@
         Examples:
             >>> circ = Circuit().xx(0, 1, 0.15)
         """
-        return Instruction(XX(angle), target=[target1, target2])
+        return Instruction(Gate.XX(angle), target=[target1, target2])
 
 
 Gate.register_gate(XX)
@@ -1171,7 +1088,7 @@
     def __init__(self, angle: float):
         super().__init__(
             angle=angle,
-            qubit_count=None,
+            qubit_count=2,
             ascii_symbols=["YY({:.3g})".format(angle), "YY({:.3g})".format(angle)],
         )
 
@@ -1192,9 +1109,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def yy(target1: QubitInput, target2: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -1210,7 +1124,7 @@
         Examples:
             >>> circ = Circuit().yy(0, 1, 0.15)
         """
-        return Instruction(YY(angle), target=[target1, target2])
+        return Instruction(Gate.YY(angle), target=[target1, target2])
 
 
 Gate.register_gate(YY)
@@ -1228,7 +1142,7 @@
     def __init__(self, angle: float):
         super().__init__(
             angle=angle,
-            qubit_count=None,
+            qubit_count=2,
             ascii_symbols=["ZZ({:.3g})".format(angle), "ZZ({:.3g})".format(angle)],
         )
 
@@ -1247,9 +1161,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 2
-    @staticmethod
     @circuit.subroutine(register=True)
     def zz(target1: QubitInput, target2: QubitInput, angle: float) -> Instruction:
         """Registers this function into the circuit class.
@@ -1265,7 +1176,7 @@
         Examples:
             >>> circ = Circuit().zz(0, 1, 0.15)
         """
-        return Instruction(ZZ(angle), target=[target1, target2])
+        return Instruction(Gate.ZZ(angle), target=[target1, target2])
 
 
 Gate.register_gate(ZZ)
@@ -1278,7 +1189,7 @@
     """CCNOT gate or Toffoli gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["C", "C", "X"])
+        super().__init__(qubit_count=3, ascii_symbols=["C", "C", "X"])
 
     def to_ir(self, target: QubitSet):
         return ir.CCNot.construct(controls=[target[0], target[1]], target=target[2])
@@ -1299,9 +1210,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 3
-    @staticmethod
     @circuit.subroutine(register=True)
     def ccnot(control1: QubitInput, control2: QubitInput, target: QubitInput) -> Instruction:
         """Registers this function into the circuit class.
@@ -1317,7 +1225,7 @@
         Examples:
             >>> circ = Circuit().ccnot(0, 1, 2)
         """
-        return Instruction(CCNot(), target=[control1, control2, target])
+        return Instruction(Gate.CCNot(), target=[control1, control2, target])
 
 
 Gate.register_gate(CCNot)
@@ -1327,7 +1235,7 @@
     """Controlled Swap gate."""
 
     def __init__(self):
-        super().__init__(qubit_count=None, ascii_symbols=["C", "SWAP", "SWAP"])
+        super().__init__(qubit_count=3, ascii_symbols=["C", "SWAP", "SWAP"])
 
     def to_ir(self, target: QubitSet):
         return ir.CSwap.construct(control=target[0], targets=[target[1], target[2]])
@@ -1348,9 +1256,6 @@
         )
 
     @staticmethod
-    def fixed_qubit_count() -> int:
-        return 3
-    @staticmethod
     @circuit.subroutine(register=True)
     def cswap(control: QubitInput, target1: QubitInput, target2: QubitInput) -> Instruction:
         """Registers this function into the circuit class.
@@ -1366,7 +1271,7 @@
         Examples:
             >>> circ = Circuit().cswap(0, 1, 2)
         """
-        return Instruction(CSwap(), target=[control, target1, target2])
+        return Instruction(Gate.CSwap(), target=[control, target1, target2])
 
 
 Gate.register_gate(CSwap)
@@ -1440,7 +1345,7 @@
         if 2 ** len(targets) != matrix.shape[0]:
             raise ValueError("Dimensions of the supplied unitary are incompatible with the targets")
 
-        return Instruction(Unitary(matrix, display_name), target=targets)
+        return Instruction(Gate.Unitary(matrix, display_name), target=targets)
 
 
 Gate.register_gate(Unitary)
