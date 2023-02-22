--- qiskit-aer/qiskit-aer#1278/after/state_chunk.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1278/before/state_chunk.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -745,10 +745,6 @@
   uint_t mask = (1ull << (chunk_bits_)) - 1;
   uint_t num_threads = qregs_[0].get_omp_threads();
 
-  size_t size_required = 2*(sizeof(std::complex<double>) << (num_qubits_*2)) + (sizeof(std::complex<double>) << (chunk_bits_*2))*num_local_chunks_;
-  if((size_required>>20) > Utils::get_system_memory_mb()){
-    throw std::runtime_error(std::string("There is not enough memory to store states as matrix"));
-  }
   auto matrix = qregs_[0].copy_to_matrix();
 
   if(distributed_rank_ == 0){
@@ -1482,9 +1478,6 @@
     MPI_Allreduce(&local_size,&global_size,1,MPI_UINT64_T,MPI_SUM,distributed_comm_);
 
     if(distributed_rank_ == 0){
-      if((global_size >> 21) > Utils::get_system_memory_mb()){
-        throw std::runtime_error(std::string("There is not enough memory to gather state"));
-      }
       state.resize(global_size);
 
       offset = 0;
@@ -1521,9 +1514,6 @@
     MPI_Allreduce(&local_size,&global_size,1,MPI_UINT64_T,MPI_SUM,distributed_comm_);
 
     if(distributed_rank_ == 0){
-      if((global_size >> 21) > Utils::get_system_memory_mb()){
-        throw std::runtime_error(std::string("There is not enough memory to gather state"));
-      }
       state.resize(global_size);
 
       offset = 0;
