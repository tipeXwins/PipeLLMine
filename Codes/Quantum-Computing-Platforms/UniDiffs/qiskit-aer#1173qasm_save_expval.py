--- qiskit-aer/qiskit-aer#1173/after/qasm_save_expval.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1173/before/qasm_save_expval.py	2022-01-10 16:02:54.000000000 +0000
@@ -46,9 +46,9 @@
 
         # Stabilizer test circuit
         state_circ = qi.random_clifford(2, seed=SEED).to_circuit()
-        oper = qi.Operator(qi.Pauli(pauli))
+        oper = qi.Pauli(pauli)
         state = qi.Statevector(state_circ)
-        target = state.expectation_value(oper).real
+        target = state.expectation_value(oper).real.round(10)
 
         # Snapshot circuit
         opts = self.BACKEND_OPTS.copy()
@@ -78,7 +78,7 @@
 
         # Stabilizer test circuit
         state_circ = qi.random_clifford(2, seed=SEED).to_circuit()
-        oper = qi.Operator(qi.Pauli(pauli))
+        oper = qi.Pauli(pauli)
         state = qi.Statevector(state_circ)
         expval = state.expectation_value(oper).real
         variance = state.expectation_value(oper ** 2).real - expval ** 2
@@ -178,9 +178,9 @@
 
         # Stabilizer test circuit
         state_circ = QuantumVolume(2, 1, seed=SEED)
-        oper = qi.Operator(qi.Pauli(pauli))
+        oper = qi.Pauli(pauli)
         state = qi.Statevector(state_circ)
-        target = state.expectation_value(oper).real
+        target = state.expectation_value(oper).real.round(10)
 
         # Snapshot circuit
         opts = self.BACKEND_OPTS.copy()
@@ -209,7 +209,7 @@
 
         # Stabilizer test circuit
         state_circ = QuantumVolume(2, 1, seed=SEED)
-        oper = qi.Operator(qi.Pauli(pauli))
+        oper = qi.Pauli(pauli)
         state = qi.Statevector(state_circ)
         expval = state.expectation_value(oper).real
         variance = state.expectation_value(oper ** 2).real - expval ** 2
@@ -244,7 +244,7 @@
         state_circ = QuantumVolume(3, 1, seed=SEED)
         oper = qi.random_hermitian(4, traceless=True, seed=SEED)
         state = qi.Statevector(state_circ)
-        target = state.expectation_value(oper, qubits).real
+        target = state.expectation_value(oper, qubits).real.round(10)
 
         # Snapshot circuit
         opts = self.BACKEND_OPTS.copy()
@@ -305,7 +305,7 @@
         opts = self.BACKEND_OPTS.copy()
         if opts.get('method') in SUPPORTED_METHODS:
 
-            oper = qi.Operator(qi.Pauli(pauli))
+            oper = qi.Pauli(pauli)
 
             # CPTP channel test circuit
             channel = qi.random_quantum_channel(4, seed=SEED)
@@ -313,7 +313,7 @@
             state_circ.append(channel, range(2))
 
             state = qi.DensityMatrix(state_circ)
-            target = state.expectation_value(oper).real
+            target = state.expectation_value(oper).real.round(10)
 
             # Snapshot circuit
             circ = transpile(state_circ, self.SIMULATOR)
@@ -337,7 +337,7 @@
         opts = self.BACKEND_OPTS.copy()
         if opts.get('method') in SUPPORTED_METHODS:
 
-            oper = qi.Operator(qi.Operator(qi.Pauli(pauli)))
+            oper = qi.Pauli(pauli)
 
             # CPTP channel test circuit
             channel = qi.random_quantum_channel(4, seed=SEED)
