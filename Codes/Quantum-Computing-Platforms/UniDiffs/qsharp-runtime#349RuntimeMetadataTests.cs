--- qsharp-runtime/qsharp-runtime#349/after/RuntimeMetadataTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/RuntimeMetadataTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -189,7 +189,7 @@
             var control = new FreeQubit(1);
             var target = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Intrinsic.CNOT>();
-            var args = op.__DataIn__((control, target));
+            var args = op.__dataIn((control, target));
             var expected = new RuntimeMetadata()
             {
                 Label = "X",
@@ -213,7 +213,7 @@
             var control2 = new FreeQubit(2);
             var target = new FreeQubit(1);
             var op = new QuantumSimulator().Get<Intrinsic.CCNOT>();
-            var args = op.__DataIn__((control1, control2, target));
+            var args = op.__dataIn((control1, control2, target));
             var expected = new RuntimeMetadata()
             {
                 Label = "X",
@@ -236,7 +236,7 @@
             var q1 = new FreeQubit(0);
             var q2 = new FreeQubit(1);
             var op = new QuantumSimulator().Get<Intrinsic.SWAP>();
-            var args = op.__DataIn__((q1, q2));
+            var args = op.__dataIn((q1, q2));
             var expected = new RuntimeMetadata()
             {
                 Label = "SWAP",
@@ -258,7 +258,7 @@
         {
             var target = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Intrinsic.Ry>();
-            var args = op.__DataIn__((2.1, target));
+            var args = op.__dataIn((2.1, target));
             var expected = new RuntimeMetadata()
             {
                 Label = "Ry",
@@ -280,7 +280,7 @@
         {
             var measureQubit = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Intrinsic.M>();
-            var args = op.__DataIn__(measureQubit);
+            var args = op.__dataIn(measureQubit);
             var expected = new RuntimeMetadata()
             {
                 Label = "M",
@@ -302,7 +302,7 @@
         {
             var target = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Intrinsic.Reset>();
-            var args = op.__DataIn__(target);
+            var args = op.__dataIn(target);
             var expected = new RuntimeMetadata()
             {
                 Label = "Reset",
@@ -324,7 +324,7 @@
         {
             IQArray<Qubit> targets = new QArray<Qubit>(new[] { new FreeQubit(0) });
             var op = new QuantumSimulator().Get<Intrinsic.ResetAll>();
-            var args = op.__DataIn__(targets);
+            var args = op.__dataIn(targets);
             var expected = new RuntimeMetadata()
             {
                 Label = "ResetAll",
@@ -349,7 +349,7 @@
         {
             var measureQubit = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Measurement.MResetX>();
-            var args = op.__DataIn__(measureQubit);
+            var args = op.__dataIn(measureQubit);
             var expected = new RuntimeMetadata()
             {
                 Label = "MResetX",
@@ -371,7 +371,7 @@
         {
             var measureQubit = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Measurement.MResetY>();
-            var args = op.__DataIn__(measureQubit);
+            var args = op.__dataIn(measureQubit);
             var expected = new RuntimeMetadata()
             {
                 Label = "MResetY",
@@ -393,7 +393,7 @@
         {
             var measureQubit = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Measurement.MResetZ>();
-            var args = op.__DataIn__(measureQubit);
+            var args = op.__dataIn(measureQubit);
             var expected = new RuntimeMetadata()
             {
                 Label = "MResetZ",
@@ -418,7 +418,7 @@
         {
             var measureQubit = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Circuits.Empty>();
-            var args = op.__DataIn__(QVoid.Instance);
+            var args = op.__dataIn(QVoid.Instance);
             var expected = new RuntimeMetadata()
             {
                 Label = "Empty",
@@ -441,7 +441,7 @@
             var q = new FreeQubit(0);
             var opArg = new QuantumSimulator().Get<Circuits.HOp>();
             var op = new QuantumSimulator().Get<Circuits.WrapperOp>();
-            var args = op.__DataIn__((opArg, q));
+            var args = op.__dataIn((opArg, q));
             var expected = new RuntimeMetadata()
             {
                 Label = "WrapperOp",
@@ -462,7 +462,7 @@
         public void NestedOperation()
         {
             var op = new QuantumSimulator().Get<Circuits.NestedOp>();
-            var args = op.__DataIn__(QVoid.Instance);
+            var args = op.__dataIn(QVoid.Instance);
             var expected = new RuntimeMetadata()
             {
                 Label = "NestedOp",
@@ -484,7 +484,7 @@
         {
             var q = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Circuits.TwoQubitOp>();
-            var args = op.__DataIn__((q, q));
+            var args = op.__dataIn((q, q));
             var expected = new RuntimeMetadata()
             {
                 Label = "TwoQubitOp",
@@ -506,7 +506,7 @@
         {
             var op = new QuantumSimulator().Get<Circuits.BoolArrayOp>();
             IQArray<Boolean> bits = new QArray<Boolean>(new bool[] { false, true });
-            var args = op.__DataIn__(bits);
+            var args = op.__dataIn(bits);
             var expected = new RuntimeMetadata()
             {
                 Label = "BoolArrayOp",
@@ -531,7 +531,7 @@
         {
             Qubit target = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Tests.Circuits.FooUDTOp>();
-            var args = op.__DataIn__(new Circuits.FooUDT(("bar", (target, 2.1))));
+            var args = op.__dataIn(new Circuits.FooUDT(("bar", (target, 2.1))));
             var expected = new RuntimeMetadata()
             {
                 Label = "FooUDTOp",
@@ -557,7 +557,7 @@
             IQArray<Qubit> controls = new QArray<Qubit>(new[] { new FreeQubit(0) });
             Qubit target = new FreeQubit(1);
             var op = new QuantumSimulator().Get<Intrinsic.H>().Controlled;
-            var args = op.__DataIn__((controls, target));
+            var args = op.__dataIn((controls, target));
             var expected = new RuntimeMetadata()
             {
                 Label = "H",
@@ -580,7 +580,7 @@
             IQArray<Qubit> controls = new QArray<Qubit>(new[] { new FreeQubit(0) });
             Qubit target = new FreeQubit(1);
             var op = new QuantumSimulator().Get<Intrinsic.X>().Controlled;
-            var args = op.__DataIn__((controls, target));
+            var args = op.__dataIn((controls, target));
             var expected = new RuntimeMetadata()
             {
                 Label = "X",
@@ -604,7 +604,7 @@
             Qubit control = new FreeQubit(1);
             Qubit target = new FreeQubit(2);
             var op = new QuantumSimulator().Get<Intrinsic.CNOT>().Controlled;
-            var args = op.__DataIn__((controls, (control, target)));
+            var args = op.__dataIn((controls, (control, target)));
             var expected = new RuntimeMetadata()
             {
                 Label = "X",
@@ -630,7 +630,7 @@
             Qubit target = new FreeQubit(3);
             IQArray<Qubit> controls = new QArray<Qubit>(new[] { control1 });
             var op = new QuantumSimulator().Get<Intrinsic.CCNOT>().Controlled;
-            var args = op.__DataIn__((controls, (control2, control3, target)));
+            var args = op.__dataIn((controls, (control2, control3, target)));
             var expected = new RuntimeMetadata()
             {
                 Label = "X",
@@ -655,7 +655,7 @@
         {
             Qubit target = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Intrinsic.H>().Adjoint;
-            var args = op.__DataIn__(target);
+            var args = op.__dataIn(target);
             var expected = new RuntimeMetadata()
             {
                 Label = "H",
@@ -677,7 +677,7 @@
         {
             Qubit target = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Intrinsic.X>().Adjoint;
-            var args = op.__DataIn__(target);
+            var args = op.__dataIn(target);
             var expected = new RuntimeMetadata()
             {
                 Label = "X",
@@ -699,7 +699,7 @@
         {
             Qubit target = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Intrinsic.H>().Adjoint.Adjoint;
-            var args = op.__DataIn__(target);
+            var args = op.__dataIn(target);
             var expected = new RuntimeMetadata()
             {
                 Label = "H",
@@ -723,7 +723,7 @@
             Qubit target = new FreeQubit(1);
             var op1 = new QuantumSimulator().Get<Intrinsic.H>().Controlled.Adjoint;
             var op2 = new QuantumSimulator().Get<Intrinsic.H>().Adjoint.Controlled;
-            var args = op1.__DataIn__((controls, target));
+            var args = op1.__dataIn((controls, target));
             var expected = new RuntimeMetadata()
             {
                 Label = "H",
@@ -749,7 +749,7 @@
             var op1 = new QuantumSimulator().Get<Intrinsic.H>().Controlled.Adjoint.Adjoint;
             var op2 = new QuantumSimulator().Get<Intrinsic.H>().Adjoint.Controlled.Adjoint;
             var op3 = new QuantumSimulator().Get<Intrinsic.H>().Adjoint.Adjoint.Controlled;
-            var args = op1.__DataIn__((controls, target));
+            var args = op1.__dataIn((controls, target));
             var expected = new RuntimeMetadata()
             {
                 Label = "H",
@@ -778,7 +778,7 @@
             var target = new FreeQubit(0);
             var op = new QuantumSimulator().Get<Intrinsic.Ry>().Partial((double d) =>
                 new ValueTuple<double, Qubit>(d, target));
-            var args = op.__DataIn__(2.1);
+            var args = op.__dataIn(2.1);
             var expected = new RuntimeMetadata()
             {
                 Label = "Ry",
