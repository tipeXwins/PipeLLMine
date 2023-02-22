--- qsharp-runtime/qsharp-runtime#349/after/SimulationCodeTests.fs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/SimulationCodeTests.fs	2022-01-10 16:02:54.000000000 +0000
@@ -861,10 +861,10 @@
             let context  = createTestContext op
             let deps     = op   |> operationDependencies |> depsByName
             let actual   = deps |> buildInit context |> formatSyntaxTree
-            let expected = sprintf "public override void __Init__() { %s }" (String.concat "" body)
+            let expected = sprintf "public override void Init() { %s }" (String.concat "" body)
             Assert.Equal (expected |> clearFormatting, actual |> clearFormatting)
 
-        let template = sprintf "this.%s = this.__Factory__.Get<%s>(typeof(%s));"
+        let template = sprintf "this.%s = this.Factory.Get<%s>(typeof(%s));"
         [
         ]
         |> testOne emptyOperation
@@ -878,37 +878,37 @@
         |> testOne genU2
 
         [
-            template "Allocate__" "Allocate" "global::Microsoft.Quantum.Intrinsic.Allocate"
-            template "Microsoft__Quantum__Intrinsic__H" "IUnitary<Qubit>" "global::Microsoft.Quantum.Intrinsic.H"
-            template "H__" "ICallable<Qubit, QVoid>" "H"
-            template "Release__" "Release" "global::Microsoft.Quantum.Intrinsic.Release"
-            template "Microsoft__Quantum__Overrides__emptyFunction" "ICallable<QVoid, QVoid>" "global::Microsoft.Quantum.Overrides.emptyFunction"
-            template "emptyFunction__" "ICallable<QVoid, QVoid>" "emptyFunction"
+            template "Allocate"                               "Allocate"                        "global::Microsoft.Quantum.Intrinsic.Allocate"
+            template "MicrosoftQuantumIntrinsicH"             "IUnitary<Qubit>"                 "global::Microsoft.Quantum.Intrinsic.H"
+            template "H"                                      "ICallable<Qubit, QVoid>"         "H"
+            template "Release"                                "Release"                         "global::Microsoft.Quantum.Intrinsic.Release"
+            template "MicrosoftQuantumOverridesemptyFunction" "ICallable<QVoid, QVoid>"         "global::Microsoft.Quantum.Overrides.emptyFunction"
+            template "emptyFunction"                          "ICallable<QVoid, QVoid>"         "emptyFunction"
         ]
         |> testOne duplicatedDefinitionsCaller
 
         [
-            template "Allocate__" "Allocate" "global::Microsoft.Quantum.Intrinsic.Allocate"
-            template "CNOT__" "IAdjointable<(Qubit, Qubit)>" "global::Microsoft.Quantum.Intrinsic.CNOT"
-            template "Microsoft__Quantum__Testing__Hold" "ICallable" "global::Microsoft.Quantum.Testing.Hold<>"
-            template "Release__" "Release" "global::Microsoft.Quantum.Intrinsic.Release"
-            template "ResultToString__" "ICallable<Result,String>" "ResultToString"
-            template "X__" "IUnitary<Qubit>" "global::Microsoft.Quantum.Intrinsic.X"
-            template "genIter__" "IUnitary" "genIter<>"
-            template "genMapper__" "ICallable" "genMapper<,>"
-            template "genU1__" "IUnitary" "genU1<>"
-            template "Microsoft__Quantum__Testing__noOpGeneric" "IUnitary" "global::Microsoft.Quantum.Testing.noOpGeneric<>"
-            template "Microsoft__Quantum__Testing__noOpResult" "IUnitary<Result>" "global::Microsoft.Quantum.Testing.noOpResult"
+            template "Allocate"                             "Allocate"                          "global::Microsoft.Quantum.Intrinsic.Allocate"
+            template "CNOT"                                 "IAdjointable<(Qubit, Qubit)>"      "global::Microsoft.Quantum.Intrinsic.CNOT"
+            template "MicrosoftQuantumTestingHold"          "ICallable"                         "global::Microsoft.Quantum.Testing.Hold<>"
+            template "Release"                              "Release"                           "global::Microsoft.Quantum.Intrinsic.Release"
+            template "ResultToString"                       "ICallable<Result,String>"          "ResultToString"
+            template "X"                                    "IUnitary<Qubit>"                   "global::Microsoft.Quantum.Intrinsic.X"
+            template "genIter"                              "IUnitary"                          "genIter<>"
+            template "genMapper"                            "ICallable"                         "genMapper<,>"
+            template "genU1"                                "IUnitary"                          "genU1<>"
+            template "MicrosoftQuantumTestingnoOpGeneric"   "IUnitary"                          "global::Microsoft.Quantum.Testing.noOpGeneric<>"
+            template "MicrosoftQuantumTestingnoOpResult"    "IUnitary<Result>"                  "global::Microsoft.Quantum.Testing.noOpResult"
         ]
         |> testOne usesGenerics
 
         [
-            template "genericWithMultipleTypeParams__"        "ICallable"                         "genericWithMultipleTypeParams<,,>"
+            template "genericWithMultipleTypeParams"        "ICallable"                         "genericWithMultipleTypeParams<,,>"
         ]
         |> testOne callsGenericWithMultipleTypeParams
 
         [
-            template "Z__"                                    "IUnitary<Qubit>"                   "global::Microsoft.Quantum.Intrinsic.Z"
+            template "Z"                                    "IUnitary<Qubit>"                   "global::Microsoft.Quantum.Intrinsic.Z"
             "this.self = this;"
         ]
         |> testOne selfInvokingOperation
@@ -981,27 +981,27 @@
         let template = sprintf @"protected %s %s { get; set; }"
 
         [
-            template "Allocate"                     "Allocate__"
-            template "IAdjointable<(Qubit,Qubit)>"  "CNOT__"
-            template "ICallable"                    "Microsoft__Quantum__Testing__Hold"
-            template "Release"                      "Release__"
-            template "ICallable<Result, String>"    "ResultToString__"
-            template "IUnitary<Qubit>"              "X__"
-            template "IUnitary"                     "genIter__"
-            template "ICallable"                    "genMapper__"
-            template "IUnitary"                     "genU1__"
-            template "IUnitary"                     "Microsoft__Quantum__Testing__noOpGeneric"
-            template "IUnitary<Result>"             "Microsoft__Quantum__Testing__noOpResult"
+            template "Allocate"                     "Allocate"
+            template "IAdjointable<(Qubit,Qubit)>"  "CNOT"
+            template "ICallable"                    "MicrosoftQuantumTestingHold"
+            template "Release"                      "Release"
+            template "ICallable<Result, String>"    "ResultToString"
+            template "IUnitary<Qubit>"              "X"
+            template "IUnitary"                     "genIter"
+            template "ICallable"                    "genMapper"
+            template "IUnitary"                     "genU1"
+            template "IUnitary"                     "MicrosoftQuantumTestingnoOpGeneric"
+            template "IUnitary<Result>"             "MicrosoftQuantumTestingnoOpResult"
         ]
         |> testOne usesGenerics
 
         [
-            template "ICallable"                    "genericWithMultipleTypeParams__"
+            template "ICallable"                    "genericWithMultipleTypeParams"
         ]
         |> testOne callsGenericWithMultipleTypeParams
 
         [
-            template "IUnitary<Qubit>"              "Z__"
+            template "IUnitary<Qubit>"              "Z"
             template "IAdjointable<Qubit>"          "self"
         ]
         |> testOne selfInvokingOperation
@@ -1015,7 +1015,7 @@
     let ``buildOperationInfoProperty test`` () =
         let testOne (_, op) expectedCodeString =
             let context = {createTestContext op with entryPoints = ImmutableArray.Create op.FullName}
-            let (_, operationName) = findClassName op
+            let (_, operationName) = findClassName context op
             let inType   = op.Signature.ArgumentType |> roslynTypeName context
             let outType  = op.Signature.ReturnType   |> roslynTypeName context
             let codeString =
