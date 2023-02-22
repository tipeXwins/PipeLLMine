--- qsharp-runtime/qsharp-runtime#533/after/tracer-target.qs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#533/before/tracer-target.qs	2022-01-10 16:02:54.000000000 +0000
@@ -3,33 +3,26 @@
 
 namespace Microsoft.Quantum.Instructions {
 
-    open Microsoft.Quantum.Targeting;
-    @TargetInstruction("single_qubit_op")
     operation single_qubit_op(op_id: Int, duration: Int, qb : Qubit) : Unit {
         body intrinsic;
     }
 
-    @TargetInstruction("multi_qubit_op")
     operation multi_qubit_op(op_id: Int, duration: Int, qbs : Qubit[]) : Unit {
         body intrinsic;
     }
 
-    @TargetInstruction("single_qubit_op_ctl")
     operation single_qubit_op_ctl(op_id: Int, duration: Int, ctl : Qubit[], qb : Qubit) : Unit {
         body intrinsic;
     }
 
-    @TargetInstruction("multi_qubit_op_ctl")
     operation multi_qubit_op_ctl(op_id: Int, duration: Int, ctl : Qubit[], qbs : Qubit[]) : Unit {
         body intrinsic;
     }
 
-    @TargetInstruction("single_qubit_measure")
     operation single_qubit_measure(op_id: Int, duration: Int, qb : Qubit) : Result {
         body intrinsic;
     }
 
-    @TargetInstruction("joint_measure")
     operation joint_measure(op_id: Int, duration: Int, qbs : Qubit[]) : Result {
         body intrinsic;
     }
@@ -105,8 +98,7 @@
 
 namespace Microsoft.Quantum.Tracer {
 
-    open Microsoft.Quantum.Targeting;
-    @TargetInstruction("inject_barrier")
+    @TargetInstruction("inject_global_barrier")
     operation Barrier(id : Int, duration : Int) : Unit {
         body intrinsic;
     }
@@ -133,7 +125,7 @@
     is Adj + Ctl {
         body  (...) { Controlled X([control], target); }
         adjoint self;
-        controlled (ctls, ...) { Controlled X(ctls + [control], target); }
+        controlled (ctls, ...) { Controlled X(ctls + control, target); }
     }
 
     @Inline()
@@ -213,7 +205,7 @@
 
     @Inline()
     operation M(qb : Qubit) : Result {
-        body  (...) { return Phys.Mz(qb); }
+        body  (...) { return Phyz.Mz(qb); }
     }
 
     @Inline()
@@ -234,8 +226,8 @@
 
             // Single qubit measurement -- differentiate between Mx and Mz
             elif Length(paulis) == 1 {
-                if (paulis[0] == PauliX) { set res = Phys.Mx(qubits[0]); }
-                else { set res = Phys.Mz(qubits[0]); }
+                if (paulis[0] == PauliX) { set res = Mx(qubits[0]); }
+                else { set res = Mz(qubits[0]); }
             }
 
             // Specialize for two-qubit measurements: Mxx, Mxz, Mzx, Mzz
