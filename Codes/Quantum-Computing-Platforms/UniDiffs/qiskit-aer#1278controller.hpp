--- qiskit-aer/qiskit-aer#1278/after/controller.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1278/before/controller.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -213,6 +213,11 @@
   virtual size_t required_memory_mb(const Circuit &circuit,
                                     const Noise::NoiseModel &noise) const = 0;
 
+  // Set distributed parallelization
+  virtual void
+  set_distributed_parallelization(const std::vector<Circuit> &circuits,
+                                  const std::vector<Noise::NoiseModel> &noise);
+
   virtual bool multiple_chunk_required(const Circuit &circuit,
                                   const Noise::NoiseModel &noise) const;
 
@@ -230,6 +235,8 @@
   size_t get_system_memory_mb();
   size_t get_gpu_memory_mb();
 
+  uint_t get_distributed_num_processes(bool par_shots) const;
+
   size_t get_min_memory_mb() const
   {
     if(num_gpus_ > 0){
@@ -264,7 +271,18 @@
   //results are stored independently in each process if true
   bool accept_distributed_results_ = true;
 
+  //distributed experiments (MPI)
+  int distributed_experiments_rank_ = 0;
+  int distributed_experiments_group_id_ = 0;
+  uint_t distributed_experiments_num_processes_ = 1;
+  int distributed_experiments_ = 1;
   uint_t num_process_per_experiment_;
+  uint_t distributed_experiments_begin_;
+  uint_t distributed_experiments_end_;
+
+  //distributed shots (MPI)
+  int distributed_shots_rank_ = 0;
+  int distributed_shots_ = 1;
 
   //process information (MPI)
   int myrank_ = 0;
@@ -382,6 +400,8 @@
   parallel_nested_ = false;
 
   num_process_per_experiment_ = 1;
+  distributed_experiments_ = 1;
+  distributed_shots_ = 1;
 
   num_gpus_ = 0;
 
@@ -407,10 +427,17 @@
   }
 
   // If memory allows, execute experiments in parallel
+#ifdef AER_MPI
+  std::vector<size_t> required_memory_mb_list(distributed_experiments_end_ - distributed_experiments_begin_);
+  for (size_t j = 0; j < distributed_experiments_end_-distributed_experiments_begin_; j++) {
+    required_memory_mb_list[j] = required_memory_mb(circuits[j+distributed_experiments_begin_], noise[j+distributed_experiments_begin_]) / num_process_per_experiment_;
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
@@ -425,9 +452,15 @@
   if (parallel_experiments_ <= 0)
     throw std::runtime_error(
         "a circuit requires more memory than max_memory_mb.");
+#ifdef AER_MPI
+  parallel_experiments_ =
+      std::min<int>({parallel_experiments_, max_experiments,
+                     max_parallel_threads_, static_cast<int>(distributed_experiments_end_ - distributed_experiments_begin_)});
+#else
   parallel_experiments_ =
       std::min<int>({parallel_experiments_, max_experiments,
                      max_parallel_threads_, static_cast<int>(circuits.size())});
+#endif
 }
 
 void Controller::set_parallelization_circuit(const Circuit &circ,
@@ -455,7 +488,11 @@
     // If circ memory is 0, set it to 1 so that we don't divide by zero
     circ_memory_mb = std::max<int>({1, circ_memory_mb});
 
+#ifdef AER_MPI
+    int shots = (circ.shots * (distributed_shots_rank_ + 1)/distributed_shots_) - (circ.shots * distributed_shots_rank_ /distributed_shots_);
+#else
     int shots = circ.shots;
+#endif
     parallel_shots_ =
         std::min<int>({static_cast<int>(max_memory_mb_ / circ_memory_mb),
                        max_shots, shots});
@@ -466,6 +503,72 @@
           : std::max<int>({1, max_parallel_threads_ / parallel_experiments_});
 }
 
+void Controller::set_distributed_parallelization(const std::vector<Circuit> &circuits,
+                                  const std::vector<Noise::NoiseModel> &noise)
+{
+  std::vector<size_t> required_memory_mb_list(circuits.size());
+  num_process_per_experiment_ = 1;
+  for (size_t j = 0; j < circuits.size(); j++) {
+    size_t size = required_memory_mb(circuits[j], noise[j]);
+    if(size > max_memory_mb_ + max_gpu_memory_mb_){
+      num_process_per_experiment_ = std::max<int>(num_process_per_experiment_,(size + (max_memory_mb_+max_gpu_memory_mb_) - 1) / (max_memory_mb_+max_gpu_memory_mb_));
+    }
+  }
+  while((num_processes_ % num_process_per_experiment_) != 0){
+    num_process_per_experiment_++;
+  }
+
+  distributed_experiments_ = num_processes_ / num_process_per_experiment_;
+
+  if(circuits.size() < distributed_experiments_){
+    // e.g. np = 8, circuits = 3, npe = 2,  de = 4 -> 3 , then np_in_group = [3,3,2]
+    //      np = 4, circuits = 1, npe = 2,  de = 2 -> 1 , then np_in_group = [4]
+    distributed_experiments_ = circuits.size();
+
+    distributed_experiments_num_processes_ = (num_processes_ + distributed_experiments_ - 1)/distributed_experiments_;
+    distributed_experiments_group_id_ = myrank_ / distributed_experiments_num_processes_;
+    if((distributed_experiments_group_id_+1)*distributed_experiments_num_processes_ > num_processes_){
+      distributed_experiments_num_processes_ = num_processes_ - distributed_experiments_group_id_*distributed_experiments_num_processes_;
+    }
+
+    if(distributed_experiments_num_processes_ > num_process_per_experiment_ && (distributed_experiments_num_processes_ % num_process_per_experiment_) == 0){
+      distributed_shots_ = distributed_experiments_num_processes_ / num_process_per_experiment_;
+      distributed_shots_rank_ = 0;
+    }
+    else{
+      //shots are not distributed
+      distributed_shots_ = 1;
+      distributed_shots_rank_ = 0;
+    }
+    distributed_experiments_rank_ = myrank_ % distributed_experiments_;
+
+    distributed_experiments_begin_ = distributed_experiments_group_id_;
+    distributed_experiments_end_ = distributed_experiments_begin_ + 1;
+  }
+  else{
+    distributed_experiments_group_id_ = myrank_ / num_process_per_experiment_;
+    distributed_experiments_rank_ = myrank_ % num_process_per_experiment_;
+    distributed_experiments_num_processes_ = num_process_per_experiment_;
+
+    distributed_experiments_begin_ = circuits.size() * distributed_experiments_group_id_ / distributed_experiments_;
+    distributed_experiments_end_ = circuits.size() * (distributed_experiments_group_id_ + 1) / distributed_experiments_;
+
+    //shots are not distributed
+    distributed_shots_ = 1;
+    distributed_shots_rank_ = 0;
+  }
+}
+
+uint_t Controller::get_distributed_num_processes(bool par_shots) const
+{
+  if(par_shots){
+    return num_process_per_experiment_;
+  }
+  else{
+    return distributed_experiments_num_processes_;    //no shot distribution, parallelize this experiment by processes in group
+  }
+}
+
 bool Controller::multiple_chunk_required(const Circuit &circ,
                                 const Noise::NoiseModel &noise) const
 {
@@ -699,16 +802,31 @@
       }
     }
 
