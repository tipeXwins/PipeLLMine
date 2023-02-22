--- qsharp-runtime/qsharp-runtime#576/after/QCTraceSimulatorImpl.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#576/before/QCTraceSimulatorImpl.cs	2022-01-10 16:02:54.000000000 +0000
@@ -152,7 +152,7 @@
             var intrinsicAssembly = coreAssembly;
             if (intrinsicAssembly == null)
             {
-                var currentName = typeof(QCTraceSimulatorImpl).Assembly.GetName();
+                var currentName = this.GetType().Assembly.GetName();
                 var coreName = currentName.FullName.Replace("Simulators", "QSharp.Core");
                 try
                 {
