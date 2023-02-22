--- qsharp-runtime/qsharp-runtime#349/after/Convert.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Convert.cs	2022-01-10 16:02:54.000000000 +0000
@@ -12,7 +12,7 @@
         public class Native : IntAsDouble
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<long, double> __Body__ => (arg) => System.Convert.ToDouble(arg);
+            public override Func<long, double> Body => (arg) => System.Convert.ToDouble(arg);
         }
     }
 
@@ -21,7 +21,7 @@
         public class Native : IntAsBigInt
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<long, BigInteger> __Body__ => (arg) => new BigInteger(arg);
+            public override Func<long, BigInteger> Body => (arg) => new BigInteger(arg);
         }
     }
 
@@ -43,7 +43,7 @@
             }
 
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<BigInteger, (long, bool)> __Body__ => MaybeBigIntAsIntFunc;
+            public override Func<BigInteger, (long, bool)> Body => MaybeBigIntAsIntFunc;
         }
     }
 
@@ -73,7 +73,7 @@
             }
 
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<BigInteger, IQArray<bool>> __Body__ => BigIntAsBoolArrayFunc;
+            public override Func<BigInteger, IQArray<bool>> Body => BigIntAsBoolArrayFunc;
         }
     }
 
@@ -110,7 +110,7 @@
             }
 
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<IQArray<bool>, BigInteger> __Body__ => BoolArrayAsBigIntFunc;
+            public override Func<IQArray<bool>, BigInteger> Body => BoolArrayAsBigIntFunc;
         }
     }
 
@@ -119,7 +119,7 @@
         public class Native : BoolAsString
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<bool, string> __Body__ => (arg) => System.Convert.ToString(arg);
+            public override Func<bool, string> Body => (arg) => System.Convert.ToString(arg);
         }
     }
 
@@ -128,7 +128,7 @@
         public class Native : DoubleAsString
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, string> __Body__ => (arg) => System.Convert.ToString(arg);
+            public override Func<double, string> Body => (arg) => System.Convert.ToString(arg);
         }
     }
 
@@ -137,7 +137,7 @@
         public class Native : DoubleAsStringWithFormat
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(double, string), string> __Body__ => (arg) => arg.Item1.ToString(arg.Item2);
+            public override Func<(double, string), string> Body => (arg) => arg.Item1.ToString(arg.Item2);
         }
     }
 
@@ -146,7 +146,7 @@
         public class Native : IntAsString
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<long, string> __Body__ => (arg) => System.Convert.ToString(arg);
+            public override Func<long, string> Body => (arg) => System.Convert.ToString(arg);
         }
     }
 
@@ -155,7 +155,7 @@
         public class Native : IntAsStringWithFormat
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(long, string), string> __Body__ => (arg) => arg.Item1.ToString(arg.Item2);
+            public override Func<(long, string), string> Body => (arg) => arg.Item1.ToString(arg.Item2);
         }
     }
 
@@ -194,7 +194,7 @@
             }
 
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<IQArray<Pauli>, long> __Body__ => PauliBitsFunc;
+            public override Func<IQArray<Pauli>, long> Body => PauliBitsFunc;
         }
     }
 }
