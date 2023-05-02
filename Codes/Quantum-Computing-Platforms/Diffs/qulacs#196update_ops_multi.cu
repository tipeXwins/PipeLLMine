989c989
< 		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*(target_qubit_index_count + 1), 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
---
> 		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
997c997
< 		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*(target_qubit_index_count + 1), 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
---
> 		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
1138c1138
< 		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*(target_qubit_index_count+control_qubit_index_count), 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
---
> 		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
1146c1146
< 		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*(target_qubit_index_count + control_qubit_index_count), 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
---
> 		    checkCudaErrors(cudaMemcpyToSymbolAsync(sorted_insert_index_list_gpu, sorted_insert_index_list, sizeof(UINT)*matrix_dim, 0, cudaMemcpyHostToDevice, *cuda_stream), __FILE__, __LINE__);
