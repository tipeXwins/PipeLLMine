--- qsharp-runtime/qsharp-runtime#349/after/AssertEqual.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/AssertEqual.cs	2022-01-10 16:02:54.000000000 +0000
@@ -13,7 +13,7 @@
         {
             public Native(IOperationFactory m) : base(m) { }
 
-            public override Func<(__T__, __T__), QVoid> __Body__ => (_args) =>
+            public override Func<(__T__, __T__), QVoid> Body => (_args) =>
             {
                 var (expected, actual) = _args;
                 Assert.Equal(expected, actual);
