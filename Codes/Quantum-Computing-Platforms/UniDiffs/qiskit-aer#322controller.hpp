--- qiskit-aer/qiskit-aer#322/after/controller.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#322/before/controller.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -599,7 +599,6 @@
   // Initialize circuit json return
   json_t result;
   OutputData data;
-  data.set_config(config);
 
   // Execute in try block so we can catch errors and return the error message
   // for individual circuit failures.
