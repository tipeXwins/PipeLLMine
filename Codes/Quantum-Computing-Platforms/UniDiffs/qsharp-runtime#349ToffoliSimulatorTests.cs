--- qsharp-runtime/qsharp-runtime#349/after/ToffoliSimulatorTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/ToffoliSimulatorTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -113,12 +113,12 @@
             var measure = sim.Get<Intrinsic.M>();
             var set = sim.Get<SetQubit>();
 
-            var ctrlX = x.__ControlledBody__.AsAction();
+            var ctrlX = x.ControlledBody.AsAction();
 
             OperationsTestHelper.ctrlTestShell(sim, ctrlX, (enabled, ctrls, q) =>
             {
                 set.Apply((Result.Zero, q));
-                x.__ControlledBody__((ctrls, q));
+                x.ControlledBody((ctrls, q));
 
                 var result = measure.Apply(q);
                 var expected = (enabled) ? Result.One : Result.Zero;
