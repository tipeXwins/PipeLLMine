--- qsharp-runtime/qsharp-runtime#349/after/Bitwise.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Bitwise.cs	2022-01-10 16:02:54.000000000 +0000
@@ -11,7 +11,7 @@
         public class Native : Xor
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(long, long), long> __Body__ => (arg) => (arg.Item1 ^ arg.Item2);
+            public override Func<(long, long), long> Body => (arg) => (arg.Item1 ^ arg.Item2);
         }
     }
 
@@ -20,7 +20,7 @@
         public class Native : And
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(long, long), long> __Body__ => (arg) => (arg.Item1 & arg.Item2);
+            public override Func<(long, long), long> Body => (arg) => (arg.Item1 & arg.Item2);
         }
     }
 
@@ -29,7 +29,7 @@
         public class Native : Or
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(long, long), long> __Body__ => (arg) => (arg.Item1 | arg.Item2);
+            public override Func<(long, long), long> Body => (arg) => (arg.Item1 | arg.Item2);
         }
     }
 
@@ -38,7 +38,7 @@
         public class Native : Not
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<long, long> __Body__ => (arg) => (~arg);
+            public override Func<long, long> Body => (arg) => (~arg);
         }
     }
 
@@ -57,7 +57,7 @@
             }
 
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<long, long> __Body__ => ParityFunc;
+            public override Func<long, long> Body => ParityFunc;
         }
     }
 
@@ -81,7 +81,7 @@
             }
 
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<IQArray<Pauli>, long> __Body__ => XBitsFunc;
+            public override Func<IQArray<Pauli>, long> Body => XBitsFunc;
         }
     }
 
@@ -105,7 +105,7 @@
             }
 
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<IQArray<Pauli>, long> __Body__ => ZBitsFunc;
+            public override Func<IQArray<Pauli>, long> Body => ZBitsFunc;
         }
     }
 }
