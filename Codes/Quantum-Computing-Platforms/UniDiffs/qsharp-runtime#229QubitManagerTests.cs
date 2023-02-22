--- qsharp-runtime/qsharp-runtime#229/after/QubitManagerTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#229/before/QubitManagerTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -123,27 +123,16 @@
                 Assert.True(n_q.Length == 0);
             }
 
+            // Test allocating qubits over capacity
+            OperationsTestHelper.IgnoreDebugAssert(() =>
             {
-                QubitManager qm_small = new QubitManager(2);
                 IQArray<Qubit> n_q;
-                Assert.Throws<NotEnoughQubits>(() => n_q = qm_small.Allocate(5));
-            }
-            {
-                QubitManager qm_small = new QubitManager(2);
-                IQArray<Qubit> n_q;
-                Assert.Throws<NotEnoughQubits>(() => n_q = qm_small.Borrow(5, null));
-            }
 
-            {
-                QubitManager qm_small = new QubitManager(20);
-                IQArray<Qubit> n_q;
-                Assert.Throws<ArgumentException>(() => n_q = qm_small.Allocate(-2));
-            }
-            {
-                QubitManager qm_small = new QubitManager(20);
-                IQArray<Qubit> n_q;
-                Assert.Throws<ArgumentException>(() => n_q = qm_small.Borrow(-2, null));
-            }
+                Assert.Throws<NotEnoughQubits>(() => n_q = qm.Allocate(10));
+                Assert.Throws<NotEnoughQubits>(() => n_q = qm.Borrow(25, exclusion));
+                Assert.Throws<ArgumentException>(() => n_q = qm.Allocate(-2));
+                Assert.Throws<ArgumentException>(() => n_q = qm.Borrow(-2, exclusion));
+            });
         }
 
         /// <summary>
