--- qsharp-runtime/qsharp-runtime#349/after/BasicTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/BasicTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -62,7 +62,7 @@
                 var measure = sim.Get<Intrinsic.M>();
                 var set = sim.Get<SetQubit>();
 
-                var ctrlX = x.__ControlledBody__.AsAction();
+                var ctrlX = x.ControlledBody.AsAction();
                 OperationsTestHelper.ctrlTestShell(sim, ctrlX, (enabled, ctrls, q) =>
                 {
                     set.Apply((Result.Zero, q));
@@ -70,7 +70,7 @@
                     var expected = Result.Zero;
                     Assert.Equal(expected, result);
 
-                    x.__ControlledBody__((ctrls, q));
+                    x.ControlledBody((ctrls, q));
                     result = measure.Apply(q);
                     expected = (enabled) ? Result.One : Result.Zero;
                     Assert.Equal(expected, result);
