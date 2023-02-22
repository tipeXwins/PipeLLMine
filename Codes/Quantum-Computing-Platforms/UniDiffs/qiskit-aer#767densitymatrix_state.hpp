--- qiskit-aer/qiskit-aer#767/after/densitymatrix_state.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#767/before/densitymatrix_state.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -410,7 +410,7 @@
         apply_matrix(op.qubits, op.mats[0]);
         break;
       case Operations::OpType::diagonal_matrix:
-        BaseState::qreg_.apply_diagonal_unitary_matrix(op.qubits, op.params);
+        BaseState::qreg_.apply_diagonal_matrix(op.qubits, op.params);
         break;
 
       case Operations::OpType::superop:
