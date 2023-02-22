--- qsharp-runtime/qsharp-runtime#349/after/StartOperationTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/StartOperationTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -141,11 +141,11 @@
                 var p1 = basic.Partial(m1);
                 var p2 = p1.Partial(m2);
 
-                AssertTuple(expected, p1.__DataIn__((q2, q3)).Value);
-                AssertTuple(expected, p2.__DataIn__((q2)).Value);
+                AssertTuple(expected, p1.__dataIn((q2, q3)).Value);
+                AssertTuple(expected, p2.__dataIn((q2)).Value);
 
-                Assert.Equal(new Qubit[] { q1, q2, q3 }, p1.__DataIn__((q2, q3)).Qubits);
-                Assert.Equal(new Qubit[] { q1, q2, q3 }, p2.__DataIn__(q2).Qubits);
+                Assert.Equal(new Qubit[] { q1, q2, q3 }, p1.__dataIn((q2, q3)).Qubits);
+                Assert.Equal(new Qubit[] { q1, q2, q3 }, p2.__dataIn(q2).Qubits);
 
                 Assert.Null(((IApplyData)basic).Qubits);
                 Assert.Equal(new Qubit[] { q1, null, null }, ((IApplyData)p1).Qubits);
@@ -169,11 +169,11 @@
                 var p1 = ((Basic)basic.Data).Partial(m1);
                 var p2 = p1.Partial(m2);
 
-                AssertTuple(expected, p1.__DataIn__((q2, q3)).Value);
-                AssertTuple(expected, p2.__DataIn__((q2)).Value);
+                AssertTuple(expected, p1.__dataIn((q2, q3)).Value);
+                AssertTuple(expected, p2.__dataIn((q2)).Value);
 
-                Assert.Equal(new Qubit[] { q1, q2, q3 }, p1.__DataIn__((q2, q3)).Qubits);
-                Assert.Equal(new Qubit[] { q1, q2, q3 }, p2.__DataIn__(q2).Qubits);
+                Assert.Equal(new Qubit[] { q1, q2, q3 }, p1.__dataIn((q2, q3)).Qubits);
+                Assert.Equal(new Qubit[] { q1, q2, q3 }, p2.__dataIn(q2).Qubits);
 
                 Assert.Null(((IApplyData)basic).Qubits);
                 Assert.Equal(new Qubit[] { q1, null, null }, ((IApplyData)p1).Qubits);
