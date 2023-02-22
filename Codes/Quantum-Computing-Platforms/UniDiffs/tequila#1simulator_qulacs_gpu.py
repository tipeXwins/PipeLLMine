--- tequila/tequila#1/after/simulator_qulacs_gpu.py	2022-01-10 16:02:54.000000000 +0000
+++ tequila/tequila#1/before/simulator_qulacs_gpu.py	2022-01-10 16:02:54.000000000 +0000
@@ -1,13 +0,0 @@
-import qulacs
-from tequila import TequilaException
-from tequila.simulators.simulator_qulacs import BackendCircuitQulacs, BackendExpectationValueQulacs
-class TequilaQulacsGpuException(TequilaException):
-    def __str__(self):
-        return "Error in qulacs qpu backend:" + self.message
-class BackendCircuitQulacsGpu(BackendCircuitQulacs):
-    def initialize_state(self, n_qubits = None):
-        if n_qubits is None:
-            n_qubits = self.n_qubits
-        return qulacs.QuantumStateGpu(n_qubits)
-class BackendExpectationValueQulacsGpu(BackendExpectationValueQulacs):
-    pass
