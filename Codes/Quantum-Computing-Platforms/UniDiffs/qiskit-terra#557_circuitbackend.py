--- qiskit-terra/qiskit-terra#557/after/_circuitbackend.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#557/before/_circuitbackend.py	2022-01-10 16:02:54.000000000 +0000
@@ -235,7 +235,7 @@
                    "rz": [(1, 1), lambda x: self.circuit.rz(x[0][0], x[1][0])],
                    "s": [(0, 1), lambda x: self.circuit.s(x[1][0])],
                    "sdg": [(0, 1), lambda x: self.circuit.s(x[1][0]).inverse()],
-                   "t": [(0, 1), lambda x: self.circuit.t(x[1][0])],
+                   "t": [(0, 1), lambda x: self.circuit.t(x[1][0]).inverse()],
                    "tdg": [(0, 1), lambda x: self.circuit.t(x[1][0]).inverse()],
                    "u1": [(1, 1), lambda x: self.circuit.u1(x[0][0], x[1][0])],
                    "u2": [(2, 1), lambda x: self.circuit.u2(x[0][0], x[0][1],
