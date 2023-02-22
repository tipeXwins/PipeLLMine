--- qiskit-aer/qiskit-aer#1278/after/densitymatrix_state_chunk.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1278/before/densitymatrix_state_chunk.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -995,10 +995,7 @@
   uint_t mask = (1ull << (BaseState::chunk_bits_)) - 1;
   uint_t num_threads = BaseState::qregs_[0].get_omp_threads();
 
-  size_t size_required = (sizeof(std::complex<double>) << (qubits.size()*2)) + (sizeof(std::complex<double>) << (BaseState::chunk_bits_*2))*BaseState::num_local_chunks_;
-  if((size_required>>20) > Utils::get_system_memory_mb()){
-    throw std::runtime_error(std::string("There is not enough memory to store density matrix"));
-  }
+  //TO DO check memory availability
   cmatrix_t reduced_state(1ull << qubits.size(),1ull << qubits.size(),true);
 
   if(BaseState::distributed_rank_ == 0){
