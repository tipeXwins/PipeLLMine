--- qiskit-ignis/qiskit-ignis#333/after/test_state_tomography.py	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-ignis/qiskit-ignis#333/before/test_state_tomography.py	2022-01-10 16:02:54.000000000 +0000
@@ -19,13 +19,14 @@
 import numpy
 import qiskit
 from qiskit import QuantumRegister, QuantumCircuit, Aer
-from qiskit.quantum_info import state_fidelity, Statevector
+from qiskit.quantum_info import state_fidelity
 import qiskit.ignis.verification.tomography as tomo
 import qiskit.ignis.verification.tomography.fitters.cvx_fit as cvx_fit
 
 
 def run_circuit_and_tomography(circuit, qubits):
-    psi = Statevector.from_instruction(circuit)
+    job = qiskit.execute(circuit, Aer.get_backend('statevector_simulator'))
+    psi = job.result().get_statevector(circuit)
     qst = tomo.state_tomography_circuits(circuit, qubits)
     job = qiskit.execute(qst, Aer.get_backend('qasm_simulator'),
                          shots=5000)
@@ -64,9 +65,9 @@
         bell.cx(q2[0], q2[1])
 
         rho_cvx, rho_mle, psi = run_circuit_and_tomography(bell, q2)
-        F_bell_cvx = state_fidelity(psi, rho_cvx, validate=False)
+        F_bell_cvx = state_fidelity(psi, rho_cvx)
         self.assertAlmostEqual(F_bell_cvx, 1, places=1)
-        F_bell_mle = state_fidelity(psi, rho_mle, validate=False)
+        F_bell_mle = state_fidelity(psi, rho_mle)
         self.assertAlmostEqual(F_bell_mle, 1, places=1)
 
     def test_bell_3_qubits(self):
@@ -77,9 +78,9 @@
         bell.cx(q3[1], q3[2])
 
         rho_cvx, rho_mle, psi = run_circuit_and_tomography(bell, q3)
-        F_bell_cvx = state_fidelity(psi, rho_cvx, validate=False)
+        F_bell_cvx = state_fidelity(psi, rho_cvx)
         self.assertAlmostEqual(F_bell_cvx, 1, places=1)
-        F_bell_mle = state_fidelity(psi, rho_mle, validate=False)
+        F_bell_mle = state_fidelity(psi, rho_mle)
         self.assertAlmostEqual(F_bell_mle, 1, places=1)
 
     def test_complex_1_qubit_circuit(self):
@@ -88,9 +89,9 @@
         circ.u3(1, 1, 1, q[0])
 
         rho_cvx, rho_mle, psi = run_circuit_and_tomography(circ, q)
-        F_bell_cvx = state_fidelity(psi, rho_cvx, validate=False)
+        F_bell_cvx = state_fidelity(psi, rho_cvx)
         self.assertAlmostEqual(F_bell_cvx, 1, places=1)
-        F_bell_mle = state_fidelity(psi, rho_mle, validate=False)
+        F_bell_mle = state_fidelity(psi, rho_mle)
         self.assertAlmostEqual(F_bell_mle, 1, places=1)
 
     def test_complex_3_qubit_circuit(self):
@@ -104,9 +105,9 @@
             circ.u3(*rand_angles(), q[j])
 
         rho_cvx, rho_mle, psi = run_circuit_and_tomography(circ, q)
-        F_bell_cvx = state_fidelity(psi, rho_cvx, validate=False)
+        F_bell_cvx = state_fidelity(psi, rho_cvx)
         self.assertAlmostEqual(F_bell_cvx, 1, places=1)
-        F_bell_mle = state_fidelity(psi, rho_mle, validate=False)
+        F_bell_mle = state_fidelity(psi, rho_mle)
         self.assertAlmostEqual(F_bell_mle, 1, places=1)
 
 
