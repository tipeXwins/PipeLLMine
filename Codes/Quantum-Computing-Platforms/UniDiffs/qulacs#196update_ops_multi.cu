--- qulacs/qulacs#196/after/update_ops_multi.cu	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#196/before/update_ops_multi.cu	2022-01-10 16:02:54.000000000 +0000
@@ -986,7 +986,7 @@
         if(target_qubit_index_count<=5){
 		    checkCudaErrors(cudaMemcpyToSymbolAsync(matrix_const_gpu, matrix, sizeof(GTYPE)*matrix_dim*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
 		    checkCudaErrors(cudaMemcpyToSymbolAsync(matrix_mask_list_gpu, matrix_mask_list, sizeof(ITYPE)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
-		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*(target_qubit_index_count + 1), 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
+		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
 
             single_qubit_control_multi_qubit_dense_matrix_gate_const_gpu<<< grid, block, 0, *cuda_stream >>> (control_qubit_index, control_value, target_qubit_index_count, state_gpu, dim);
         }else{
@@ -994,7 +994,7 @@
 		    checkCudaErrors(cudaMemcpyAsync(d_matrix, matrix, matrix_dim *matrix_dim * sizeof(GTYPE), cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
 		    checkCudaErrors(cudaMalloc(reinterpret_cast<void **>(&d_matrix_mask_list), matrix_dim *matrix_dim * sizeof(GTYPE) ), __FILE__, __LINE__);
 		    checkCudaErrors(cudaMemcpyAsync(d_matrix_mask_list, matrix_mask_list, sizeof(ITYPE)*matrix_dim, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
-		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*(target_qubit_index_count + 1), 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
+		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
 		    
             single_qubit_control_multi_qubit_dense_matrix_gate_const_gpu<<< grid, block, 0, *cuda_stream >>> (control_qubit_index, control_value, target_qubit_index_count, d_matrix, state_gpu, dim);
         }
@@ -1135,7 +1135,7 @@
         if(target_qubit_index_count<=5){
 		    checkCudaErrors(cudaMemcpyToSymbolAsync(matrix_const_gpu, matrix, sizeof(GTYPE)*matrix_dim*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
 		    checkCudaErrors(cudaMemcpyToSymbolAsync(matrix_mask_list_gpu, matrix_mask_list, sizeof(ITYPE)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
-		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*(target_qubit_index_count+control_qubit_index_count), 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
+		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
 
             multi_qubit_control_multi_qubit_dense_matrix_gate_const_gpu<<< grid, block, 0, *cuda_stream >>> (control_mask, target_qubit_index_count, control_qubit_index_count, state_gpu, dim);
         }else{
@@ -1143,7 +1143,7 @@
 		    checkCudaErrors(cudaMemcpyAsync(d_matrix, matrix, matrix_dim *matrix_dim * sizeof(GTYPE), cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
 		    checkCudaErrors(cudaMalloc(reinterpret_cast<void **>(&d_matrix_mask_list), matrix_dim *matrix_dim * sizeof(GTYPE) ), __FILE__, __LINE__);
 		    checkCudaErrors(cudaMemcpyAsync(d_matrix_mask_list, matrix_mask_list, sizeof(ITYPE)*matrix_dim, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
-		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*(target_qubit_index_count + control_qubit_index_count), 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
+		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
 		    
             multi_qubit_control_multi_qubit_dense_matrix_gate_const_gpu<<< grid, block, 0, *cuda_stream >>> (control_mask, target_qubit_index_count, control_qubit_index_count, d_matrix, state_gpu, dim);
         }
