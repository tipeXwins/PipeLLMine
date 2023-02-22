--- qiskit-aer/qiskit-aer#1278/after/statevector_state_chunk.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1278/before/statevector_state_chunk.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -487,29 +487,25 @@
       return BaseState::qregs_[0].move_to_vector();
   }
   else{
-    size_t size_required = 2*(sizeof(std::complex<double>) << BaseState::num_qubits_) + (sizeof(std::complex<double>) << BaseState::chunk_bits_)*BaseState::num_local_chunks_;
-    if((size_required >> 20) > Utils::get_system_memory_mb()){
-      throw std::runtime_error(std::string("There is not enough memory to store states"));
-    }
-    else{
-      int_t iChunk;
-      auto state = BaseState::qregs_[0].move_to_vector();
-      state.resize(BaseState::num_local_chunks_ << BaseState::chunk_bits_);
+    int_t iChunk;
+    auto state = BaseState::qregs_[0].move_to_vector();
+
+    //TO DO check memory availability
+    state.resize(BaseState::num_local_chunks_ << BaseState::chunk_bits_);
 
 #pragma omp parallel for if(BaseState::chunk_omp_parallel_) private(iChunk)
-      for(iChunk=1;iChunk<BaseState::num_local_chunks_;iChunk++){
-        auto tmp = BaseState::qregs_[iChunk].move_to_vector();
-        uint_t j,offset = iChunk << BaseState::chunk_bits_;
-        for(j=0;j<tmp.size();j++){
-          state[offset + j] = tmp[j];
-        }
+    for(iChunk=1;iChunk<BaseState::num_local_chunks_;iChunk++){
+      auto tmp = BaseState::qregs_[iChunk].move_to_vector();
+      uint_t j,offset = iChunk << BaseState::chunk_bits_;
+      for(j=0;j<tmp.size();j++){
+        state[offset + j] = tmp[j];
       }
+    }
 
 #ifdef AER_MPI
-      BaseState::gather_state(state);
+    BaseState::gather_state(state);
 #endif
-      return state;
-    }
+    return state;
   }
 }
 
@@ -520,30 +516,25 @@
     return BaseState::qregs_[0].copy_to_vector();
   }
   else{
-    size_t size_required = 2*(sizeof(std::complex<double>) << BaseState::num_qubits_) + (sizeof(std::complex<double>) << BaseState::chunk_bits_)*BaseState::num_local_chunks_;
-    if((size_required >> 20) > Utils::get_system_memory_mb()){
-      throw std::runtime_error(std::string("There is not enough memory to store states"));
-    }
-    else{
-      int_t iChunk;
-      auto state = BaseState::qregs_[0].copy_to_vector();
+    int_t iChunk;
+    auto state = BaseState::qregs_[0].copy_to_vector();
 
-      state.resize(BaseState::num_local_chunks_ << BaseState::chunk_bits_);
+    //TO DO check memory availability
+    state.resize(BaseState::num_local_chunks_ << BaseState::chunk_bits_);
 
 #pragma omp parallel for if(BaseState::chunk_omp_parallel_) private(iChunk)
-      for(iChunk=1;iChunk<BaseState::num_local_chunks_;iChunk++){
-        auto tmp = BaseState::qregs_[iChunk].copy_to_vector();
-        uint_t j,offset = iChunk << BaseState::chunk_bits_;
-        for(j=0;j<tmp.size();j++){
-          state[offset + j] = tmp[j];
-        }
+    for(iChunk=1;iChunk<BaseState::num_local_chunks_;iChunk++){
+      auto tmp = BaseState::qregs_[iChunk].copy_to_vector();
+      uint_t j,offset = iChunk << BaseState::chunk_bits_;
+      for(j=0;j<tmp.size();j++){
+        state[offset + j] = tmp[j];
       }
+    }
 
 #ifdef AER_MPI
-      BaseState::gather_state(state);
+    BaseState::gather_state(state);
 #endif
-      return state;
-    }
+    return state;
   }
 }
 
