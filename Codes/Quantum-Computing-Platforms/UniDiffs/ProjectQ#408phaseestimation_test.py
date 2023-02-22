--- ProjectQ/ProjectQ#408/after/phaseestimation_test.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#408/before/phaseestimation_test.py	2022-01-10 16:02:54.000000000 +0000
@@ -42,9 +42,8 @@
             AutoReplacer(rule_set),
         ],
     )
-    N = 150
     results = np.array([])
-    for i in range(N):
+    for i in range(150):
         autovector = eng.allocate_qureg(1)
         X | autovector
         H | autovector
@@ -61,8 +60,8 @@
         eng.flush()
 
     num_phase = (results == 0.5).sum()
-    assert num_phase / N >= 0.35, "Statistics phase calculation are not correct (%f vs. %f)" % (
-        num_phase / N,
+    assert num_phase / 100.0 >= 0.35, "Statistics phase calculation are not correct (%f vs. %f)" % (
+        num_phase / 100.0,
         0.35,
     )
 
@@ -76,9 +75,8 @@
             AutoReplacer(rule_set),
         ],
     )
-    N = 150
     results = np.array([])
-    for i in range(N):
+    for i in range(150):
         autovector = eng.allocate_qureg(1)
         theta = cmath.pi * 2.0 * 0.125
         unit = Ph(theta)
@@ -94,8 +92,8 @@
         eng.flush()
 
     num_phase = (results == 0.125).sum()
-    assert num_phase / N >= 0.35, "Statistics phase calculation are not correct (%f vs. %f)" % (
-        num_phase / N,
+    assert num_phase / 100.0 >= 0.35, "Statistics phase calculation are not correct (%f vs. %f)" % (
+        num_phase / 100.0,
         0.35,
     )
 
@@ -115,9 +113,8 @@
             AutoReplacer(rule_set),
         ],
     )
-    N = 150
     results = np.array([])
-    for i in range(N):
+    for i in range(150):
         autovector = eng.allocate_qureg(2)
         X | autovector[0]
         ancillas = eng.allocate_qureg(3)
@@ -132,8 +129,8 @@
         eng.flush()
 
     num_phase = (results == 0.125).sum()
-    assert num_phase / N >= 0.34, "Statistics phase calculation are not correct (%f vs. %f)" % (
-        num_phase / N,
+    assert num_phase / 100.0 >= 0.34, "Statistics phase calculation are not correct (%f vs. %f)" % (
+        num_phase / 100.0,
         0.34,
     )
 
@@ -146,11 +143,10 @@
             AutoReplacer(rule_set),
         ],
     )
-    N = 100
     results = np.array([])
     results_plus = np.array([])
     results_minus = np.array([])
-    for i in range(N):
+    for i in range(100):
         autovector = eng.allocate_qureg(1)
         amplitude0 = (np.sqrt(2) + np.sqrt(6)) / 4.0
         amplitude1 = (np.sqrt(2) - np.sqrt(6)) / 4.0
@@ -178,8 +174,8 @@
         eng.flush()
 
     total = len(results_plus) + len(results_minus)
-    plus_probability = len(results_plus) / N
-    assert total == pytest.approx(N, abs=5)
+    plus_probability = len(results_plus) / 100.0
+    assert total == pytest.approx(100, abs=5)
     assert plus_probability == pytest.approx(
         1.0 / 4.0, abs=1e-1
     ), "Statistics on |+> probability are not correct (%f vs. %f)" % (