@@ -1094,37 +1094,37 @@
         |> testOne (applyVisitor zeroQubitOperation)
 
         [
-            "X__.Apply(q1);"
+            "X.Apply(q1);"
         ]
         |> testOne (applyVisitor oneQubitOperation)
 
         [
-            "X__.Adjoint.Apply(q1);"
+            "X.Adjoint.Apply(q1);"
         ]
         |> testOne (adjointVisitor oneQubitOperation)
 
         [
             "var (q2, r) = t1;        "
-            "CNOT__.Apply((q1,q2));       "
-            "R__.Apply((r,q1));           "
+            "CNOT.Apply((q1,q2));       "
+            "R.Apply((r,q1));           "
         ]
         |> testOne (applyVisitor twoQubitOperation)
         [
             "var (q2, r) = t1;        "
-            "R__.Adjoint.Apply((r,q1));"
-            "CNOT__.Adjoint.Apply((q1,q2));"
+            "R.Adjoint.Apply((r,q1));"
+            "CNOT.Adjoint.Apply((q1,q2));"
         ]
         |> testOne (adjointVisitor twoQubitOperation)
 
         [
-            "three_op1__.Apply((q1,q2));"
-            "three_op1__.Apply((q2,q1));"
-            "three_op1__.Apply((q1,q2));"
+            "three_op1.Apply((q1,q2));"
+            "three_op1.Apply((q2,q1));"
+            "three_op1.Apply((q1,q2));"
         ]
         |> testOne (applyVisitor threeQubitOperation)
 
         [
-            "Z__.Adjoint.Apply(q1);"
+            "Z.Adjoint.Apply(q1);"
             "self.Apply(q1);"
         ]
         |> testOne (adjointVisitor selfInvokingOperation)
@@ -1166,7 +1166,7 @@
         let testOne = testOneBody
 
         [
-            "X__.Apply(q1);"
+            "X.Apply(q1);"
         ]
         |> testOne (applyVisitor oneQubitOperation)
 
@@ -1180,7 +1180,7 @@
         |> testOne (applyVisitor composeImpl)
 
         [
-            "return composeImpl__.Partial((second, first, _));"
+            "return composeImpl.Partial((second, first, _));"
         ]
         |> testOne (applyVisitor compose)
 
@@ -1189,22 +1189,22 @@
     let ``usesGenerics body`` () =
         [
             "var a = (IQArray<Result>)new QArray<Result>(Result.One, Result.Zero, Result.Zero);"
-            "var s = (IQArray<String>)new QArray<String>(ResultToString__.Apply(a[0L]), ResultToString__.Apply(a[1L]));"
-            "Microsoft__Quantum__Testing__noOpResult.Apply(a[0L]);"
+            "var s = (IQArray<String>)new QArray<String>(ResultToString.Apply(a[0L]), ResultToString.Apply(a[1L]));"
+            "MicrosoftQuantumTestingnoOpResult.Apply(a[0L]);"
 
             """
             {
-                var qubits = Allocate__.Apply(3L);
+                var qubits = Allocate.Apply(3L);
 #line hidden
                 bool __arg1__ = true;
                 try
                 {
-                    var op = Microsoft__Quantum__Testing__Hold.Partial(new Func<QVoid,(ICallable,(Qubit,Qubit),QVoid)>((__arg2__) => (CNOT__, (qubits[0L], qubits[1L]), __arg2__)));
+                    var op = MicrosoftQuantumTestingHold.Partial(new Func<QVoid,(ICallable,(Qubit,Qubit),QVoid)>((__arg2__) => (CNOT, (qubits[0L], qubits[1L]), __arg2__)));
                     op.Apply(QVoid.Instance);
 
-                    Microsoft__Quantum__Testing__noOpGeneric.Apply(qubits[0L]);
-                    Microsoft__Quantum__Testing__noOpGeneric.Apply(a[0L]);
-                    genIter__.Apply((X__, qubits));
+                    MicrosoftQuantumTestingnoOpGeneric.Apply(qubits[0L]);
+                    MicrosoftQuantumTestingnoOpGeneric.Apply(a[0L]);
+                    genIter.Apply((X, qubits));
                 }
 #line hidden
                 catch
@@ -1217,17 +1217,17 @@
                 {
                     if (__arg1__)
                     {
-                        Release__.Apply(qubits);
+                        Release.Apply(qubits);
                     }
                 }
             }
             """
-            "genIter__.Apply((Microsoft__Quantum__Testing__noOpResult, a));"
+            "genIter.Apply((MicrosoftQuantumTestingnoOpResult, a));"
             """
-            genIter__.Apply((genU1__, genMapper__.Apply<IQArray<String>>((ResultToString__, a))));
+            genIter.Apply((genU1, genMapper.Apply<IQArray<String>>((ResultToString, a))));
             """
-            "genIter__.Apply((genU1__, s));"
-            "genIter__.Apply((genU1__, a));"
+            "genIter.Apply((genU1, s));"
+            "genIter.Apply((genU1, a));"
         ]
         |> testOneBody (applyVisitor usesGenerics)
 
@@ -1235,20 +1235,20 @@
     [<Fact>]
     let ``callTests body`` () =
         [
-            "var plain = new call_plain(X__);"
-            "var adj   = new call_adj(X__);"
-            "var ctr   = new call_ctr(X__);"
-            "var uni   = new call_uni(X__);"
-
-            "X__.Apply(qubits.Data[0L]);"
-            "X__.Adjoint.Apply(qubits.Data[0L]);"
-            "X__.Controlled.Apply((qubits.Data.Slice(new QRange(1L,5L)), qubits.Data[0L]));"
+            "var plain = new call_plain(X);"
+            "var adj   = new call_adj(X);"
+            "var ctr   = new call_ctr(X);"
+            "var uni   = new call_uni(X);"
+
+            "X.Apply(qubits.Data[0L]);"
+            "X.Adjoint.Apply(qubits.Data[0L]);"
+            "X.Controlled.Apply((qubits.Data.Slice(new QRange(1L,5L)), qubits.Data[0L]));"
 
-            "call_target1__.Apply((1L, X__,     X__,   X__,   X__));"
-            "call_target1__.Apply((1L, plain.Data, adj.Data, ctr.Data, uni.Data));"
+            "call_target1.Apply((1L, X,     X,   X,   X));"
+            "call_target1.Apply((1L, plain.Data, adj.Data, ctr.Data, uni.Data));"
 
-            "call_target2__.Apply((1L, (Result.Zero, X__),    (Result.Zero, X__),  (Result.Zero, X__),  (Result.Zero, X__)));"
-            "call_target2__.Apply((2L, (Result.One, plain.Data), (Result.One, adj.Data), (Result.One, ctr.Data), (Result.One, uni.Data)));"
+            "call_target2.Apply((1L, (Result.Zero, X),    (Result.Zero, X),  (Result.Zero, X),  (Result.Zero, X)));"
+            "call_target2.Apply((2L, (Result.One, plain.Data), (Result.One, adj.Data), (Result.One, ctr.Data), (Result.One, uni.Data)));"
         ]
         |> testOneBody (applyVisitor callTests)
 
@@ -1258,7 +1258,7 @@
         [
             "var q2 = q1;"
 
-            "var r = M__.Apply(q1);"
+            "var r = M.Apply(q1);"
 
             "var i = 1.1D;"
             "var iZero = 0L;"
@@ -1291,7 +1291,7 @@
             "var __arg1__ = t;"
             "var __arg2__ = t;"
 
-            "return let_f0__.Apply(n);"
+            "return let_f0.Apply(n);"
         ]
         |> testOneBody (applyVisitor letsOperations)
 
@@ -1334,7 +1334,7 @@
             """
             if ((r == Result.One))
             {
-                n = (if_f0__.Apply(QVoid.Instance) * i);
+                n = (if_f0.Apply(QVoid.Instance) * i);
             }
             """
             """
@@ -1358,7 +1358,7 @@
             }
             else
             {
-                return ((p==Pauli.PauliI)?3L:if_f0__.Apply(QVoid.Instance));
+                return ((p==Pauli.PauliI)?3L:if_f0.Apply(QVoid.Instance));
             }
             """
         ]
