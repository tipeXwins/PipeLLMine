--- qsharp-runtime/qsharp-runtime#349/after/Reset.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Reset.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,7 +17,7 @@
                 this.Simulator = m;
             }
 
-            public override Func<Qubit, QVoid> __Body__ => (q1) =>
+            public override Func<Qubit, QVoid> Body => (q1) =>
             {
                 Simulator.QuantumProcessor.Reset(q1);
                 return QVoid.Instance;
