--- qiskit-terra/qiskit-terra#440/after/clifford_backend.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-terra/qiskit-terra#440/before/clifford_backend.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -406,13 +406,13 @@
 
 void CliffordBackend::qc_idle(uint_t qubit) {
 
-  if (noise_flag && !gate_error("id").ideal) {
+  if (noise_flag && !gate_error("idle").ideal) {
 #ifdef DEBUG
     std::stringstream ss;
     ss << "DEBUG CliffordBackend::qc_gate_id(" << qubit << ")";
     std::clog << ss.str() << std::endl;
 #endif
-    qc_relax(qubit, gate_error("id").gate_time);
+    qc_relax(qubit, gate_error("idle").gate_time);
   }
 }
 