@@ -1382,7 +1382,7 @@
             @"foreach (var n in range)
             #line hidden
             {
-                result = ((range.End + result) + (n * -(foreach_f2__.Apply((n, 4L)))));
+                result = ((range.End + result) + (n * -(foreach_f2.Apply((n, 4L)))));
             }"
             """
             if ((result > 10L))
@@ -1420,7 +1420,7 @@
     [<Fact>]
     let ``test Length dependency`` () =
         [
-            "iter__.Apply((Length__, new QArray<IQArray<Result>>(new QArray<Result>(Result.One), new QArray<Result>(Result.Zero, Result.One))));"
+            "iter.Apply((Length, new QArray<IQArray<Result>>(new QArray<Result>(Result.One), new QArray<Result>(Result.Zero, Result.One))));"
         ]
         |> testOneBody (applyVisitor testLengthDependency)
 
@@ -1481,22 +1481,22 @@
         [
             """
             {
-                var qubits = Allocate__.Apply(i);
+                var qubits = Allocate.Apply(i);
 #line hidden
                 bool __arg1__ = true;
                 try
                 {
                     while (true)
                     {
-                        var res =  repeat_op0__.Apply(new repeat_udt0((0L, qubits)));
+                        var res =  repeat_op0.Apply(new repeat_udt0((0L, qubits)));
 
-                        if ((repeat_op1__.Apply((0L, qubits)) == Result.One))
+                        if ((repeat_op1.Apply((0L, qubits)) == Result.One))
                         {
                             break;
                         }
                         else
                         {
-                            res = repeat_op2__.Apply((3D, new repeat_udt0(((i-1L), qubits))));
+                            res = repeat_op2.Apply((3D, new repeat_udt0(((i-1L), qubits))));
                         }
                     }
                 }
@@ -1511,7 +1511,7 @@
                 {
                     if (__arg1__)
                     {
-                        Release__.Apply(qubits);
+                        Release.Apply(qubits);
                     }
                 }
             }
