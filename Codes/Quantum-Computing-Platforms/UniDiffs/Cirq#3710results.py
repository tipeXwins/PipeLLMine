--- Cirq/Cirq#3710/after/results.py	2022-01-10 16:02:54.000000000 +0000
+++ Cirq/Cirq#3710/before/results.py	2022-01-10 16:02:54.000000000 +0000
@@ -252,7 +252,7 @@
                 [(value >> (self.num_qubits() - target - 1)) & 1 for target in targets]
                 for value in rand_values
             ]
-            measurements[key] = np.array(bits)
+            measurements[key] = bits
         return study.Result(params=params or study.ParamResolver({}), measurements=measurements)
 
     def __eq__(self, other):
