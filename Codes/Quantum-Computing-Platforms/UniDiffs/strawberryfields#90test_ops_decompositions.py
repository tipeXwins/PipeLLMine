--- strawberryfields/strawberryfields#90/after/test_ops_decompositions.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#90/before/test_ops_decompositions.py	2022-01-10 16:02:54.000000000 +0000
@@ -275,6 +275,7 @@
         assert np.allclose(ratio, np.ones([n, n]), atol=tol, rtol=0)
 
 
+@pytest.mark.broken('FIXME hbar issue')
 class TestGaussianTransform:
     """Tests for the GaussianTransform quantum operation"""
 
@@ -284,20 +285,32 @@
         S1 = random_symplectic(n)
         S2 = random_symplectic(n)
 
-        G1 = ops.GaussianTransform(S1)
-        G1inv = ops.GaussianTransform(np.linalg.inv(S1))
-        G2 = ops.GaussianTransform(S2)
+        G1 = ops.GaussianTransform(S1, hbar=hbar)
+        G1inv = ops.GaussianTransform(np.linalg.inv(S1), hbar=hbar)
+        G2 = ops.GaussianTransform(S2, hbar=hbar)
 
         # a symplectic merged with its inverse is identity
         assert G1.merge(G1inv) is None
 
         # two merged symplectics are the same as their product
         assert np.allclose(G1.merge(G2).p[0].x, S2 @ S1, atol=tol, rtol=0)
+    def test_setting_hbar(self, hbar):
+        prog = sf.Program(3, hbar=hbar)
+        S1 = random_symplectic(3, passive=False)
+        with pytest.raises(ValueError, match="specify the hbar keyword argument"):
+            ops.GaussianTransform(S1)
+        G = ops.GaussianTransform(S1, hbar=hbar)
+        assert G.hbar == hbar
+        with eng:
+            G = ops.GaussianTransform(S1)
+        assert G.hbar == hbar
 
     def test_passive(self, tol):
         """Test that a passive decomposition is correctly flagged as requiring
         only a single interferometer"""
-        G = ops.GaussianTransform(np.identity(6))
+        prog = sf.Program(3)
+        with eng:
+            G = ops.GaussianTransform(np.identity(6))
 
         assert not G.active
         assert hasattr(G, "U1")
@@ -307,8 +320,10 @@
     def test_active(self, tol):
         """Test that an active decomposition is correctly flagged as requiring
         two interferometers and squeezing"""
+        prog = sf.Program(3)
         S1 = random_symplectic(3, passive=False)
-        G = ops.GaussianTransform(S1)
+        with eng:
+            G = ops.GaussianTransform(S1)
 
         assert G.active
         assert hasattr(G, "U1")
@@ -329,9 +344,10 @@
         U1 = X1 + 1j * P1
         U2 = X2 + 1j * P2
 
-        prog = sf.Program(n)
-        G = ops.GaussianTransform(S)
-        cmds = G.decompose(prog.register)
+        prog = sf.Program(n, hbar=hbar)
+        with eng:
+            G = ops.GaussianTransform(S)
+            cmds = G.decompose(q)
 
         assert np.all(U1 == G.U1)
         assert np.all(U2 == G.U2)
@@ -361,7 +377,7 @@
 
         # the resulting covariance state
         cov = S @ S.T
-        assert np.allclose(cov, S @ S.T, atol=tol, rtol=0)
+        assert np.allclose(cov, S @ S.T * hbar / 2, atol=tol, rtol=0)
 
     def test_decomposition_passive(self, hbar, tol):
         """Test that a passive symplectic is correctly decomposed into an interferometer"""
@@ -371,9 +387,10 @@
         P1 = S[n:, :n]
         U1 = X1 + 1j * P1
 
-        prog = sf.Program(n)
-        G = ops.GaussianTransform(S)
-        cmds = G.decompose(prog.register)
+        prog = sf.Program(n, hbar=hbar)
+        with eng:
+            G = ops.GaussianTransform(S)
+            cmds = G.decompose(q)
 
         S = np.identity(2 * n)
 
@@ -396,7 +413,7 @@
 
         # the resulting covariance state
         cov = S @ S.T
