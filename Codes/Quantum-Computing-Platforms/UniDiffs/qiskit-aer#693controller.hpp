--- qiskit-aer/qiskit-aer#693/after/controller.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#693/before/controller.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -44,7 +44,6 @@
 #include "framework/results/experiment_data.hpp"
 #include "noise/noise_model.hpp"
 #include "transpile/circuitopt.hpp"
-#include "transpile/basic_opts.hpp"
 #include "transpile/truncate_qubits.hpp"
 
 
@@ -629,13 +628,11 @@
   // Execute in try block so we can catch errors and return the error message
   // for individual circuit failures.
   try {
-    Transpile::ReduceBarrier barrier_pass;
-    barrier_pass.optimize_circuit(circ, noise, circ.opset(), data);
     // Truncate unused qubits from circuit and noise model
     if (truncate_qubits_) {
       Transpile::TruncateQubits truncate_pass;
       truncate_pass.set_config(config);
-      truncate_pass.optimize_circuit(circ, noise, circ.opset(), data);
+      truncate_pass.optimize_circuit(circ, noise, Operations::OpSet(), data);
     }
     // set parallelization for this circuit
     if (!explicit_parallelization_) {
