--- qsharp-runtime/qsharp-runtime#349/after/Release.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Release.cs	2022-01-10 16:02:54.000000000 +0000
@@ -13,6 +13,6 @@
 
         public abstract void Apply(IQArray<Qubit> qubits);
 
-        public override void __Init__() { }
+        public override void Init() { }
     }
 }
