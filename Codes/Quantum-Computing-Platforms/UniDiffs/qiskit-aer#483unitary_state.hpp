--- qiskit-aer/qiskit-aer#483/after/unitary_state.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#483/before/unitary_state.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -193,7 +193,7 @@
   {"cz", Gates::mcz},       // Controlled-Z gate
   {"cu1", Gates::mcu1},     // Controlled-u1 gate
   {"cu2", Gates::mcu2},    // Controlled-u2
-  {"cu3", Gates::mcu3},     // Controlled-u3 gate
+  {"cu3", Gates::mcu1},     // Controlled-u3 gate
   {"swap", Gates::mcswap},  // SWAP gate
   // Three-qubit gates
   {"ccx", Gates::mcx},      // Controlled-CX gate (Toffoli)