@@ -1524,14 +1524,14 @@
         [
             """
             {
-                var q = Allocate__.Apply();
+                var q = Allocate.Apply();
 #line hidden
                 bool __arg1__ = true;
                 try
                 {
                     var flag = true;
-                    (flag ? X__ : Z__).Apply(q);
-                    alloc_op0__.Apply(q);
+                    (flag ? X : Z).Apply(q);
+                    alloc_op0.Apply(q);
                 }
 #line hidden
                 catch
@@ -1544,18 +1544,18 @@
                 {
                     if (__arg1__)
                     {
-                        Release__.Apply(q);
+                        Release.Apply(q);
                     }
                 }
             }"""
             """
             {
-                var qs = Allocate__.Apply(n);
+                var qs = Allocate.Apply(n);
 #line hidden
                 bool __arg2__ = true;
                 try
                 {
-                    alloc_op0__.Apply(qs[(n-1L)]);
+                    alloc_op0.Apply(qs[(n-1L)]);
                 }
 #line hidden
                 catch
@@ -1568,19 +1568,19 @@
                 {
                     if (__arg2__)
                     {
-                        Release__.Apply(qs);
+                        Release.Apply(qs);
                     }
                 }
             }"""
             """
             {
-                var (q1, (q2, (__arg3__, q3, __arg4__, q4))) = (Allocate__.Apply(), ((Allocate__.Apply(), Allocate__.Apply(2L)), (Allocate__.Apply(), Allocate__.Apply(n), Allocate__.Apply((n-1L)), Allocate__.Apply(4L))));
+                var (q1, (q2, (__arg3__, q3, __arg4__, q4))) = (Allocate.Apply(), ((Allocate.Apply(), Allocate.Apply(2L)), (Allocate.Apply(), Allocate.Apply(n), Allocate.Apply((n-1L)), Allocate.Apply(4L))));
 #line hidden
                 bool __arg5__ = true;
                 try
                 {
-                    alloc_op0__.Apply(q1);
-                    alloc_op0__.Apply(q3[1L]);
+                    alloc_op0.Apply(q1);
+                    alloc_op0.Apply(q3[1L]);
                 }
 #line hidden
                 catch
@@ -1593,13 +1593,13 @@
                 {
                     if (__arg5__)
                     {
-                        Release__.Apply(q1);
-                        Release__.Apply(q2.Item1);
-                        Release__.Apply(q2.Item2);
-                        Release__.Apply(__arg3__);
-                        Release__.Apply(q3);
-                        Release__.Apply(__arg4__);
-                        Release__.Apply(q4);
+                        Release.Apply(q1);
+                        Release.Apply(q2.Item1);
+                        Release.Apply(q2.Item2);
+                        Release.Apply(__arg3__);
+                        Release.Apply(q3);
+                        Release.Apply(__arg4__);
+                        Release.Apply(q4);
                     }
                 }
             }"""
@@ -1609,12 +1609,12 @@
         [
             """
             {
-                var b = Borrow__.Apply(n);
+                var b = Borrow.Apply(n);
 #line hidden
                 bool __arg1__ = true;
                 try
                 {
-                    alloc_op0__.Apply(b[(n-1L)]);
+                    alloc_op0.Apply(b[(n-1L)]);
                 }
 #line hidden
                 catch
@@ -1627,25 +1627,25 @@
                 {
                     if (__arg1__)
                     {
-                        Return__.Apply(b);
+                        Return.Apply(b);
                     }
                 }
             }"""
             """
             {
-                var (q1, (q2, (__arg2__, q3))) = (Borrow__.Apply(), (Borrow__.Apply(2L), (Borrow__.Apply(), (Borrow__.Apply(n), Borrow__.Apply(4L)))));
+                var (q1, (q2, (__arg2__, q3))) = (Borrow.Apply(), (Borrow.Apply(2L), (Borrow.Apply(), (Borrow.Apply(n), Borrow.Apply(4L)))));
 #line hidden
                 bool __arg3__ = true;
                 try
                 {
                     {
-                        var qt = (Allocate__.Apply(), (Allocate__.Apply(1L), Allocate__.Apply(2L)));
+                        var qt = (Allocate.Apply(), (Allocate.Apply(1L), Allocate.Apply(2L)));
 #line hidden
                         bool __arg4__ = true;
                         try
                         {
                             var (qt1, qt2) = ((Qubit, (IQArray<Qubit>, IQArray<Qubit>)))qt;
-                            alloc_op0__.Apply(qt1);
+                            alloc_op0.Apply(qt1);
                         }
 #line hidden
                         catch
@@ -1658,15 +1658,15 @@
                         {
                             if (__arg4__)
                             {
-                                Release__.Apply(qt.Item1);
-                                Release__.Apply(qt.Item2.Item1);
-                                Release__.Apply(qt.Item2.Item2);
+                                Release.Apply(qt.Item1);
+                                Release.Apply(qt.Item2.Item1);
+                                Release.Apply(qt.Item2.Item2);
                             }
                         }
                     }
 
-                    alloc_op0__.Apply(q1);
-                    alloc_op0__.Apply(q2[1L]);
+                    alloc_op0.Apply(q1);
+                    alloc_op0.Apply(q2[1L]);
                 }
 #line hidden
                 catch
@@ -1679,11 +1679,11 @@
                 {
                     if (__arg3__)
                     {
-                        Return__.Apply(q1);
-                        Return__.Apply(q2);
-                        Return__.Apply(__arg2__);
-                        Return__.Apply(q3.Item1);
-                        Return__.Apply(q3.Item2);
+                        Return.Apply(q1);
+                        Return.Apply(q2);
+                        Return.Apply(__arg2__);
+                        Return.Apply(q3.Item1);
+                        Return.Apply(q3.Item2);
                     }
                 }
             }"""
@@ -1732,7 +1732,7 @@
         |> testOne randomAbstractOperation
 
         Some """
-        public override Func<QVoid,QVoid> __Body__ => (__in__) =>
+        public override Func<QVoid,QVoid> Body => (__in__) =>
         {
             #line hidden
             return QVoid.Instance;
@@ -1740,11 +1740,11 @@
         |> testOne zeroQubitOperation
 
         Some """
-        public override Func<Qubit,QVoid> __Body__ => (__in__) =>
+        public override Func<Qubit,QVoid> Body => (__in__) =>
         {
             var q1 = __in__;
 
-            X__.Apply(q1);
+            X.Apply(q1);
             #line hidden
             return  QVoid.Instance;
         };
@@ -1752,14 +1752,14 @@
         |> testOne oneQubitOperation
 
         Some """
-        public override Func<(Qubit,(Qubit,Double)), QVoid> __Body__ => (__in__) =>
+        public override Func<(Qubit,(Qubit,Double)), QVoid> Body => (__in__) =>
         {
             var (q1,t1) = __in__;
 
             var (q2,r) = t1;
 
-            CNOT__.Apply((q1, q2));
-            R__.Apply((r, q1));
+            CNOT.Apply((q1, q2));
+            R.Apply((r, q1));
 
             #line hidden
             return  QVoid.Instance;
@@ -1769,14 +1769,14 @@
 
 
         Some """
-        public override Func<(Qubit,Qubit,IQArray<Qubit>), QVoid> __Body__ => (__in__) =>
+        public override Func<(Qubit,Qubit,IQArray<Qubit>), QVoid> Body => (__in__) =>
         {
             var (q1,q2,arr1) = __in__;
 
-            da_op0__.Apply(QVoid.Instance);
-            da_op1__.Adjoint.Apply(q1);
-            da_op2__.Controlled.Apply((new QArray<Qubit>(q1), (1L, q2)));
-            da_op3__.Controlled.Adjoint.Apply((new QArray<Qubit>(q1, q2), (1.1D, Result.One, arr1.Length)));
+            da_op0.Apply(QVoid.Instance);
+            da_op1.Adjoint.Apply(q1);
+            da_op2.Controlled.Apply((new QArray<Qubit>(q1), (1L, q2)));
+            da_op3.Controlled.Adjoint.Apply((new QArray<Qubit>(q1, q2), (1.1D, Result.One, arr1.Length)));
 
             #line hidden
             return QVoid.Instance;
@@ -1796,10 +1796,10 @@
         let op4 = "IUnitary";
         let f1  = "ICallable"
         Some (sprintf """
-        public override Func<(Qubit, %s, %s, %s, (%s, %s), %s), %s> __Body__  => (__in__) =>
+        public override Func<(Qubit, %s, %s, %s, (%s, %s), %s), %s> Body  => (__in__) =>
                 {
                     var (q1, op0, op1, op2, t1, f1) = __in__;
-                    op1.Apply(OP_1__);
+                    op1.Apply(OP_1);
                     var v0 = op0;
                     var r0 = v0.Apply<Result>(q1);
                     var (op3, op4) = t1;
@@ -1863,7 +1863,7 @@
             "var s1 = (IQArray<Qubit>)qubits.Slice(new QRange(0L,10L));"
             "var s2 = (IQArray<Qubit>)qubits.Slice(r2);"
             "var s3 = (IQArray<Qubit>)qubits.Slice(ranges[3L]);"
-            "var s4 = (IQArray<Qubit>)qubits.Slice(GetMeARange__.Apply(QVoid.Instance));"
+            "var s4 = (IQArray<Qubit>)qubits.Slice(GetMeARange.Apply(QVoid.Instance));"
 
             "return qubits.Slice(new QRange(10L,-(3L),0L));"
         ]
@@ -1925,17 +1925,17 @@
         None
         |> testOne oneQubitAbstractOperation
 
-        Some "public override Func<Qubit, QVoid> __AdjointBody__ => __Body__;"
+        Some "public override Func<Qubit, QVoid> AdjointBody  => Body;"
         |> testOne oneQubitSelfAdjointAbstractOperation
 
         None
         |> testOne randomAbstractOperation
 
-        Some "public override Func<Qubit, QVoid> __AdjointBody__ => __Body__;"
+        Some "public override Func<Qubit, QVoid> AdjointBody => Body;"
         |> testOne oneQubitSelfAdjointOperation
 
         Some """
-        public override Func<QVoid, QVoid> __AdjointBody__ => (__in__) =>
+        public override Func<QVoid, QVoid> AdjointBody => (__in__) =>
         {
             #line hidden
             return QVoid.Instance;
@@ -1943,10 +1943,10 @@
         |> testOne zeroQubitOperation
 
         Some """
-        public override Func<Qubit, QVoid> __AdjointBody__ => (__in__) =>
+        public override Func<Qubit, QVoid> AdjointBody => (__in__) =>
         {
             var q1 = __in__;
-            X__.Adjoint.Apply(q1);
+            X.Adjoint.Apply(q1);
 
             #line hidden
             return QVoid.Instance;
@@ -1954,14 +1954,14 @@
         |> testOne oneQubitOperation
 
         Some """
-        public override Func<(Qubit,(Qubit,Double)), QVoid> __AdjointBody__ => (__in__) =>
+        public override Func<(Qubit,(Qubit,Double)), QVoid> AdjointBody => (__in__) =>
         {
             var (q1,t1) = __in__;
 
             var (q2,r) = t1;
 
-            R__.Adjoint.Apply((r, q1));
-            CNOT__.Adjoint.Apply((q1, q2));
+            R.Adjoint.Apply((r, q1));
+            CNOT.Adjoint.Apply((q1, q2));
 
             #line hidden
             return QVoid.Instance;
@@ -1969,19 +1969,19 @@
         |> testOne twoQubitOperation
 
         Some """
-        public override Func<(Qubit,Qubit,Qubits), QVoid> __AdjointBody__ => (__in__) =>
+        public override Func<(Qubit,Qubit,Qubits), QVoid> AdjointBody => (__in__) =>
         {
             var (q1,q2,arr1) = __in__;
-            three_op1__.Adjoint.Apply((q1, q2));
-            three_op1__.Adjoint.Apply((q2, q1));
-            three_op1__.Adjoint.Apply((q1, q2));
+            three_op1.Adjoint.Apply((q1, q2));
+            three_op1.Adjoint.Apply((q2, q1));
+            three_op1.Adjoint.Apply((q1, q2));
             #line hidden
             return QVoid.Instance;
         };"""
         |> testOne threeQubitOperation
 
 
-        Some "public override Func<__T__, QVoid> __AdjointBody__ => __Body__;"
+        Some "public override Func<__T__, QVoid> AdjointBody => Body;"
         |> testOne genAdj1
 
     [<Fact>]
@@ -1998,7 +1998,7 @@
         |> testOne randomAbstractOperation
 
         Some """
-        public override Func<(IQArray<Qubit>,QVoid), QVoid> __ControlledBody__ => (__in__) =>
+        public override Func<(IQArray<Qubit>,QVoid), QVoid> ControlledBody => (__in__) =>
         {
             var (__controlQubits__, __unitArg__) = __in__;
 
@@ -2008,11 +2008,11 @@
         |> testOne zeroQubitOperation
 
         Some """
-        public override Func<(IQArray<Qubit>,Qubit), QVoid> __ControlledBody__ => (__in__) =>
+        public override Func<(IQArray<Qubit>,Qubit), QVoid> ControlledBody => (__in__) =>
         {
             var (c, q1) = __in__;
 
-            X__.Controlled.Apply((c, q1));
+            X.Controlled.Apply((c, q1));
 
             #line hidden
             return QVoid.Instance;
@@ -2020,13 +2020,13 @@
         |> testOne oneQubitOperation
 
         Some """
-        public override Func<(IQArray<Qubit>,(Qubit,Qubit,Qubits)), QVoid> __ControlledBody__ => (__in__) =>
+        public override Func<(IQArray<Qubit>,(Qubit,Qubit,Qubits)), QVoid> ControlledBody => (__in__) =>
         {
             var (c, (q1, q2, arr1)) = __in__;
 
-            three_op1__.Controlled.Apply((c, (q1, q2)));
-            three_op1__.Controlled.Apply((c, (q2, q1)));
-            three_op1__.Controlled.Apply((c, (q1, q2)));
+            three_op1.Controlled.Apply((c, (q1, q2)));
+            three_op1.Controlled.Apply((c, (q2, q1)));
+            three_op1.Controlled.Apply((c, (q1, q2)));
 
             #line hidden
             return QVoid.Instance;
@@ -2040,14 +2040,14 @@
         None
         |> testOne oneQubitAbstractOperation
 
-        Some "public override Func<(IQArray<Qubit>,Qubit), QVoid> __ControlledAdjointBody__ => __ControlledBody__;"
+        Some "public override Func<(IQArray<Qubit>,Qubit), QVoid> ControlledAdjointBody  => ControlledBody;"
         |> testOne oneQubitSelfAdjointAbstractOperation
 
         None
         |> testOne randomAbstractOperation
 
         Some """
-        public override Func<(IQArray<Qubit>,QVoid), QVoid> __ControlledAdjointBody__ => (__in__) =>
+        public override Func<(IQArray<Qubit>,QVoid), QVoid> ControlledAdjointBody => (__in__) =>
         {
             var (__controlQubits__, __unitArg__) = __in__;
 
@@ -2057,10 +2057,10 @@
         |> testOne zeroQubitOperation
 
         Some """
-        public override Func<(IQArray<Qubit>, Qubit), QVoid> __ControlledAdjointBody__ => (__in__) =>
+        public override Func<(IQArray<Qubit>, Qubit), QVoid> ControlledAdjointBody => (__in__) =>
         {
             var (c,q1) = __in__;
-            X__.Controlled.Adjoint.Apply((c, q1));
+            X.Controlled.Adjoint.Apply((c, q1));
             #line hidden
             return QVoid.Instance;
         };"""
@@ -2068,13 +2068,13 @@
         |> testOne oneQubitOperation
 
         Some """
-        public override Func<(IQArray<Qubit>,(Qubit,Qubit,Qubits)), QVoid> __ControlledAdjointBody__ => (__in__) =>
+        public override Func<(IQArray<Qubit>,(Qubit,Qubit,Qubits)), QVoid> ControlledAdjointBody => (__in__) =>
         {
             var (c,(q1,q2,arr1)) = __in__;
 
-            three_op1__.Controlled.Adjoint.Apply((c, (q1, q2)));
-            three_op1__.Controlled.Adjoint.Apply((c, (q2, q1)));
-            three_op1__.Controlled.Adjoint.Apply((c, (q1, q2)));
+            three_op1.Controlled.Adjoint.Apply((c, (q1, q2)));
+            three_op1.Controlled.Adjoint.Apply((c, (q2, q1)));
+            three_op1.Controlled.Adjoint.Apply((c, (q1, q2)));
 
             #line hidden
             return QVoid.Instance;
@@ -2085,40 +2085,40 @@
     let ``partial application`` () =
         [
             //todo: "partial1Args.Partial<Int64>(_).Apply(1L);"
-            "partial3Args__
+            "partial3Args
                 .Partial(new Func<(Int64,Double,Result), (Int64,Double,Result)>((__arg1__) => (__arg1__.Item1, __arg1__.Item2, __arg1__.Item3)))
                 .Apply((1L, 3.5D, Result.One));"
-            "partial3Args__
+            "partial3Args
                 .Partial(new Func<Double, (Int64,Double,Result)>((__arg2__) => (1L, __arg2__, Result.Zero)))
                 .Apply(3.5D);"
-            "partial3Args__
+            "partial3Args
                 .Partial(new Func<(Int64,Result), (Int64,Double,Result)>((__arg3__) => (__arg3__.Item1, 3.5D, __arg3__.Item2)))
                 .Apply((1L, Result.Zero));"
-            "partial3Args__
+            "partial3Args
                 .Partial(new Func<Result, (Int64,Double,Result)>((__arg4__) => (1L, 3.5D, __arg4__)))
                 .Apply(Result.Zero);"
-            "partial3Args__
+            "partial3Args
                 .Partial(new Func<(Double,Result), (Int64,Double,Result)>((__arg5__) => (1L, __arg5__.Item1, __arg5__.Item2)))
                 .Apply((3.5D, Result.Zero));"
-            "partialInnerTuple__
+            "partialInnerTuple
                 .Partial(new Func<(Int64,(Double,Result)), (Int64,(Double,Result))>((__arg6__) => (__arg6__.Item1, (__arg6__.Item2.Item1, __arg6__.Item2.Item2))))
                 .Apply((1L, (3.5D, Result.One)));"
-            "partialInnerTuple__
+            "partialInnerTuple
                 .Partial(new Func<(Int64,(Double,Result)), (Int64,(Double,Result))>((__arg7__) => (__arg7__.Item1, (__arg7__.Item2.Item1, __arg7__.Item2.Item2))))
                 .Apply((1L, (3.5D, Result.Zero)));"
-            "partialInnerTuple__
+            "partialInnerTuple
                 .Partial(new Func<(Double,Result), (Int64,(Double,Result))>((__arg8__) => (1L, (__arg8__.Item1, __arg8__.Item2))))
                 .Apply((3.5D, Result.Zero));"
-            "partialInnerTuple__
+            "partialInnerTuple
                 .Partial(new Func<(Int64,Result), (Int64,(Double,Result))>((__arg9__) => (__arg9__.Item1, (3.5D, __arg9__.Item2))))
                 .Apply((1L, Result.Zero));"
-            "partialInnerTuple__
+            "partialInnerTuple
                 .Partial(new Func<(Int64,Double), (Int64,(Double,Result))>((__arg10__) => (__arg10__.Item1, (__arg10__.Item2, Result.One))))
                 .Apply((1L, 3.5D));"
-            "partialInnerTuple__
+            "partialInnerTuple
                 .Partial(new Func<Result, (Int64,(Double,Result))>((__arg11__) => (1L, (3.5D, __arg11__))))
                 .Apply(Result.One);"
-            "partialNestedArgsOp__
+            "partialNestedArgsOp
                 .Partial(new Func<((Int64,Int64,Int64),((Double,Double),(Result,Result,Result))), ((Int64,Int64,Int64),((Double,Double),(Result,Result,Result)))>((__arg12__) =>
                     (
                         (__arg12__.Item1.Item1, __arg12__.Item1.Item2, __arg12__.Item1.Item3),
@@ -2138,7 +2138,7 @@
                     )
                 ))
                 .Apply((1L, ((3.3D, 2D), Result.Zero)));"
-            "partialNestedArgsOp__
+            "partialNestedArgsOp
                 .Partial(new Func<(Int64,((Double,Double),Result)), ((Int64,Int64,Int64),((Double,Double),(Result,Result,Result)))>((__arg14__) =>
                     (
                         (1L, i, __arg14__.Item1),
@@ -2158,7 +2158,7 @@
                     )
                 ))
                 .Apply((3.3D, Result.Zero));"
-            "partialNestedArgsOp__
+            "partialNestedArgsOp
                 .Partial(new Func<(Int64,(Double,Result)), ((Int64,Int64,Int64),((Double,Double),(Result,Result,Result)))>((__arg16__) =>
                     (
                         (i, __arg16__.Item1, 1L),
@@ -2174,20 +2174,20 @@
                     )
                 ))
                 .Apply(3.3D);"
-            "partialGeneric1__
+            "partialGeneric1
                 .Partial(new Func<Int64, (Int64, Result, (Int64, Result))>((__arg18__) =>
                     (0L, Result.Zero, (__arg18__, Result.One))
                 ))
                 .Apply(1L);"
-            "partialGeneric1__
+            "partialGeneric1
                 .Partial(new Func<(Int64, Result), (Int64, Result, (Int64, Result))>((__arg19__) =>
                     (__arg19__.Item1, __arg19__.Item2, (1L, Result.One))
                 ))
                 .Apply((0L, Result.Zero));"
-            "partialGeneric1__.Partial((0L, _, (1L, _))).Apply((Result.Zero, Result.One));"
-            "partialGeneric2__.Partial((0L, Result.Zero, (_, Result.One))).Apply(1L);"
-            "partialGeneric2__.Partial((_, _, (1L, Result.One))).Apply((0L, Result.Zero));"
-            "partialGeneric2__.Partial((0L, _, (1L, _))).Apply((Result.Zero, Result.One));"
+            "partialGeneric1.Partial((0L, _, (1L, _))).Apply((Result.Zero, Result.One));"
+            "partialGeneric2.Partial((0L, Result.Zero, (_, Result.One))).Apply(1L);"
+            "partialGeneric2.Partial((_, _, (1L, Result.One))).Apply((0L, Result.Zero));"
+            "partialGeneric2.Partial((0L, _, (1L, _))).Apply((Result.Zero, Result.One));"
             "partialInput
                 .Partial(new Func<(Double,(Result,Result)), (Int64,(Double,Double),(Result,Result,Result))>((__arg20__) =>
                     (
@@ -2202,7 +2202,7 @@
                 .Partial(new Func<IQArray<Qubit>, (Double,ICallable,IQArray<Qubit>)>((__arg21__) =>
                 (
                     1.1D,
-                    partialFunction__.Partial(new Func<(Int64,Double), (Int64,Double,Pauli)>((__arg22__) =>
+                    partialFunction.Partial(new Func<(Int64,Double), (Int64,Double,Pauli)>((__arg22__) =>
                         (
                             __arg22__.Item1,
                             __arg22__.Item2,
@@ -2216,10 +2216,10 @@
         |> testOneBody (applyVisitor partialApplicationTest)
 
         [
-            "var r1 = partialFunction__
+            "var r1 = partialFunction
                 .Partial(new Func<(Int64,Double,Pauli), (Int64,Double,Pauli)>((__arg1__) => (__arg1__.Item1, __arg1__.Item2, __arg1__.Item3)))
                 .Apply<Result>((2L, 2.2D, Pauli.PauliY));"
-            "var r2 = partialFunction__
+            "var r2 = partialFunction
                 .Partial(new Func<(Double,Pauli), (Int64,Double,Pauli)>((__arg2__) => (1L, __arg2__.Item1, __arg2__.Item2)))
                 .Partial(new Func<Pauli, (Double,Pauli)>((__arg3__) => (3.3D, __arg3__)))
                 .Apply<Result>(Pauli.PauliZ);"
@@ -2234,7 +2234,7 @@
     let ``buildRun test`` () =
         let testOne (_,op) expected =
             let context = createTestContext op
-            let _, nonGenericName = findClassName op
+            let (name, nonGenericName) = findClassName context op
             let actual = buildRun context nonGenericName op.ArgumentTuple op.Signature.ArgumentType op.Signature.ReturnType |> formatSyntaxTree
             Assert.Equal(expected |> clearFormatting, actual |> clearFormatting)
 
@@ -2357,10 +2357,10 @@
 
         public static HoneywellEntryPointInfo<QVoid, QVoid> Info => new HoneywellEntryPointInfo<QVoid, QVoid>(typeof(emptyOperation));
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__(QVoid data) => data;
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__)
         {
             return __m__.Run<emptyOperation, QVoid, QVoid>(QVoid.Instance);
@@ -2396,10 +2396,10 @@
 
         public static IonQEntryPointInfo<(Qubit, Basis, (Pauli, IQArray<IQArray<Double>>, Boolean), Int64), QVoid> Info => new IonQEntryPointInfo<(Qubit, Basis, (Pauli, IQArray<IQArray<Double>>, Boolean), Int64), QVoid>(typeof(randomAbstractOperation));
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__((Qubit,Basis,(Pauli,IQArray<IQArray<Double>>,Boolean),Int64) data) => new In(data);
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn((Qubit,Basis,(Pauli,IQArray<IQArray<Double>>,Boolean),Int64) data) => new In(data);
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__, Qubit q1, Basis b, (Pauli,IQArray<IQArray<Double>>,Boolean) t, Int64 i)
         {
             return __m__.Run<randomAbstractOperation, (Qubit,Basis,(Pauli,IQArray<IQArray<Double>>,Boolean),Int64), QVoid>((q1, b, t, i));
@@ -2424,52 +2424,52 @@
 
         public static QCIEntryPointInfo<Qubit, QVoid> Info => new QCIEntryPointInfo<Qubit, QVoid>(typeof(oneQubitOperation));
 
-        protected IUnitary<Qubit> X__ { get; set; }
+        protected IUnitary<Qubit> X { get; set; }
 
-        public override Func<Qubit, QVoid> __Body__ => (__in__) =>
+        public override Func<Qubit, QVoid> Body => (__in__) =>
         {
             var q1 = __in__;
-            X__.Apply(q1);
+            X.Apply(q1);
 #line hidden
             return QVoid.Instance;
         }
 
         ;
-        public override Func<Qubit, QVoid> __AdjointBody__ => (__in__) =>
+        public override Func<Qubit, QVoid> AdjointBody => (__in__) =>
         {
             var q1 = __in__;
-            X__.Adjoint.Apply(q1);
+            X.Adjoint.Apply(q1);
 #line hidden
             return QVoid.Instance;
         }
 
         ;
-        public override Func<(IQArray<Qubit>,Qubit), QVoid> __ControlledBody__ => (__in__) =>
+        public override Func<(IQArray<Qubit>,Qubit), QVoid> ControlledBody => (__in__) =>
         {
             var (c,q1) = __in__;
-            X__.Controlled.Apply((c, q1));
+            X.Controlled.Apply((c, q1));
 #line hidden
             return QVoid.Instance;
         }
 
         ;
-        public override Func<(IQArray<Qubit>,Qubit), QVoid> __ControlledAdjointBody__ => (__in__) =>
+        public override Func<(IQArray<Qubit>,Qubit), QVoid> ControlledAdjointBody => (__in__) =>
         {
             var (c,q1) = __in__;
-            X__.Controlled.Adjoint.Apply((c, q1));
+            X.Controlled.Adjoint.Apply((c, q1));
 #line hidden
             return QVoid.Instance;
         }
 
         ;
 
-        public override void __Init__()
+        public override void Init()
         {
-            this.X__ = this.__Factory__.Get<IUnitary<Qubit>>(typeof(global::Microsoft.Quantum.Intrinsic.X));
+            this.X = this.Factory.Get<IUnitary<Qubit>>(typeof(global::Microsoft.Quantum.Intrinsic.X));
         }
 
-        public override IApplyData __DataIn__(Qubit data) => data;
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn(Qubit data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__, Qubit q1)
         {
             return __m__.Run<oneQubitOperation, Qubit, QVoid>(q1);
@@ -2510,10 +2510,10 @@
 
         public static HoneywellEntryPointInfo<(__X__, (Int64, (__Y__, __Z__), Result)), QVoid> Info => new HoneywellEntryPointInfo<(__X__, (Int64, (__Y__, __Z__), Result)), QVoid>(typeof(genCtrl3<__X__,__Y__,__Z__>));
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__((__X__,(Int64,(__Y__,__Z__),Result)) data) => new In(data);
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn((__X__,(Int64,(__Y__,__Z__),Result)) data) => new In(data);
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__, __X__ arg1, (Int64,(__Y__,__Z__),Result) arg2)
         {
             return __m__.Run<genCtrl3<__X__,__Y__,__Z__>, (__X__,(Int64,(__Y__,__Z__),Result)), QVoid>((arg1, arg2));
@@ -2551,7 +2551,7 @@
 
         public static IonQEntryPointInfo<(ICallable, ICallable, __B__), QVoid> Info => new IonQEntryPointInfo<(ICallable, ICallable, __B__), QVoid>(typeof(composeImpl<__A__,__B__>));
 
-        public override Func<(ICallable,ICallable,__B__), QVoid> __Body__ => (__in__) =>
+        public override Func<(ICallable,ICallable,__B__), QVoid> Body => (__in__) =>
         {
             var (second,first,arg) = __in__;
             second.Apply(first.Apply<__A__>(arg));
@@ -2559,10 +2559,10 @@
             return QVoid.Instance;
         };
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__((ICallable,ICallable,__B__) data) => new In(data);
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn((ICallable,ICallable,__B__) data) => new In(data);
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__, ICallable second, ICallable first, __B__ arg)
         {
             return __m__.Run<composeImpl<__A__,__B__>, (ICallable,ICallable,__B__), QVoid>((second, first, arg));
@@ -2585,10 +2585,10 @@
 
         public static QCIEntryPointInfo<__A__, QVoid> Info => new QCIEntryPointInfo<__A__, QVoid>(typeof(genF1<__A__>));
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__(__A__ data) => new QTuple<__A__>(data);
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn(__A__ data) => new QTuple<__A__>(data);
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__, __A__ arg)
         {
             return __m__.Run<genF1<__A__>, __A__, QVoid>(arg);
@@ -2611,19 +2611,19 @@
         String ICallable.FullName => "Microsoft.Quantum.Compiler.Generics.EmptyInternalFunction";
         public static EntryPointInfo<QVoid, QVoid> Info => new EntryPointInfo<QVoid, QVoid>(typeof(EmptyInternalFunction));
 
-        public override Func<QVoid, QVoid> __Body__ => (__in__) =>
+        public override Func<QVoid, QVoid> Body => (__in__) =>
         {
 #line hidden
             return QVoid.Instance;
         };
 
-        public override void __Init__()
+        public override void Init()
         {
         }
 
-        public override IApplyData __DataIn__(QVoid data) => data;
+        public override IApplyData __dataIn(QVoid data) => data;
 
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
 
     public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__)
     {
@@ -2645,19 +2645,19 @@
         String ICallable.FullName => "Microsoft.Quantum.Compiler.Generics.EmptyInternalOperation";
         public static EntryPointInfo<QVoid, QVoid> Info => new EntryPointInfo<QVoid, QVoid>(typeof(EmptyInternalOperation));
 
-        public override Func<QVoid, QVoid> __Body__ => (__in__) =>
+        public override Func<QVoid, QVoid> Body => (__in__) =>
         {
     #line hidden
             return QVoid.Instance;
         };
 
-        public override void __Init__()
+        public override void Init()
         {
         }
 
-        public override IApplyData __DataIn__(QVoid data) => data;
+        public override IApplyData __dataIn(QVoid data) => data;
 
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
 
     public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__)
     {
@@ -2671,17 +2671,17 @@
     [<Fact>]
     let ``duplicatedDefinitionsCaller body`` () =
         [
-            "emptyFunction__.Apply(QVoid.Instance);"
-            "Microsoft__Quantum__Overrides__emptyFunction.Apply(QVoid.Instance);"
+            "emptyFunction.Apply(QVoid.Instance);"
+            "MicrosoftQuantumOverridesemptyFunction.Apply(QVoid.Instance);"
             """
             {
-                var qubits = Allocate__.Apply(1L);
+                var qubits = Allocate.Apply(1L);
 #line hidden
                 bool __arg1__ = true;
                 try
                 {
-                    H__.Apply(qubits[0L]);
-                    Microsoft__Quantum__Intrinsic__H.Apply(qubits[0L]);
+                    H.Apply(qubits[0L]);
+                    MicrosoftQuantumIntrinsicH.Apply(qubits[0L]);
                 }
 #line hidden
                 catch
@@ -2694,7 +2694,7 @@
                 {
                     if (__arg1__)
                     {
-                        Release__.Apply(qubits);
+                        Release.Apply(qubits);
                     }
                 }
             }"""
@@ -2709,12 +2709,12 @@
 
         let expected =
             [
-                template "Allocate"                "Allocate__"
-                template "IUnitary<Qubit>"         "Microsoft__Quantum__Intrinsic__H"
-                template "ICallable<Qubit, QVoid>" "H__"
-                template "Release"                 "Release__"
-                template "ICallable<QVoid, QVoid>" "Microsoft__Quantum__Overrides__emptyFunction"
-                template "ICallable<QVoid, QVoid>" "emptyFunction__"
+                template "Allocate"                "Allocate"
+                template "IUnitary<Qubit>"         "MicrosoftQuantumIntrinsicH"
+                template "ICallable<Qubit, QVoid>" "H"
+                template "Release"                 "Release"
+                template "ICallable<QVoid, QVoid>" "MicrosoftQuantumOverridesemptyFunction"
+                template "ICallable<QVoid, QVoid>" "emptyFunction"
             ]
 
         let (_,op) = duplicatedDefinitionsCaller
@@ -2730,7 +2730,7 @@
 
     [<Fact>]
     let ``buildOpsProperties - internal callables`` () =
-        let property = sprintf "private protected %s %s__ { get; set; }"
+        let property = sprintf "private protected %s %s { get; set; }"
         let expected =
             [
                 property "ICallable<QVoid, QVoid>" "EmptyInternalFunction"
@@ -2762,17 +2762,17 @@
         String ICallable.FullName => "Microsoft.Quantum.Compiler.Generics.UpdateUdtItems";
         public static EntryPointInfo<MyType2, MyType2> Info => new EntryPointInfo<MyType2, MyType2>(typeof(UpdateUdtItems));
 
-        public override Func<MyType2, MyType2> __Body__ => (__in__) =>
+        public override Func<MyType2, MyType2> Body => (__in__) =>
         {
             var udt = __in__;
             vararr=QArray<Int64>.Create(10L);
             return new MyType2((1L,udt.Data.Item2,(arr?.Copy(),udt.Data.Item3.Item2)));
         };
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__(MyType2data) => data;
-        public override IApplyData __DataOut__(MyType2data) => data;
+        public override IApplyData __dataIn(MyType2data) => data;
+        public override IApplyData __dataOut(MyType2data) => data;
         public static System.Threading.Tasks.Task<MyType2> Run(IOperationFactory __m__, MyType2 udt)
         {
             return __m__.Run<UpdateUdtItems,MyType2,MyType2>(udt);
@@ -2793,10 +2793,10 @@
         String ICallable.FullName => "Microsoft.Quantum.Overrides.emptyFunction";
         public static EntryPointInfo<QVoid, QVoid> Info => new EntryPointInfo<QVoid, QVoid>(typeof(emptyFunction));
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__(QVoid data) => data;
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__)
         {
             return __m__.Run<emptyFunction, QVoid, QVoid>(QVoid.Instance);
@@ -2817,15 +2817,15 @@
         String ICallable.FullName => "Microsoft.Quantum.Testing.intFunction";
         public static EntryPointInfo<QVoid, Int64> Info => new EntryPointInfo<QVoid, Int64>(typeof(intFunction));
 
-        public override Func<QVoid, Int64> __Body__ => (__in__) =>
+        public override Func<QVoid, Int64> Body => (__in__) =>
         {
             return 1L;
         };
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__(QVoid data) => data;
-        public override IApplyData __DataOut__(Int64 data) => new QTuple<Int64>(data);
+        public override IApplyData __dataIn(QVoid data) => data;
+        public override IApplyData __dataOut(Int64 data) => new QTuple<Int64>(data);
         public static System.Threading.Tasks.Task<Int64> Run(IOperationFactory __m__)
         {
             return __m__.Run<intFunction, QVoid, Int64>(QVoid.Instance);
@@ -2855,16 +2855,16 @@
         String ICallable.FullName => "Microsoft.Quantum.Testing.powFunction";
         public static EntryPointInfo<(Int64, Int64), Int64> Info => new EntryPointInfo<(Int64, Int64), Int64>(typeof(powFunction));
 
-        public override Func<(Int64,Int64), Int64> __Body__ => (__in__) =>
+        public override Func<(Int64,Int64), Int64> Body => (__in__) =>
         {
             var (x,y) = __in__;
             return x.Pow(y);
         };
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__((Int64,Int64) data) => new In(data);
-        public override IApplyData __DataOut__(Int64 data) => new QTuple<Int64>(data);
+        public override IApplyData __dataIn((Int64,Int64) data) => new In(data);
+        public override IApplyData __dataOut(Int64 data) => new QTuple<Int64>(data);
         public static System.Threading.Tasks.Task<Int64> Run(IOperationFactory __m__, Int64 x, Int64 y)
         {
             return __m__.Run<powFunction, (Int64,Int64), Int64>((x, y));
@@ -2894,16 +2894,16 @@
         String ICallable.FullName => "Microsoft.Quantum.Testing.bigPowFunction";
         public static EntryPointInfo<(System.Numerics.BigInteger, Int64), System.Numerics.BigInteger> Info => new EntryPointInfo<(System.Numerics.BigInteger, Int64), System.Numerics.BigInteger>(typeof(bigPowFunction));
 
-        public override Func<(System.Numerics.BigInteger,Int64), System.Numerics.BigInteger> __Body__ => (__in__) =>
+        public override Func<(System.Numerics.BigInteger,Int64), System.Numerics.BigInteger> Body => (__in__) =>
         {
             var (x,y) = __in__;
             return x.Pow(y);
         };
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__((System.Numerics.BigInteger,Int64) data) => new In(data);
-        public override IApplyData __DataOut__(System.Numerics.BigInteger data) => new QTuple<System.Numerics.BigInteger>(data);
+        public override IApplyData __dataIn((System.Numerics.BigInteger,Int64) data) => new In(data);
+        public override IApplyData __dataOut(System.Numerics.BigInteger data) => new QTuple<System.Numerics.BigInteger>(data);
         public static System.Threading.Tasks.Task<System.Numerics.BigInteger> Run(IOperationFactory __m__, System.Numerics.BigInteger x, Int64 y)
         {
             return __m__.Run<bigPowFunction, (System.Numerics.BigInteger,Int64), System.Numerics.BigInteger>((x, y));
@@ -3277,9 +3277,9 @@
 
         String ICallable.Name => "emptyFunction";
         String ICallable.FullName => "Microsoft.Quantum.emptyFunction";
-        public override void __Init__() { }
-        public override IApplyData __DataIn__(Pair data) => data;
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override void Init() { }
+        public override IApplyData __dataIn(Pair data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__, Pair p)
         {
             return __m__.Run<emptyFunction, Pair, QVoid>(p);
@@ -3294,9 +3294,9 @@
 
         String ICallable.Name => "emptyOperation";
         String ICallable.FullName => "Microsoft.Quantum.emptyOperation";
-        public override void __Init__() { }
-        public override IApplyData __DataIn__(QVoid data) => data;
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override void Init() { }
+        public override IApplyData __dataIn(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__)
         {
             return __m__.Run<emptyOperation, QVoid, QVoid>(QVoid.Instance);
@@ -3432,7 +3432,7 @@
 
         String ICallable.Name => "HelloWorld";
         String ICallable.FullName => "Microsoft.Quantum.Tests.Inline.HelloWorld";
-        public override Func<Int64, Int64> __Body__ => (__in__) =>
+        public override Func<Int64, Int64> Body => (__in__) =>
         {
             var n = __in__;
 #line 9 "%%"
@@ -3441,10 +3441,10 @@
             return r;
         };
 
-        public override void __Init__() { }
+        public override void Init() { }
 
-        public override IApplyData __DataIn__(Int64 data) => new QTuple<Int64>(data);
-        public override IApplyData __DataOut__(Int64 data) => new QTuple<Int64>(data);
+        public override IApplyData __dataIn(Int64 data) => new QTuple<Int64>(data);
+        public override IApplyData __dataOut(Int64 data) => new QTuple<Int64>(data);
         public static System.Threading.Tasks.Task<Int64> Run(IOperationFactory __m__, Int64 n)
         {
             return __m__.Run<HelloWorld, Int64, Int64>(n);
@@ -3489,25 +3489,25 @@
 
         String ICallable.Name => "TestLineInBlocks";
         String ICallable.FullName => "Microsoft.Quantum.Tests.LineNumbers.TestLineInBlocks";
-        protected Allocate Allocate__
+        protected Allocate Allocate
         {
             get;
             set;
         }
 
-        protected Release Release__
+        protected Release Release
         {
             get;
             set;
         }
 
-        protected IUnitary<Qubit> X__
+        protected IUnitary<Qubit> X
         {
             get;
             set;
         }
 
-        public override Func<Int64, Result> __Body__ => (__in__) =>
+        public override Func<Int64, Result> Body => (__in__) =>
         {
             var n = __in__;
 #line 11 "%%"
@@ -3515,7 +3515,7 @@
 #line hidden
             {
 #line 13 "%%"
-                var (ctrls,q) = (Allocate__.Apply(r), Allocate__.Apply());
+                var (ctrls,q) = (Allocate.Apply(r), Allocate.Apply());
 #line hidden
                 bool __arg1__ = true;
                 try
@@ -3524,7 +3524,7 @@
                     if ((n == 0L))
                     {
 #line 16 "%%"
-                        X__.Apply(q);
+                        X.Apply(q);
                     }
                     else
                     {
@@ -3533,7 +3533,7 @@
 #line hidden
                         {
 #line 21 "%%"
-                            X__.Controlled.Apply((new QArray<Qubit>(c), q));
+                            X.Controlled.Apply((new QArray<Qubit>(c), q));
                         }
                     }
                 }
@@ -3549,9 +3549,9 @@
                     if (__arg1__)
                     {
 #line hidden
-                        Release__.Apply(ctrls);
+                        Release.Apply(ctrls);
 #line hidden
-                        Release__.Apply(q);
+                        Release.Apply(q);
                     }
                 }
             }
@@ -3561,15 +3561,15 @@
         }
 
         ;
-        public override void __Init__()
+        public override void Init()
         {
-            this.Allocate__ = this.__Factory__.Get<Allocate>(typeof(global::Microsoft.Quantum.Intrinsic.Allocate));
-            this.Release__ = this.__Factory__.Get<Release>(typeof(global::Microsoft.Quantum.Intrinsic.Release));
-            this.X__ = this.__Factory__.Get<IUnitary<Qubit>>(typeof(global::Microsoft.Quantum.Intrinsic.X));
+            this.Allocate = this.Factory.Get<Allocate>(typeof(global::Microsoft.Quantum.Intrinsic.Allocate));
+            this.Release = this.Factory.Get<Release>(typeof(global::Microsoft.Quantum.Intrinsic.Release));
+            this.X = this.Factory.Get<IUnitary<Qubit>>(typeof(global::Microsoft.Quantum.Intrinsic.X));
         }
 
-        public override IApplyData __DataIn__(Int64 data) => new QTuple<Int64>(data);
-        public override IApplyData __DataOut__(Result data) => new QTuple<Result>(data);
+        public override IApplyData __dataIn(Int64 data) => new QTuple<Int64>(data);
+        public override IApplyData __dataOut(Result data) => new QTuple<Result>(data);
         public static System.Threading.Tasks.Task<Result> Run(IOperationFactory __m__, Int64 n)
         {
             return __m__.Run<TestLineInBlocks, Int64, Result>(n);
@@ -3728,19 +3728,19 @@
         String ICallable.Name => "UnitTest1";
         String ICallable.FullName => "Microsoft.Quantum.Tests.UnitTests.UnitTest1";
 
-        public override Func<QVoid, QVoid> __Body__ => (__in__) =>
+        public override Func<QVoid, QVoid> Body => (__in__) =>
         {
         #line hidden
             return QVoid.Instance;
         }
 
         ;
-        public override void __Init__()
+        public override void Init()
         {
         }
 
-        public override IApplyData __DataIn__(QVoid data) => data;
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__)
         {
             return __m__.Run<UnitTest1, QVoid, QVoid>(QVoid.Instance);
@@ -3789,19 +3789,19 @@
         String ICallable.Name => "UnitTest2";
         String ICallable.FullName => "Microsoft.Quantum.Tests.UnitTests.UnitTest2";
 
-        public override Func<QVoid, QVoid> __Body__ => (__in__) =>
+        public override Func<QVoid, QVoid> Body => (__in__) =>
         {
         #line hidden
             return QVoid.Instance;
         }
 
         ;
-        public override void __Init__()
+        public override void Init()
         {
         }
 
-        public override IApplyData __DataIn__(QVoid data) => data;
-        public override IApplyData __DataOut__(QVoid data) => data;
+        public override IApplyData __dataIn(QVoid data) => data;
+        public override IApplyData __dataOut(QVoid data) => data;
         public static System.Threading.Tasks.Task<QVoid> Run(IOperationFactory __m__)
         {
             return __m__.Run<UnitTest2, QVoid, QVoid>(QVoid.Instance);
