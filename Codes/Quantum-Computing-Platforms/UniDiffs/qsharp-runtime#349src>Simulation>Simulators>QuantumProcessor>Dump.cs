--- qsharp-runtime/qsharp-runtime#349/after/src>Simulation>Simulators>QuantumProcessor>Dump.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/src>Simulation>Simulators>QuantumProcessor>Dump.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,7 +17,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<T, QVoid> __Body__ => (location) =>
+            public override Func<T, QVoid> Body => (location) =>
             {
                 if (location == null) { throw new ArgumentNullException(nameof(location)); }
 
@@ -36,7 +36,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<(T, IQArray<Qubit>), QVoid> __Body__ => (__in) =>
+            public override Func<(T, IQArray<Qubit>), QVoid> Body => (__in) =>
             {
                 var (location, qubits) = __in;
 
