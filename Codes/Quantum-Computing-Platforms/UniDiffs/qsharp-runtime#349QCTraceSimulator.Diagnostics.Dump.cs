--- qsharp-runtime/qsharp-runtime#349/after/QCTraceSimulator.Diagnostics.Dump.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/QCTraceSimulator.Diagnostics.Dump.cs	2022-01-10 16:02:54.000000000 +0000
@@ -17,13 +17,13 @@
                 core = m;
             }
 
-            public override Func<T, QVoid> __Body__ => (location) =>
+            public override Func<T, QVoid> Body => (location) =>
             {
                 if (location == null) { throw new ArgumentNullException(nameof(location)); }
                 var filename = (location is QVoid) ? "" : location.ToString();
                 var msg = "QCTraceSimulator doesn't support state dump.";
 
-                var logMessage = this.__Factory__.Get<ICallable<string, QVoid>, Intrinsic.Message>();
+                var logMessage = this.Factory.Get<ICallable<string, QVoid>, Intrinsic.Message>();
 
                 if (string.IsNullOrEmpty(filename))
                 {
@@ -54,7 +54,7 @@
                 core = m;
             }
 
-            public override Func<(T, IQArray<Qubit>), QVoid> __Body__ => (__in) =>
+            public override Func<(T, IQArray<Qubit>), QVoid> Body => (__in) =>
             {
                 var (location, qubits) = __in;
 
@@ -62,7 +62,7 @@
                 var filename = (location is QVoid) ? "" : location.ToString();
                 var msg = "QCTraceSimulator doesn't support state dump.";
 
-                var logMessage = this.__Factory__.Get<ICallable<string, QVoid>, Intrinsic.Message>();
+                var logMessage = this.Factory.Get<ICallable<string, QVoid>, Intrinsic.Message>();
 
                 if (string.IsNullOrEmpty(filename))
                 {
