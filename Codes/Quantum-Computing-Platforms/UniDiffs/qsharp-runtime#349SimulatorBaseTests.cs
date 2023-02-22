--- qsharp-runtime/qsharp-runtime#349/after/SimulatorBaseTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/SimulatorBaseTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -328,9 +328,9 @@
             {
             }
 
-            public override Func<Qubit, QVoid> __Body__ => throw new NotImplementedException();
+            public override Func<Qubit, QVoid> Body => throw new NotImplementedException();
 
-            public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledBody__ => throw new NotImplementedException();
+            public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledBody => throw new NotImplementedException();
         }
 
         /// <summary>
@@ -343,9 +343,9 @@
             {
             }
 
-            public override Func<Qubit, Result> __Body__ => throw new NotImplementedException();
+            public override Func<Qubit, Result> Body => throw new NotImplementedException();
 
-            public override void __Init__()
+            public override void Init()
             {
             }
         }
@@ -363,12 +363,12 @@
 
             public IUnitary<Qubit> X { get; set; }
 
-            public override void __Init__()
+            public override void Init()
             {
-                this.X = this.__Factory__.Get<IUnitary<Qubit>, Intrinsic.X>();
+                this.X = this.Factory.Get<IUnitary<Qubit>, Intrinsic.X>();
             }
 
-            public override Func<QVoid, QVoid> __Body__ => throw new NotImplementedException();
+            public override Func<QVoid, QVoid> Body => throw new NotImplementedException();
         }
 
         /// <summary>
@@ -384,15 +384,15 @@
 
             string ICallable.FullName => "LikeX";
 
-            public override void __Init__() { }
+            public override void Init() { }
 
-            public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledAdjointBody__ => throw new NotImplementedException();
+            public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledAdjointBody => throw new NotImplementedException();
 
-            public override Func<Qubit, QVoid> __AdjointBody__ => throw new NotImplementedException();
+            public override Func<Qubit, QVoid> AdjointBody => throw new NotImplementedException();
 
-            public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledBody__ => throw new NotImplementedException();
+            public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledBody => throw new NotImplementedException();
 
-            public override Func<Qubit, QVoid> __Body__ => throw new NotImplementedException();
+            public override Func<Qubit, QVoid> Body => throw new NotImplementedException();
         }
 
 
@@ -407,14 +407,14 @@
 
             public ICallable B { get; set; }
 
-            public override void __Init__()
+            public override void Init()
             {
-                this.B = this.__Factory__.Get<ICallable, B>();
+                this.B = this.Factory.Get<ICallable, B>();
             }
 
             string ICallable.FullName => "A";
 
-            public override Func<QVoid, QVoid> __Body__ => (_) => { return QVoid.Instance; };
+            public override Func<QVoid, QVoid> Body => (_) => { return QVoid.Instance; };
         }
 
         /// <summary>
@@ -430,12 +430,12 @@
 
             public ICallable A { get; set; }
 
-            public override void __Init__()
+            public override void Init()
             {
-                this.A = this.__Factory__.Get<ICallable, A>();
+                this.A = this.Factory.Get<ICallable, A>();
             }
 
-            public override Func<QVoid, QVoid> __Body__ => (_) => { return QVoid.Instance; };
+            public override Func<QVoid, QVoid> Body => (_) => { return QVoid.Instance; };
         }
 
         public class Gen<T> : Operation<T, QVoid>, ICallable
@@ -446,16 +446,16 @@
 
             string ICallable.FullName => "Gen";
 
-            public override Func<T, QVoid> __Body__ => (_) => { return QVoid.Instance; };
+            public override Func<T, QVoid> Body => (_) => { return QVoid.Instance; };
 
             public ICallable A { get; set; }
 
             public IUnitary<Qubit> X { get; set; }
 
-            public override void __Init__()
+            public override void Init()
             {
-                this.A = this.__Factory__.Get<ICallable, A>();
-                this.X = this.__Factory__.Get<IUnitary<Qubit>, Intrinsic.X>();
+                this.A = this.Factory.Get<ICallable, A>();
+                this.X = this.Factory.Get<IUnitary<Qubit>, Intrinsic.X>();
             }
         }
 
@@ -470,11 +470,11 @@
 
             public ICallable Gen { get; set; }
 
-            public override Func<QVoid, QVoid> __Body__ => (_) => { return QVoid.Instance; };
+            public override Func<QVoid, QVoid> Body => (_) => { return QVoid.Instance; };
 
-            public override void __Init__()
+            public override void Init()
             {
-                this.Gen = this.__Factory__.Get<ICallable>(typeof(Gen<>));
+                this.Gen = this.Factory.Get<ICallable>(typeof(Gen<>));
             }
         }
     }
