--- tequila/tequila#119/after/simulator_qibo.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#119/before/simulator_qibo.py	2022-01-10 16:02:54.000000000 +0000
@@ -430,7 +430,7 @@
         # todo there are faster ways
 
         for k, v in backend_result.frequencies(binary=True).items():
-            converted_key = BitString.from_bitstring(other=BitString.from_binary(binary=k))
+            converted_key = BitString.from_bitstring(other=BitStringLSB.from_binary(binary=k))
             result._state[converted_key] = v
 
 
@@ -678,7 +678,6 @@
         -------
         None
         """
-        target_qubits = sorted(target_qubits)
         added=[]
         for t in target_qubits:
             circuit.add(gates.M(t))
@@ -737,3 +736,4 @@
 
 class BackendExpectationValueQibo(BackendExpectationValue):
     BackendCircuitType = BackendCircuitQibo
+
