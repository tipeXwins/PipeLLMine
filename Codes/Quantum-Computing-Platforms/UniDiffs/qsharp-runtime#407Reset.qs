--- qsharp-runtime/qsharp-runtime#407/after/Reset.qs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#407/before/Reset.qs	2022-01-10 16:02:54.000000000 +0000
@@ -3,7 +3,6 @@
 
 namespace Microsoft.Quantum.Measurement {
     open Microsoft.Quantum.Intrinsic;
-    open Microsoft.Quantum.Targeting;
 
     internal operation BasisChangeZtoY(target : Qubit) : Unit is Adj + Ctl {
         H(target);
@@ -46,10 +45,6 @@
     ///
     /// # Output
     /// The result of measuring `target` in the Pauli $Z$ basis.
-    @RequiresCapability(
-        "BasicQuantumFunctionality",
-        "MResetZ is replaced by a supported implementation on all execution targets."
-    )
     operation MResetZ (target : Qubit) : Result {
         let result = M(target);
 
@@ -80,10 +75,6 @@
     ///
     /// # Output
     /// The result of measuring `target` in the Pauli $X$ basis.
-    @RequiresCapability(
-        "BasicQuantumFunctionality",
-        "MResetX is replaced by a supported implementation on all execution targets."
-    )
     operation MResetX (target : Qubit) : Result {
         let result = Measure([PauliX], [target]);
 
@@ -117,10 +108,6 @@
     ///
     /// # Output
     /// The result of measuring `target` in the Pauli $Y$ basis.
-    @RequiresCapability(
-        "BasicQuantumFunctionality",
-        "MResetY is replaced by a supported implementation on all execution targets."
-    )
     operation MResetY (target : Qubit) : Result {
         let result = Measure([PauliY], [target]);
 
