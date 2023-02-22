--- xacc/xacc#362/after/QsimAccelerator.hpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#362/before/QsimAccelerator.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -13,11 +13,6 @@
 #pragma one
 #include "xacc.hpp"
 #include "AllGateVisitor.hpp"
-#ifdef __AVX2__
-#ifndef __FMA__
-#undef __AVX2__
-#endif
-#endif
 // Qsim:
 #include "circuit.h"
 #include "gates_qsim.h"
