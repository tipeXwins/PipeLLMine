--- amazon-braket-sdk-python/amazon-braket-sdk-python#192/after/test_tensor_network_simulator.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#192/before/test_tensor_network_simulator.py	2022-01-10 16:02:54.000000000 +0000
@@ -41,7 +41,7 @@
 @pytest.mark.parametrize("simulator_arn", SIMULATOR_ARNS)
 def test_qft_iqft_h(simulator_arn, aws_session, s3_destination_folder):
     num_qubits = 24
-    h_qubit = random.randint(0, num_qubits - 1)
+    h_qubit = random.randint(0, num_qubits)
     circuit = _inverse_qft(_qft(Circuit().h(h_qubit), num_qubits), num_qubits)
     device = AwsDevice(simulator_arn, aws_session)
     no_result_types_testing(
