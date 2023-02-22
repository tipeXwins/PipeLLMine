--- qiskit-aer/qiskit-aer#1206/after/matrix_product_state_internal.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1206/before/matrix_product_state_internal.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -866,14 +866,7 @@
     double renorm = 1 / std::sqrt(1. - accum);
     cmatrix_t temp_mat = kmats.back()* renorm;
     apply_matrix_internal(qubits, temp_mat);
-  }  
-  uint_t min_qubit = qubits[0];
-  uint_t max_qubit = qubits[0];
-  for (uint_t i=qubits[0]; i<qubits.size(); i++) {
-    min_qubit = std::min(min_qubit, qubits[i]);
-    max_qubit = std::max(max_qubit, qubits[i]);
   }
-  propagate_to_neighbors_internal(min_qubit, max_qubit);
 }
 
 void MPS::centralize_qubits(const reg_t &qubits, 
@@ -1498,24 +1491,21 @@
     measurement_matrix = measurement_matrix * (1 / sqrt(prob1));
   }
   apply_matrix_internal(qubits_to_update, measurement_matrix);
-  propagate_to_neighbors_internal(qubit, qubit);
-  return measurement;
-}
 
-void MPS::propagate_to_neighbors_internal(uint_t min_qubit, uint_t max_qubit) {
   // step 4 - propagate the changes to all qubits to the right
-  for (uint_t i=max_qubit; i<num_qubits_-1; i++) {
+  for (uint_t i=qubit; i<num_qubits_-1; i++) {
     if (lambda_reg_[i].size() == 1) 
       break;   // no need to propagate if no entanglement
     apply_2_qubit_gate(i, i+1, id, cmatrix_t(1, 1));
   }
 
   // and propagate the changes to all qubits to the left
-  for (int_t i=min_qubit; i>0; i--) {
+  for (int_t i=qubit; i>0; i--) {
     if (lambda_reg_[i-1].size() == 1) 
       break;   // no need to propagate if no entanglement
     apply_2_qubit_gate(i-1, i, id, cmatrix_t(1, 1));
   }
+  return measurement;
 }
 
 void MPS::apply_initialize(const reg_t &qubits, 