-        assert np.allclose(cov, S @ S.T, atol=tol, rtol=0)
+        assert np.allclose(cov, S @ S.T * hbar / 2, atol=tol, rtol=0)
 
     def test_active_on_vacuum(self, hbar, tol):
         """Test that an active symplectic applied to a vacuum is
@@ -413,9 +430,10 @@
         U1 = X1 + 1j * P1
         U2 = X2 + 1j * P2
 
-        prog = sf.Program(n)
-        G = ops.GaussianTransform(S, vacuum=True)
-        cmds = G.decompose(prog.register)
+        prog = sf.Program(n, hbar=hbar)
+        with eng:
+            G = ops.GaussianTransform(S, vacuum=True)
+            cmds = G.decompose(q)
 
         S = np.identity(2 * n)
 
@@ -442,39 +460,54 @@
         # the resulting covariance state
         cov = S @ S.T
 
-        assert np.allclose(cov, S @ S.T, atol=tol, rtol=0)
+        assert np.allclose(cov, S @ S.T * hbar / 2, atol=tol, rtol=0)
 
 
+@pytest.mark.broken('FIXME hbar issue')
 class TestGaussian:
     """Tests for the Gaussian quantum state preparation"""
 
     def test_merge(self, hbar, tol):
-        """Test that merging two Preparations only keeps the latter one."""
+        """Test that two covariances matrices overwrite each other on merge"""
         n = 3
         V1 = random_covariance(n, pure=False, hbar=hbar)
         V2 = random_covariance(n, pure=True, hbar=hbar)
-        r1 = np.random.randn(2*n)
-        r2 = np.random.randn(2*n)
 
-        G1 = ops.Gaussian(V1, r1)
-        G2 = ops.Gaussian(V2, r2)
+        cov1 = ops.Gaussian(V1, hbar=hbar)
+        cov2 = ops.Gaussian(V2, hbar=hbar)
 
-        assert G1.merge(G2) is G2
+        assert cov1.merge(cov2) == cov2
 
-        S = ops.Squeezed(2)
-        assert S.merge(G2) is G2
-        assert G2.merge(S) is S
+        assert ops.Squeezed(2).merge(cov2) == cov2
+
+    def test_setting_hbar(self, hbar):
+        prog = sf.Program(3, hbar=hbar)
+        cov = random_covariance(3, hbar=hbar)
+        with pytest.raises(ValueError, match="specify the hbar keyword argument"):
+            ops.Gaussian(cov)
+        G = ops.Gaussian(cov, hbar=hbar)
+        assert G.hbar == hbar
+        with eng:
+            G = ops.Gaussian(cov)
+        assert G.hbar == hbar
 
     def test_incorrect_means_length(self, hbar):
         """Test that an exception is raised len(means)!=len(cov)"""
         cov = random_covariance(3, hbar=hbar)
 
         with pytest.raises(ValueError, match="must have the same length"):
-            ops.Gaussian(cov, r=np.array([0]))
+            ops.Gaussian(cov, r=np.array([0]), hbar=hbar)
+    def test_apply_decomp(self, hbar):
+        prog = sf.Program(3, hbar=hbar)
+        cov = random_covariance(3, hbar=hbar)
+        with eng:
+            G = ops.Gaussian(cov, decomp=True)
+        with pytest.raises(NotImplementedError):
+            G._apply(q, None)
 
     def test_apply_decomp(self, hbar):
         """Test that the apply method, when decomp = False, calls the Backend directly."""
-        prog = sf.Program(3)
+        prog = sf.Program(3, hbar=hbar)
         cov = random_covariance(3, hbar=hbar)
 
         class DummyBackend:
@@ -484,18 +517,20 @@
                 """Raises a syntax error when called"""
                 raise SyntaxError
 
-        G = ops.Gaussian(cov, decomp=False)
+        with eng:
+            G = ops.Gaussian(cov, decomp=False)
         with pytest.raises(SyntaxError):
-            G._apply(prog.register, DummyBackend())
+            G._apply(q, DummyBackend())
 
     def test_decomposition(self, hbar, tol):
         """Test that an arbitrary decomposition provides the right covariance matrix"""
         n = 3
-        prog = sf.Program(n)
+        prog = sf.Program(n, hbar=hbar)
         cov = random_covariance(n)
 
-        G = ops.Gaussian(cov)
-        cmds = G.decompose(prog.register)
+        with eng:
+            G = ops.Gaussian(cov)
+            cmds = G.decompose(q)
 
         S = np.identity(2 * n)
         cov_init = np.identity(2 * n) * hbar / 2
@@ -503,7 +538,7 @@
         # calculating the resulting decomposed symplectic
         for cmd in cmds:
             # all operations should be BSgates, Rgates, or Sgates
-            assert isinstance(cmd.op, (ops.Vacuum, ops.Thermal, ops.GaussianTransform))
+            assert isinstance(cmd.op, (ops.Thermal, ops.GaussianTransform))
 
             # build up the symplectic transform
             modes = [i.ind for i in cmd.reg]
@@ -526,12 +561,13 @@
 
     def test_thermal_decomposition(self, hbar, tol):
         n = 3
-        prog = sf.Program(n)
+        prog = sf.Program(n, hbar=hbar)
         nbar = np.array([0.453, 0.23, 0.543])
         cov = np.diag(np.tile(2 * nbar + 1, 2)) * hbar / 2
 
-        G = ops.Gaussian(cov)
-        cmds = G.decompose(prog.register)
+        with eng:
+            G = ops.Gaussian(cov)
+            cmds = G.decompose(q)
 
         assert len(cmds) == n
 
@@ -542,26 +578,27 @@
 
     def test_squeezed_decomposition(self, hbar, tol):
         n = 3
-        prog = sf.Program(n)
+        prog = sf.Program(n, hbar=hbar)
 
         sq_r = np.array([0.453, 0.23, 0.543])
         S = np.diag(np.exp(np.concatenate([-sq_r, sq_r])))
-        cov = S @ S.T * (hbar / 2)
+        cov = S @ S.T
 
-        G = ops.Gaussian(cov)
-        cmds = G.decompose(prog.register)
+        with eng:
+            G = ops.Gaussian(cov)
+            cmds = G.decompose(q)
 
         assert len(cmds) == n
 
         # calculating the resulting decomposed symplectic
         for i, cmd in enumerate(cmds):
-            assert isinstance(cmd.op, ops.Squeezed)
+            assert isinstance(cmd.op, ops.Sgate)
             assert np.allclose(cmd.op.p[0].x, sq_r[i], atol=tol, rtol=0)
             assert cmd.op.p[1].x == 0
 
     def test_rotated_squeezed_decomposition(self, hbar, tol):
         n = 3
-        prog = sf.Program(n)
+        prog = sf.Program(n, hbar=hbar)
 
         sq_r = np.array([0.453, 0.23, 0.543])
         sq_phi = np.array([-0.123, 0.2143, 0.021])
@@ -571,36 +608,15 @@
         for i, phi in enumerate(sq_phi):
             S = _rotation(phi / 2, i, n) @ S
 
-        cov = S @ S.T * (hbar / 2)
-        G = ops.Gaussian(cov)
-        cmds = G.decompose(prog.register)
+        cov = S @ S.T
+        with eng:
+            G = ops.Gaussian(cov)
+            cmds = G.decompose(q)
 
         assert len(cmds) == n
 
         # calculating the resulting decomposed symplectic
         for i, cmd in enumerate(cmds):
-            assert isinstance(cmd.op, ops.Squeezed)
+            assert isinstance(cmd.op, ops.Sgate)
             assert np.allclose(cmd.op.p[0].x, sq_r[i], atol=tol, rtol=0)
             assert np.allclose(cmd.op.p[1].x, sq_phi[i], atol=tol, rtol=0)
-
-    def test_degenerate_decomposition(self, hbar, tol):
-        """Test that a decomposition involving no squeezing results in a Vacuum preparation."""
-        n = 2
-        prog = sf.Program(n)
-
-        sq_r = np.array([0, 1.5])
-        S = np.diag(np.exp(np.concatenate([-sq_r, sq_r])))
-        cov = S @ S.T * (hbar / 2)
-
-        G = ops.Gaussian(cov)
-        cmds = G.decompose(prog.register)
-
-        assert len(cmds) == 2
-
-        for cmd in cmds[:1]:
-            assert isinstance(cmd.op, ops.Vacuum)
-
-        for cmd in cmds[1:]:
-            assert isinstance(cmd.op, ops.Squeezed)
-            assert np.allclose(cmd.op.p[0].x, sq_r[1], atol=tol, rtol=0)
-            assert np.allclose(cmd.op.p[1].x, 0, atol=tol, rtol=0)
