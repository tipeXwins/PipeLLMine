--- Cirq/Cirq#2758/after/n_qubit_tomography_test.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#2758/before/n_qubit_tomography_test.py	2022-01-10 16:02:54.000000000 +0000
@@ -30,7 +30,7 @@
             bit = state & (1 << (n - i - 1))
             if bit:
                 circuit.append(cirq.X(q))
-        res = cirq.experiments.state_tomography(cirq.Simulator(seed=87539319),
+        res = cirq.experiments.state_tomography(cirq.Simulator(),
                                                 qubits,
                                                 circuit,
                                                 repetitions=1000,
@@ -47,7 +47,7 @@
     circuit.append(cirq.CNOT(cirq.LineQubit(0), cirq.LineQubit(1)))
     circuit.append(cirq.CNOT(cirq.LineQubit(0), cirq.LineQubit(2)))
     res = cirq.experiments.state_tomography(
-        cirq.Simulator(seed=87539319),
+        cirq.Simulator(),
         [cirq.LineQubit(0),
          cirq.LineQubit(1),
          cirq.LineQubit(2)],
@@ -94,7 +94,7 @@
     ), (Q1, Q0, Q2, Q3)),
 ))
 def test_density_matrix_from_state_tomography_is_correct(circuit, qubits):
-    sim = cirq.Simulator(seed=87539319)
+    sim = cirq.Simulator()
     tomography_result = cirq.experiments.state_tomography(sim,
                                                           qubits,
                                                           circuit,
@@ -113,7 +113,7 @@
 ))
 def test_agrees_with_two_qubit_state_tomography(circuit):
     qubits = (Q0, Q1)
-    sim = cirq.Simulator(seed=87539319)
+    sim = cirq.Simulator()
     tomography_result = cirq.experiments.state_tomography(sim,
                                                           qubits,
                                                           circuit,
