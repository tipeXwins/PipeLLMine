--- qsharp-runtime/qsharp-runtime#349/after/Math.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/Math.cs	2022-01-10 16:02:54.000000000 +0000
@@ -12,7 +12,7 @@
         public class Native : AbsD
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Abs;
+            public override Func<double, double> Body => System.Math.Abs;
         }
     }
 
@@ -21,7 +21,7 @@
         public class Native : AbsI
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<long, long> __Body__ => System.Math.Abs;
+            public override Func<long, long> Body => System.Math.Abs;
         }
     }
 
@@ -30,7 +30,7 @@
         public class Native : AbsL
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<BigInteger, BigInteger> __Body__ => BigInteger.Abs;
+            public override Func<BigInteger, BigInteger> Body => BigInteger.Abs;
         }
     }
 
@@ -39,7 +39,7 @@
         public class Native : ArcCos
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Acos;
+            public override Func<double, double> Body => System.Math.Acos;
         }
     }
 
@@ -48,7 +48,7 @@
         public class Native : ArcSin
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Asin;
+            public override Func<double, double> Body => System.Math.Asin;
         }
     }
 
@@ -57,7 +57,7 @@
         public class Native : ArcTan
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Atan;
+            public override Func<double, double> Body => System.Math.Atan;
         }
     }
 
@@ -67,7 +67,7 @@
         public class Native : ArcTan2
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(double, double), double> __Body__ => (args) => System.Math.Atan2(args.Item1, args.Item2);
+            public override Func<(double, double), double> Body => (args) => System.Math.Atan2(args.Item1, args.Item2);
         }
     }
 
@@ -76,7 +76,7 @@
         public class Native : Ceiling
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, long> __Body__ => (arg) => System.Convert.ToInt64(System.Math.Ceiling(arg));
+            public override Func<double, long> Body => (arg) => System.Convert.ToInt64(System.Math.Ceiling(arg));
         }
     }
 
@@ -85,7 +85,7 @@
         public class Native : Cos
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Cos;
+            public override Func<double, double> Body => System.Math.Cos;
         }
     }
 
@@ -94,7 +94,7 @@
         public class Native : Cosh
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Cosh;
+            public override Func<double, double> Body => System.Math.Cosh;
         }
     }
 
@@ -110,7 +110,7 @@
                 var div = BigInteger.DivRem(arg.Item1, arg.Item2, out rem);
                 return (div, rem);
             }
-            public override Func<(BigInteger, BigInteger), (BigInteger, BigInteger)> __Body__ => Impl;
+            public override Func<(BigInteger, BigInteger), (BigInteger, BigInteger)> Body => Impl;
         }
     }
 
@@ -119,7 +119,7 @@
         public class Native : E
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<QVoid, double> __Body__ => (arg) => System.Math.E;
+            public override Func<QVoid, double> Body => (arg) => System.Math.E;
         }
     }
 
@@ -128,7 +128,7 @@
         public class Native : ExpD
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Exp;
+            public override Func<double, double> Body => System.Math.Exp;
         }
     }
 
@@ -137,7 +137,7 @@
         public class Native : Floor
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, long> __Body__ => (arg) => System.Convert.ToInt64(System.Math.Floor(arg));
+            public override Func<double, long> Body => (arg) => System.Convert.ToInt64(System.Math.Floor(arg));
         }
     }
 
@@ -146,7 +146,7 @@
         public class Native : IEEERemainder
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(double, double), double> __Body__ => (arg) => System.Math.IEEERemainder(arg.Item1, arg.Item2);
+            public override Func<(double, double), double> Body => (arg) => System.Math.IEEERemainder(arg.Item1, arg.Item2);
         }
     }
 
@@ -155,7 +155,7 @@
         public class Native : Log
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Log;
+            public override Func<double, double> Body => System.Math.Log;
         }
     }
 
@@ -164,7 +164,7 @@
         public class Native : Log10
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => System.Math.Log10;
+            public override Func<double, double> Body => System.Math.Log10;
         }
     }
 
@@ -173,7 +173,7 @@
         public class Native : MaxD
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(double, double), double> __Body__ => (args) => System.Math.Max(args.Item1, args.Item2);
+            public override Func<(double, double), double> Body => (args) => System.Math.Max(args.Item1, args.Item2);
         }
     }
 
@@ -182,7 +182,7 @@
         public class Native : MaxI
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(long, long), long> __Body__ => (args) => System.Math.Max(args.Item1, args.Item2);
+            public override Func<(long, long), long> Body => (args) => System.Math.Max(args.Item1, args.Item2);
         }
     }
 
