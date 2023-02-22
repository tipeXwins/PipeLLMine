--- qiskit-aer/qiskit-aer#1188/after/matrix_product_state_internal.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1188/before/matrix_product_state_internal.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -820,7 +820,7 @@
                    const std::vector<cmatrix_t> &kmats,
                    RngEngine &rng) {
   reg_t internal_qubits = get_internal_qubits(qubits);
-  apply_kraus_internal(internal_qubits, kmats, rng);
+  apply_kraus_internal(qubits, kmats, rng);
 
 }
 void MPS::apply_kraus_internal(const reg_t &qubits,
