--- qsharp-runtime/qsharp-runtime#349/after/PartialMapperTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/PartialMapperTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -19,9 +19,9 @@
 
             string ICallable.FullName => "NoOp";
 
-            public override Func<TestTuple, QVoid> __Body__ => (a) => QVoid.Instance;
+            public override Func<TestTuple, QVoid> Body => (a) => QVoid.Instance;
 
-            public override void __Init__() { }
+            public override void Init() { }
         }
 
         private void TestOneTupleNoSubstitution<I>(I original, params object[] expected)
