--- xacc/xacc#378/after/QlmAccelerator.in.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#378/before/QlmAccelerator.in.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -513,7 +513,7 @@
     auto hw_model = hardwareModel(gates_spec, all_gates_noise);
     // Noisy simulator:
     auto noisyQProc = pybind11::module::import("qat.qpus").attr("NoisyQProc");
-    m_qlmQpuServer = noisyQProc(hw_model, "deterministic-vectorized");
+    m_qlmQpuServer = noisyQProc(hw_model);
   } else if (params.stringExists("backend")) {
     m_noiseModel = xacc::getService<NoiseModel>("IBM");
     m_noiseModel->initialize(params);
@@ -546,9 +546,7 @@
     }();
 
     pybind11::dict gates_noise;
-    for (const auto &iter : QLM_GATE_ERRORS) {
-      auto aqasmGate = iter.first;
-      auto errorRate = iter.second;
+    for (const auto &[aqasmGate, errorRate] : QLM_GATE_ERRORS) {
       // std::cout << aqasmGate << ": " << errorRate << "\n";
       if (aqasmGate == "RX" || aqasmGate == "RY" || aqasmGate == "RZ") {
         gates_noise[aqasmGate.c_str()] = pybind11::cpp_function(
@@ -834,9 +832,6 @@
   if (m_noiseModel && m_shots < 0) {
     auto compute_density_matrix =
         pybind11::module::import("qat.noisy").attr("compute_density_matrix");
-    auto qlmJob = constructQlmJob(buffer, compositeInstruction);
-    auto result = m_qlmQpuServer.attr("submit")(qlmJob);
-    persistResultToBuffer(buffer, result, qlmJob);
     auto circ = constructQlmCirc(buffer, compositeInstruction);
     pybind11::array_t<std::complex<double>> rho =
         compute_density_matrix(circ, m_qlmQpuServer);
