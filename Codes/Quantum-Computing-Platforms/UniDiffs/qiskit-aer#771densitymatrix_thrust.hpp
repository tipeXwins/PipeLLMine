--- qiskit-aer/qiskit-aer#771/after/densitymatrix_thrust.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#771/before/densitymatrix_thrust.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -442,10 +442,10 @@
     q2 = pV[offsets[2]+i0];
     q3 = pV[offsets[3]+i0];
 
-    pV[offsets[0]+i0] = q3;
+    pV[offsets[0]+i0] = q0;
     pV[offsets[1]+i0] = -q2;
     pV[offsets[2]+i0] = -q1;
-    pV[offsets[3]+i0] = q0;
+    pV[offsets[3]+i0] = q3;
 		return 0.0;
   }
 
