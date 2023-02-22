--- qiskit-aer/qiskit-aer#693/after/qasm_controller.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#693/before/qasm_controller.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -22,6 +22,7 @@
 #include "simulators/stabilizer/stabilizer_state.hpp"
 #include "simulators/statevector/statevector_state.hpp"
 #include "simulators/superoperator/superoperator_state.hpp"
+#include "transpile/basic_opts.hpp"
 #include "transpile/delay_measure.hpp"
 #include "transpile/fusion.hpp"
 
@@ -273,6 +274,7 @@
 // Constructor
 //-------------------------------------------------------------------------
 QasmController::QasmController() {
+  add_circuit_optimization(Transpile::ReduceBarrier());
   add_circuit_optimization(Transpile::DelayMeasure());
   add_circuit_optimization(Transpile::Fusion());
 }