@@ -191,7 +191,7 @@
         public class Native : MaxL
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(BigInteger, BigInteger), BigInteger> __Body__ => (args) => BigInteger.Max(args.Item1, args.Item2);
+            public override Func<(BigInteger, BigInteger), BigInteger> Body => (args) => BigInteger.Max(args.Item1, args.Item2);
         }
     }
 
@@ -200,7 +200,7 @@
         public class Native : MinD
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(double, double), double> __Body__ => (args) => System.Math.Min(args.Item1, args.Item2);
+            public override Func<(double, double), double> Body => (args) => System.Math.Min(args.Item1, args.Item2);
         }
     }
 
@@ -209,7 +209,7 @@
         public class Native : MinI
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(long, long), long> __Body__ => (args) => System.Math.Min(args.Item1, args.Item2);
+            public override Func<(long, long), long> Body => (args) => System.Math.Min(args.Item1, args.Item2);
         }
     }
 
@@ -218,7 +218,7 @@
         public class Native : MinL
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(BigInteger, BigInteger), BigInteger> __Body__ => (args) => BigInteger.Min(args.Item1, args.Item2);
+            public override Func<(BigInteger, BigInteger), BigInteger> Body => (args) => BigInteger.Min(args.Item1, args.Item2);
         }
     }
 
@@ -227,7 +227,7 @@
         public class Native : ModPowL
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(BigInteger, BigInteger, BigInteger), BigInteger> __Body__ => (args) => BigInteger.ModPow(args.Item1, args.Item2, args.Item3);
+            public override Func<(BigInteger, BigInteger, BigInteger), BigInteger> Body => (args) => BigInteger.ModPow(args.Item1, args.Item2, args.Item3);
         }
     }
 
@@ -236,7 +236,7 @@
         public class Native : PI
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<QVoid, double> __Body__ => (arg) => System.Math.PI;
+            public override Func<QVoid, double> Body => (arg) => System.Math.PI;
         }
     }
 
@@ -245,7 +245,7 @@
         public class Native : PowD
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<(double, double), double> __Body__ => (arg) => System.Math.Pow(arg.Item1, arg.Item2);
+            public override Func<(double, double), double> Body => (arg) => System.Math.Pow(arg.Item1, arg.Item2);
         }
     }
 
@@ -254,7 +254,7 @@
         public class Native : Round
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, long> __Body__ => (arg) => System.Convert.ToInt64(System.Math.Round(arg));
+            public override Func<double, long> Body => (arg) => System.Convert.ToInt64(System.Math.Round(arg));
         }
     }
 
@@ -263,7 +263,7 @@
         public class Native : Sin
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => (theta) => System.Math.Sin(theta);
+            public override Func<double, double> Body => (theta) => System.Math.Sin(theta);
         }
     }
 
@@ -272,7 +272,7 @@
         public class Native : SignD
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, long> __Body__ => (arg) => System.Math.Sign(arg);
+            public override Func<double, long> Body => (arg) => System.Math.Sign(arg);
         }
     }
 
@@ -281,7 +281,7 @@
         public class Native : SignI
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<long, long> __Body__ => (arg) => System.Math.Sign(arg);
+            public override Func<long, long> Body => (arg) => System.Math.Sign(arg);
         }
     }
 
@@ -290,7 +290,7 @@
         public class Native : SignL
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<BigInteger, long> __Body__ => (arg) => arg.Sign;
+            public override Func<BigInteger, long> Body => (arg) => arg.Sign;
         }
     }
 
@@ -299,7 +299,7 @@
         public class Native : Sinh
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => (theta) => System.Math.Sinh(theta);
+            public override Func<double, double> Body => (theta) => System.Math.Sinh(theta);
         }
     }
 
@@ -308,7 +308,7 @@
         public class Native : Sqrt
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => (arg) => System.Math.Sqrt(arg);
+            public override Func<double, double> Body => (arg) => System.Math.Sqrt(arg);
         }
     }
 
@@ -317,7 +317,7 @@
         public class Native : Tan
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => (theta) => System.Math.Tan(theta);
+            public override Func<double, double> Body => (theta) => System.Math.Tan(theta);
         }
     }
 
@@ -326,7 +326,7 @@
         public class Native : Tanh
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, double> __Body__ => (theta) => System.Math.Tanh(theta);
+            public override Func<double, double> Body => (theta) => System.Math.Tanh(theta);
         }
     }
 
@@ -335,7 +335,7 @@
         public class Native : Truncate
         {
             public Native(IOperationFactory m) : base(m) { }
-            public override Func<double, long> __Body__ => (arg) => System.Convert.ToInt64(System.Math.Truncate(arg));
+            public override Func<double, long> Body => (arg) => System.Convert.ToInt64(System.Math.Truncate(arg));
         }
     }
 }