+#ifdef AER_MPI
+    try{
+      //catch exception raised by required_memory_mb because of invalid simulation method
+      set_distributed_parallelization(circuits, circ_noise_models);
+    }
+    catch (std::exception &e) {
+      save_exception_to_results(result,e);
+    }
+
+    const auto num_circuits = distributed_experiments_end_ - distributed_experiments_begin_;
+    result.resize(num_circuits);
+#endif
 
     //get max qubits for this process (to allocate qubit register at once)
     max_qubits_ = 0;
+#ifdef AER_MPI
+    for (size_t j = distributed_experiments_begin_; j < distributed_experiments_end_; j++) {
+#else
     for (size_t j = 0; j < circuits.size(); j++) {
+#endif
       if(circuits[j].num_qubits > max_qubits_){
         max_qubits_ = circuits[j].num_qubits;
       }
     }
 
-    num_process_per_experiment_ = num_processes_;
     if (!explicit_parallelization_) {
       // set parallelization for experiments
       try{
@@ -732,6 +850,11 @@
     //store rank and number of processes, if no distribution rank=0 procs=1 is set
     result.metadata.add(num_processes_,"num_mpi_processes");
     result.metadata.add(myrank_,"mpi_rank");
+#ifdef AER_MPI
+    result.metadata.add(distributed_experiments_,"distributed_experiments");
+    result.metadata.add(distributed_experiments_group_id_,"distributed_experiments_group_id");
+    result.metadata.add(distributed_experiments_rank_,"distributed_experiments_rank_in_group");
+#endif
 
 #ifdef _OPENMP
     // Check if circuit parallelism is nested with one of the others
@@ -753,17 +876,21 @@
       #endif
     }
 #endif
+    uint_t offset = 0;
+#ifdef AER_MPI
+    offset = distributed_experiments_begin_;
+#endif
     // then- and else-blocks have intentionally duplication.
     // Nested omp has significant overheads even though a guard condition exists.
     const int NUM_RESULTS = result.results.size();
     if (parallel_experiments_ > 1) {
       #pragma omp parallel for num_threads(parallel_experiments_)
       for (int j = 0; j < result.results.size(); ++j) {
-        execute_circuit(circuits[j], circ_noise_models[j], config, result.results[j]);
+        execute_circuit(circuits[j + offset], circ_noise_models[j + offset], config, result.results[j]);
       }
     } else {
       for (int j = 0; j < result.results.size(); ++j) {
-        execute_circuit(circuits[j], circ_noise_models[j], config, result.results[j]);
+        execute_circuit(circuits[j + offset], circ_noise_models[j + offset], config, result.results[j]);
       }
     }
 
@@ -831,6 +958,11 @@
     }
 
     int shots = circ.shots;
+#ifdef AER_MPI
+    if(parallel_shots_ > 1 && distributed_shots_ > 1){   //if shots can be distributed
+      shots = (circ.shots * (distributed_shots_rank_ + 1)/distributed_shots_) - (circ.shots * distributed_shots_rank_ /distributed_shots_);
+    }
+#endif
 
     // Single shot thread execution
     if (parallel_shots_ <= 1) {
@@ -900,6 +1032,11 @@
     result.seed = circ.seed;
     result.metadata.add(parallel_shots_, "parallel_shots");
     result.metadata.add(parallel_state_update_, "parallel_state_update");
+#ifdef AER_MPI
+    if(parallel_shots_ > 1 && distributed_shots_ > 1){
+      result.metadata.add(distributed_shots_,"distributed_shots");
+    }
+#endif
     // Add timer data
     auto timer_stop = myclock_t::now(); // stop timer
     double time_taken =
