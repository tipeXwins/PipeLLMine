--- xacc/xacc#309_B/after/kak.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#309_B/before/kak.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -524,7 +524,7 @@
 
     const std::complex<double> globalFactor = in_mat(rowIdx, colIdx) / totalU(rowIdx, colIdx);
     totalU = globalFactor * totalU;
-    return allClose(in_mat, totalU, 1e-6);
+    return allClose(in_mat, totalU);
   };
 
   assert(validateSimplifiedSequence(composite, in_mat));
@@ -772,7 +772,7 @@
       const double xAngle = -2 * x;
       const double yAngle = -2 * y;
       auto composite = gateRegistry->createComposite("__TEMP__INTERACTION_COMPOSITE__" + std::to_string(getTempId()));  
-      composite->addInstruction(gateRegistry->createInstruction("Rx", { bit2 }, { M_PI_2 }));
+      composite->addInstruction(gateRegistry->createInstruction("Rx", { bit1 }, { M_PI_2 }));
       composite->addInstruction(gateRegistry->createInstruction("H", { bit1 }));
       composite->addInstruction(gateRegistry->createInstruction("CZ", { bit2, bit1 }));
       composite->addInstruction(gateRegistry->createInstruction("H", { bit1 }));
