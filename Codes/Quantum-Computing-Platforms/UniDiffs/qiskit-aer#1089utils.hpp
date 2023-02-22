--- qiskit-aer/qiskit-aer#1089/after/utils.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1089/before/utils.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -1018,7 +1018,7 @@
 
   // We go via long integer conversion, so we process 64-bit chunks at
   // a time
-  const size_t block = 16;
+  const size_t block = 8;
   const size_t len = str.size();
   const size_t chunks = len / block;
   const size_t remain = len % block;
@@ -1027,8 +1027,7 @@
   std::string bin = (prefix) ? "0b" : "";
 
   // Start with remain
-  if (remain != 0)
-      bin += int2string(std::stoull(str.substr(0, remain), nullptr, 16), 2);
+  bin += int2string(std::stoull(str.substr(0, remain), nullptr, 16), 2);
   for (size_t j=0; j < chunks; ++j) {
     std::string part = int2string(std::stoull(str.substr(remain + j * block, block), nullptr, 16), 2, 64);
     bin += part;
