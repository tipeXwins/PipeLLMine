--- qiskit-aer/qiskit-aer#1278/after/qasm_controller.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1278/before/qasm_controller.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -204,6 +204,10 @@
       const Circuit& circ,
       const Noise::NoiseModel& noise) override;
 
+  // Set distributed parallelization
+  virtual void
+  set_distributed_parallelization(const std::vector<Circuit> &circuits,
+                                  const std::vector<Noise::NoiseModel> &noise) override;
 
   // Return a fusion transpilation pass configured for the current
   // method, circuit and config
@@ -961,6 +965,59 @@
   }
 }
 
+
+void QasmController::set_distributed_parallelization(const std::vector<Circuit> &circuits,
+                                  const std::vector<Noise::NoiseModel> &noise)
+{
+#ifdef AER_MPI
+  uint_t i,ncircuits;
+  bool sample_opt = true;
+
+  ncircuits = circuits.size();
+  for(i=0;i<ncircuits;i++){
+    const auto method = simulation_method(circuits[i], noise[i], false);
+    switch (method) {
+      case Method::statevector:
+      case Method::statevector_thrust_gpu:
+      case Method::statevector_thrust_cpu:
+      case Method::stabilizer:
+      case Method::matrix_product_state: {
+        if (circuits[i].shots > 1 &&
+            (noise[i].has_quantum_errors() ||
+             !check_measure_sampling_opt(circuits[i], Method::statevector))) {
+          sample_opt = false;
+        }
+        break;
+      }
+      case Method::density_matrix:
+      case Method::density_matrix_thrust_gpu:
+      case Method::density_matrix_thrust_cpu: {
+        if (circuits[i].shots > 1 &&
+            !check_measure_sampling_opt(circuits[i], Method::density_matrix)) {
+          sample_opt = false;
+        }
+        break;
+      }
+      default: {
+        sample_opt = false;
+      }
+    }
+    if(!sample_opt){
+      break;
+    }
+  }
+
+
+  if(sample_opt){
+    Base::Controller::set_distributed_parallelization(circuits, noise);
+
+    //shots are not distributed
+    Base::Controller::distributed_shots_ = 1;
+    Base::Controller::distributed_shots_rank_ = 0;
+  }
+#endif
+}
+
 //-------------------------------------------------------------------------
 // Run circuit helpers
 //-------------------------------------------------------------------------
@@ -984,7 +1041,7 @@
   // Set state config
   state.set_config(config);
   state.set_parallalization(parallel_state_update_);
-  state.set_distribution(Base::Controller::num_process_per_experiment_);
+  state.set_distribution(Base::Controller::get_distributed_num_processes(shots == circ.shots));
   state.set_global_phase(circ.global_phase_angle);
 
   // Rng engine
