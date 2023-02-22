--- qiskit-aer/qiskit-aer#1132/after/matrix_product_state.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1132/before/matrix_product_state.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -973,11 +973,11 @@
   std::vector<reg_t> all_samples;
   all_samples.reserve(shots);
   for (int_t val : allbit_samples) {
-    reg_t allbit_sample = Utils::int2reg(val, 2, qubits.size());
+    reg_t allbit_sample = Utils::int2reg(val, 2, qreg_.num_qubits());
     reg_t sample;
     sample.reserve(qubits.size());
-    for (uint_t j=0; j<qubits.size(); j++){
-      sample.push_back(allbit_sample[j]);
+    for (uint_t qubit : qubits) {
+      sample.push_back(allbit_sample[qubit]);
     }
     all_samples.push_back(sample);
   }
