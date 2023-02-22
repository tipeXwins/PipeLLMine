--- qiskit-aer/qiskit-aer#1294/after/fusion.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1294/before/fusion.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -658,10 +658,8 @@
       continue;
 
     std::vector<uint_t> fusing_op_idxs;
-    while(op_idx < next_diagonal_start && op_idx < fusion_end) {
+    for (; op_idx < next_diagonal_start; ++op_idx)
       fusing_op_idxs.push_back(op_idx);
-      ++op_idx;
-    }
 
     --op_idx;
     allocate_new_operation(ops, op_idx, fusing_op_idxs, method, true);
