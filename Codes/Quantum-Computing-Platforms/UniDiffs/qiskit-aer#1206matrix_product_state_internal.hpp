--- qiskit-aer/qiskit-aer#1206/after/matrix_product_state_internal.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1206/before/matrix_product_state_internal.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -317,7 +317,6 @@
 			  const cmatrix_t &mat, bool is_diagonal=false);
   void apply_matrix_internal(const reg_t & qubits, const cmatrix_t &mat,
 			     bool is_diagonal=false);
-  void propagate_to_neighbors_internal(uint_t min_qubit, uint_t max_qubit);
   // apply_matrix for more than 2 qubits
   void apply_multi_qubit_gate(const reg_t &qubits,
 			      const cmatrix_t &mat,
