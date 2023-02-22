--- qiskit-aer/qiskit-aer#1278/after/aer_controller.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1278/before/aer_controller.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -312,6 +312,14 @@
   void set_parallelization_circuit_method(const Circuit &circ,
                                           const Noise::NoiseModel &noise);
 
+  // Set distributed parallelization
+  void
+  set_distributed_parallelization(const std::vector<Circuit> &circuits,
+                                  const std::vector<Noise::NoiseModel> &noise);
+
+  void set_distributed_parallelization_method(
+      const std::vector<Circuit> &circuits,
+      const std::vector<Noise::NoiseModel> &noise);
 
   bool multiple_chunk_required(const Circuit &circuit,
                                const Noise::NoiseModel &noise) const;
@@ -322,8 +330,10 @@
   size_t get_system_memory_mb();
   size_t get_gpu_memory_mb();
 
+  uint_t get_distributed_num_processes(bool par_shots) const;
+
   size_t get_min_memory_mb() const {
-    if (sim_device_ == Device::GPU && num_gpus_ > 0) {
+    if (num_gpus_ > 0) {
       return max_gpu_memory_mb_ / num_gpus_; // return per GPU memory size
     }
     return max_memory_mb_;
@@ -355,10 +365,22 @@
   // results are stored independently in each process if true
   bool accept_distributed_results_ = true;
 
+  // distributed experiments (MPI)
+  int distributed_experiments_rank_ = 0;
+  int distributed_experiments_group_id_ = 0;
+  uint_t distributed_experiments_num_processes_ = 1;
+  int distributed_experiments_ = 1;
+  uint_t num_process_per_experiment_;
+  uint_t distributed_experiments_begin_;
+  uint_t distributed_experiments_end_;
+
+  // distributed shots (MPI)
+  int distributed_shots_rank_ = 0;
+  int distributed_shots_ = 1;
+
   // process information (MPI)
   int myrank_ = 0;
   int num_processes_ = 1;
-  int num_process_per_experiment_ = 1;
 
   uint_t cache_block_qubit_ = 0;
 };
@@ -528,6 +550,8 @@
   parallel_nested_ = false;
 
   num_process_per_experiment_ = 1;
+  distributed_experiments_ = 1;
+  distributed_shots_ = 1;
 
   num_gpus_ = 0;
 
@@ -538,38 +562,44 @@
 
 void Controller::set_parallelization_experiments(
     const std::vector<Circuit> &circuits,
-    const std::vector<Noise::NoiseModel> &noise) 
-{
-  if(circuits.size() == 1){
-    parallel_experiments_ = 1;
-    return;
-  }
-
+    const std::vector<Noise::NoiseModel> &noise) {
   // Use a local variable to not override stored maximum based
   // on currently executed circuits
   const auto max_experiments =
-      (max_parallel_experiments_ > 1)
+      (max_parallel_experiments_ > 0)
           ? std::min({max_parallel_experiments_, max_parallel_threads_})
           : max_parallel_threads_;
 
-  if (max_experiments == 1) {
+  if (max_experiments == 1 && num_processes_ == 1) {
     // No parallel experiment execution
     parallel_experiments_ = 1;
     return;
   }
 
   // If memory allows, execute experiments in parallel
+#ifdef AER_MPI
+  std::vector<size_t> required_memory_mb_list(distributed_experiments_end_ -
+                                              distributed_experiments_begin_);
+  for (size_t j = 0;
+       j < distributed_experiments_end_ - distributed_experiments_begin_; j++) {
+    required_memory_mb_list[j] =
+        required_memory_mb(circuits[j + distributed_experiments_begin_],
+                           noise[j + distributed_experiments_begin_]) /
+        num_process_per_experiment_;
+  }
+#else
   std::vector<size_t> required_memory_mb_list(circuits.size());
   for (size_t j = 0; j < circuits.size(); j++) {
     required_memory_mb_list[j] = required_memory_mb(circuits[j], noise[j]);
   }
+#endif
   std::sort(required_memory_mb_list.begin(), required_memory_mb_list.end(),
             std::greater<>());
   size_t total_memory = 0;
   parallel_experiments_ = 0;
   for (size_t required_memory_mb : required_memory_mb_list) {
     total_memory += required_memory_mb;
-    if (total_memory > max_memory_mb_)
+    if (total_memory > max_memory_mb_ * num_process_per_experiment_)
       break;
     ++parallel_experiments_;
   }
@@ -577,14 +607,21 @@
   if (parallel_experiments_ <= 0)
     throw std::runtime_error(
         "a circuit requires more memory than max_memory_mb.");
+#ifdef AER_MPI
+  parallel_experiments_ = std::min<int>(
+      {parallel_experiments_, max_experiments, max_parallel_threads_,
+       static_cast<int>(distributed_experiments_end_ -
+                        distributed_experiments_begin_)});
+#else
   parallel_experiments_ =
       std::min<int>({parallel_experiments_, max_experiments,
                      max_parallel_threads_, static_cast<int>(circuits.size())});
+#endif
 }
 
 void Controller::set_parallelization_circuit(const Circuit &circ,
-                                             const Noise::NoiseModel &noise) 
-{
+                                             const Noise::NoiseModel &noise) {
+
   // Use a local variable to not override stored maximum based
   // on currently executed circuits
   const auto max_shots =
@@ -602,14 +639,19 @@
     // And assign the remaining threads to state update
     int circ_memory_mb =
         required_memory_mb(circ, noise) / num_process_per_experiment_;
-    size_t mem_size = (sim_device_ == Device::GPU) ? max_memory_mb_ + max_gpu_memory_mb_ : max_memory_mb_;
-    if (mem_size < circ_memory_mb)
+    if (max_memory_mb_ + max_gpu_memory_mb_ < circ_memory_mb)
       throw std::runtime_error(
           "a circuit requires more memory than max_memory_mb.");
     // If circ memory is 0, set it to 1 so that we don't divide by zero
     circ_memory_mb = std::max<int>({1, circ_memory_mb});
 
+#ifdef AER_MPI
+    int shots =
+        (circ.shots * (distributed_shots_rank_ + 1) / distributed_shots_) -
+        (circ.shots * distributed_shots_rank_ / distributed_shots_);
+#else
     int shots = circ.shots;
+#endif
     parallel_shots_ = std::min<int>(
         {static_cast<int>(max_memory_mb_ / circ_memory_mb), max_shots, shots});
   }
@@ -619,31 +661,116 @@
           : std::max<int>({1, max_parallel_threads_ / parallel_experiments_});
 }
 
+void Controller::set_distributed_parallelization(
+    const std::vector<Circuit> &circuits,
+    const std::vector<Noise::NoiseModel> &noise) {
+  std::vector<size_t> required_memory_mb_list(circuits.size());
+  num_process_per_experiment_ = 1;
+  for (size_t j = 0; j < circuits.size(); j++) {
+    size_t size = required_memory_mb(circuits[j], noise[j]);
+    if (size > max_memory_mb_ + max_gpu_memory_mb_) {
+      num_process_per_experiment_ =
+          std::max<int>(num_process_per_experiment_,
+                        (size + (max_memory_mb_ + max_gpu_memory_mb_) - 1) /
+                            (max_memory_mb_ + max_gpu_memory_mb_));
+    }
+  }
+  while ((num_processes_ % num_process_per_experiment_) != 0) {
+    num_process_per_experiment_++;
+  }
+
+  distributed_experiments_ = num_processes_ / num_process_per_experiment_;
+
+  if (circuits.size() < distributed_experiments_) {
+    // e.g. np = 8, circuits = 3, npe = 2,  de = 4 -> 3 , then np_in_group =
+    // [3,3,2]
+    //      np = 4, circuits = 1, npe = 2,  de = 2 -> 1 , then np_in_group = [4]
+    distributed_experiments_ = circuits.size();
+
+    distributed_experiments_num_processes_ =
+        (num_processes_ + distributed_experiments_ - 1) /
+        distributed_experiments_;
+    distributed_experiments_group_id_ =
+        myrank_ / distributed_experiments_num_processes_;
+    if ((distributed_experiments_group_id_ + 1) *
+            distributed_experiments_num_processes_ >
+        num_processes_) {
+      distributed_experiments_num_processes_ =
+          num_processes_ - distributed_experiments_group_id_ *
+                               distributed_experiments_num_processes_;
+    }
+
+    if (distributed_experiments_num_processes_ > num_process_per_experiment_ &&
+        (distributed_experiments_num_processes_ %
+         num_process_per_experiment_) == 0) {
+      distributed_shots_ =
+          distributed_experiments_num_processes_ / num_process_per_experiment_;
+      distributed_shots_rank_ = 0;
+    } else {
+      // shots are not distributed
+      distributed_shots_ = 1;
+      distributed_shots_rank_ = 0;
+    }
+    distributed_experiments_rank_ = myrank_ % distributed_experiments_;
+
+    distributed_experiments_begin_ = distributed_experiments_group_id_;
+    distributed_experiments_end_ = distributed_experiments_begin_ + 1;
+  } else {
+    distributed_experiments_group_id_ = myrank_ / num_process_per_experiment_;
+    distributed_experiments_rank_ = myrank_ % num_process_per_experiment_;
+    distributed_experiments_num_processes_ = num_process_per_experiment_;
+
+    distributed_experiments_begin_ = circuits.size() *
+                                     distributed_experiments_group_id_ /
+                                     distributed_experiments_;
+    distributed_experiments_end_ = circuits.size() *
+                                   (distributed_experiments_group_id_ + 1) /
+                                   distributed_experiments_;
+
+    // shots are not distributed
+    distributed_shots_ = 1;
+    distributed_shots_rank_ = 0;
+  }
+}
+
+uint_t Controller::get_distributed_num_processes(bool par_shots) const {
+  if (par_shots) {
+    return num_process_per_experiment_;
+  } else {
+    return distributed_experiments_num_processes_; // no shot distribution,
+                                                   // parallelize this
+                                                   // experiment by processes in
+                                                   // group
+  }
+}
+
 bool Controller::multiple_chunk_required(const Circuit &circ,
-                                         const Noise::NoiseModel &noise) const 
-{
+                                         const Noise::NoiseModel &noise) const {
   if (circ.num_qubits < 3)
     return false;
-  if (cache_block_qubit_ >= 2 && cache_block_qubit_ < circ.num_qubits)
+
+  if (num_process_per_experiment_ > 1 ||
+      Controller::get_min_memory_mb() < required_memory_mb(circ, noise))
     return true;
 
-  if(num_process_per_experiment_ == 1 && sim_device_ == Device::GPU && num_gpus_ > 0){
-    return (max_gpu_memory_mb_ / num_gpus_ < required_memory_mb(circ, noise));
-  }
-  if(num_process_per_experiment_ > 1){
-    size_t total_mem = max_memory_mb_;
-    if(sim_device_ == Device::GPU)
-      total_mem += max_gpu_memory_mb_;
-    if(total_mem*num_process_per_experiment_ > required_memory_mb(circ, noise))
-      return true;
-  }
+  if (cache_block_qubit_ >= 2 && cache_block_qubit_ < circ.num_qubits)
+    return true;
 
   return false;
 }
 
-size_t Controller::get_system_memory_mb() 
-{
-  size_t total_physical_memory = Utils::get_system_memory_mb();
+size_t Controller::get_system_memory_mb() {
+  size_t total_physical_memory = 0;
+#if defined(__linux__) || defined(__APPLE__)
+  auto pages = sysconf(_SC_PHYS_PAGES);
+  auto page_size = sysconf(_SC_PAGE_SIZE);
+  total_physical_memory = pages * page_size;
+#elif defined(_WIN64) || defined(_WIN32)
+  MEMORYSTATUSEX status;
+  status.dwLength = sizeof(status);
+  GlobalMemoryStatusEx(&status);
+  total_physical_memory = status.ullTotalPhys;
+#endif
 #ifdef AER_MPI
   // get minimum memory size per process
   uint64_t locMem, minMem;
@@ -652,7 +779,7 @@
   total_physical_memory = minMem;
 #endif
 
-  return total_physical_memory;
+  return total_physical_memory >> 20;
 }
 
 size_t Controller::get_gpu_memory_mb() {
@@ -730,9 +857,7 @@
 
   size_t required_mb = state.required_memory_mb(circ.num_qubits, circ.ops) /
                        num_process_per_experiment_;
-                                                
-  size_t mem_size = (sim_device_ == Device::GPU) ? max_memory_mb_ + max_gpu_memory_mb_ : max_memory_mb_;
-  if (mem_size < required_mb) {
+  if (max_memory_mb_ + max_gpu_memory_mb_ < required_mb) {
     if (throw_except) {
       std::string name = "";
       JSON::get_value(name, "name", circ.header);
@@ -771,7 +896,7 @@
     // if blocking is not set by config, automatically set if required
     if (multiple_chunk_required(circ, noise)) {
       int nplace = num_process_per_experiment_;
-      if(sim_device_ == Device::GPU && num_gpus_ > 0)
+      if (num_gpus_ > 0)
         nplace *= num_gpus_;
       cache_block_pass.set_blocking(circ.num_qubits, get_min_memory_mb() << 20,
                                     nplace, complex_size, is_matrix);
@@ -859,14 +984,32 @@
       }
     }
 
+#ifdef AER_MPI
+    try {
+      // catch exception raised by required_memory_mb because of invalid
+      // simulation method
+      set_distributed_parallelization_method(circuits, circ_noise_models);
+    } catch (std::exception &e) {
+      save_exception_to_results(result, e);
+    }
+
+    const auto num_circuits =
+        distributed_experiments_end_ - distributed_experiments_begin_;
+    result.resize(num_circuits);
+#endif
+
     // get max qubits for this process (to allocate qubit register at once)
     max_qubits_ = 0;
+#ifdef AER_MPI
+    for (size_t j = distributed_experiments_begin_;
+         j < distributed_experiments_end_; j++) {
+#else
     for (size_t j = 0; j < circuits.size(); j++) {
+#endif
       if (circuits[j].num_qubits > max_qubits_) {
         max_qubits_ = circuits[j].num_qubits;
       }
     }
-    num_process_per_experiment_ = num_processes_;
 
     if (!explicit_parallelization_) {
       // set parallelization for experiments
@@ -892,6 +1035,13 @@
     // set
     result.metadata.add(num_processes_, "num_mpi_processes");
     result.metadata.add(myrank_, "mpi_rank");
+#ifdef AER_MPI
+    result.metadata.add(distributed_experiments_, "distributed_experiments");
+    result.metadata.add(distributed_experiments_group_id_,
+                        "distributed_experiments_group_id");
+    result.metadata.add(distributed_experiments_rank_,
+                        "distributed_experiments_rank_in_group");
+#endif
 
 #ifdef _OPENMP
     // Check if circuit parallelism is nested with one of the others
@@ -914,6 +1064,10 @@
 #endif
     }
 #endif
+    uint_t offset = 0;
+#ifdef AER_MPI
+    offset = distributed_experiments_begin_;
+#endif
     // then- and else-blocks have intentionally duplication.
     // Nested omp has significant overheads even though a guard condition
     // exists.
@@ -921,12 +1075,12 @@
     if (parallel_experiments_ > 1) {
 #pragma omp parallel for num_threads(parallel_experiments_)
       for (int j = 0; j < result.results.size(); ++j) {
-        execute_circuit(circuits[j], circ_noise_models[j],
+        execute_circuit(circuits[j + offset], circ_noise_models[j + offset],
                         config, result.results[j]);
       }
     } else {
       for (int j = 0; j < result.results.size(); ++j) {
-        execute_circuit(circuits[j], circ_noise_models[j],
+        execute_circuit(circuits[j + offset], circ_noise_models[j + offset],
                         config, result.results[j]);
       }
     }
@@ -993,6 +1147,14 @@
     }
 
     int shots = circ.shots;
+#ifdef AER_MPI
+    if (parallel_shots_ > 1 &&
+        distributed_shots_ > 1) { // if shots can be distributed
+      shots =
+          (circ.shots * (distributed_shots_rank_ + 1) / distributed_shots_) -
+          (circ.shots * distributed_shots_rank_ / distributed_shots_);
+    }
+#endif
 
     // Single shot thread execution
     if (parallel_shots_ <= 1) {
@@ -1062,6 +1224,11 @@
     result.seed = circ.seed;
     result.metadata.add(parallel_shots_, "parallel_shots");
     result.metadata.add(parallel_state_update_, "parallel_state_update");
+#ifdef AER_MPI
+    if (parallel_shots_ > 1 && distributed_shots_ > 1) {
+      result.metadata.add(distributed_shots_, "distributed_shots");
+    }
+#endif
     // Add timer data
     auto timer_stop = myclock_t::now(); // stop timer
     double time_taken =
@@ -1651,6 +1818,55 @@
   }
 }
 
+void Controller::set_distributed_parallelization_method(
+    const std::vector<Circuit> &circuits,
+    const std::vector<Noise::NoiseModel> &noise) {
+#ifdef AER_MPI
+  uint_t i, ncircuits;
+  bool sample_opt = true;
+
+  ncircuits = circuits.size();
+  for (i = 0; i < ncircuits; i++) {
+    const auto method = simulation_method(circuits[i], noise[i], false);
+    switch (method) {
+    case Method::statevector:
+    case Method::stabilizer:
+    case Method::unitary:
+    case Method::matrix_product_state: {
+      if (circuits[i].shots > 1 &&
+          (noise[i].has_quantum_errors() ||
+           !check_measure_sampling_opt(circuits[i], method))) {
+        sample_opt = false;
+      }
+      break;
+    }
+    case Method::density_matrix:
+    case Method::superop: {
+      if (circuits[i].shots > 1 &&
+          !check_measure_sampling_opt(circuits[i], method)) {
+        sample_opt = false;
+      }
+      break;
+    }
+    default: {
+      sample_opt = false;
+    }
+    }
+    if (!sample_opt) {
+      break;
+    }
+  }
+
+  if (sample_opt) {
+    set_distributed_parallelization(circuits, noise);
+
+    // shots are not distributed
+    distributed_shots_ = 1;
+    distributed_shots_rank_ = 0;
+  }
+#endif
+}
+
 //-------------------------------------------------------------------------
 // Run circuit helpers
 //-------------------------------------------------------------------------
@@ -1671,7 +1887,7 @@
   // Set state config
   state.set_config(config);
   state.set_parallalization(parallel_state_update_);
-  state.set_distribution(num_processes_);
+  state.set_distribution(get_distributed_num_processes(shots == circ.shots));
   state.set_global_phase(circ.global_phase_angle);
 
   // Rng engine
