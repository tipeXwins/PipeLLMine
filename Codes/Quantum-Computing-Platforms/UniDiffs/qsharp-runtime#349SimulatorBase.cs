--- qsharp-runtime/qsharp-runtime#349/after/SimulatorBase.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/SimulatorBase.cs	2022-01-10 16:02:54.000000000 +0000
@@ -105,7 +105,7 @@
 
         public virtual void Init(AbstractCallable op)
         {
-            op.__Init__();
+            op.Init();
         }
 
         public override AbstractCallable CreateInstance(Type t)
@@ -395,7 +395,7 @@
                 sim = m;
             }
 
-            public override Func<String, QVoid> __Body__ => (msg) =>
+            public override Func<String, QVoid> Body => (msg) =>
             {
                 sim.OnLog?.Invoke(msg);
                 return QVoid.Instance;
@@ -414,7 +414,7 @@
                 sim = m;
             }
 
-            public override Func<QVoid, long> __Body__ => (arg) => sim.QubitManager.GetFreeQubitsCount();
+            public override Func<QVoid, long> Body => (arg) => sim.QubitManager.GetFreeQubitsCount();
         }
 
         /// <summary>
@@ -429,7 +429,7 @@
                 sim = m;
             }
 
-            public override Func<QVoid, long> __Body__ => (arg) => sim.QubitManager.GetParentQubitsAvailableToBorrowCount() +
+            public override Func<QVoid, long> Body => (arg) => sim.QubitManager.GetParentQubitsAvailableToBorrowCount() +
                                                                sim.QubitManager.GetFreeQubitsCount();
         }
 
@@ -446,7 +446,7 @@
                 sim = m;
             }
 
-            public override Func<(long, long), long> __Body__ => arg =>
+            public override Func<(long, long), long> Body => arg =>
             {
                 var (min, max) = arg;
                 if (max <= min)
@@ -470,7 +470,7 @@
                 sim = m;
             }
 
-            public override Func<(double, double), double> __Body__ => arg =>
+            public override Func<(double, double), double> Body => arg =>
             {
                 var (min, max) = arg;
                 if (max <= min)
