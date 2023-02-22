--- qiskit-aer/qiskit-aer#707/after/operations.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#707/before/operations.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -681,7 +681,7 @@
     throw std::invalid_argument("\"diagonal\" matrix is wrong size.");
   }
   for (const auto val : op.params) {
-    if (!Linalg::almost_equal(std::abs(val), 1.0, 1e-7)) {
+    if (!Linalg::almost_equal(std::abs(val), 1.0)) {
       throw std::invalid_argument("\"diagonal\" matrix is not unitary.");
     }
   }
