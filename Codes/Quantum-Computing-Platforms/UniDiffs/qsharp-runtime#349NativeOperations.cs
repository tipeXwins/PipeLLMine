--- qsharp-runtime/qsharp-runtime#349/after/NativeOperations.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/NativeOperations.cs	2022-01-10 16:02:54.000000000 +0000
@@ -20,7 +20,7 @@
         {
             public Native(IOperationFactory m) : base(m) { }
 
-            public override Func<QVoid, String> __Body__ => (arg) =>
+            public override Func<QVoid, String> Body => (arg) =>
             {
                 return RESULT;
             };
@@ -34,18 +34,18 @@
         {
             public Native(IOperationFactory m) : base(m) { }
 
-            public override Func<QVoid, String> __Body__ => (arg) =>
+            public override Func<QVoid, String> Body => (arg) =>
             {
-                if (this.__Factory__ is QuantumSimulator)
+                if (this.Factory is QuantumSimulator)
                 {
                     return "Simulator";
                 }
-                else if (this.__Factory__ is ToffoliSimulator)
+                else if (this.Factory is ToffoliSimulator)
                 {
                     return "Toffoli";
                 }
 
-                return base.__Body__(arg);
+                return base.Body(arg);
             };
         }
     }
@@ -58,7 +58,7 @@
         {
             public Other1(IOperationFactory m) : base(m) { }
 
-            public override Func<__T__, string> __Body__ => throw new NotImplementedException();
+            public override Func<__T__, string> Body => throw new NotImplementedException();
         }
 
         // This one should not be used, it has the same number of Type parameters,
@@ -70,7 +70,7 @@
         {
             public Emulation(IOperationFactory m) : base(m) { }
 
-            public override Func<__T__, string> __Body__ => (arg) =>
+            public override Func<__T__, string> Body => (arg) =>
             {
                 if (arg is string s)
                 {
@@ -92,7 +92,7 @@
         {
             public Emulation(IOperationFactory m) : base(m) { }
 
-            public override Func<__T__, __T__> __Body__ => (arg) =>
+            public override Func<__T__, __T__> Body => (arg) =>
             {
                 if (arg is string s)
                 {
@@ -100,9 +100,9 @@
                 }
                 else
                 {
-                    return base.__Body__(arg);
+                    return base.Body(arg);
                 }
             };
         }
     }
-}
+}
\ No newline at end of file
