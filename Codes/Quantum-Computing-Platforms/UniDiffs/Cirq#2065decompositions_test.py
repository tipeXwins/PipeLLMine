--- Cirq/Cirq#2065/after/decompositions_test.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#2065/before/decompositions_test.py	2022-01-10 16:02:54.000000000 +0000
@@ -235,9 +235,10 @@
     cirq.testing.random_unitary(2) for _ in range(10)
 ])
 def test_single_qubit_matrix_to_native_gates_cases(intended_effect):
-    gates = cirq.single_qubit_matrix_to_phased_x_z(intended_effect, atol=1e-6)
+    gates = cirq.single_qubit_matrix_to_phased_x_z(
+        intended_effect, atol=0.0001)
     assert len(gates) <= 2
-    assert_gates_implement_unitary(gates, intended_effect, atol=1e-5)
+    assert_gates_implement_unitary(gates, intended_effect, atol=1e-8)
 
 
 @pytest.mark.parametrize('pre_turns,post_turns',
