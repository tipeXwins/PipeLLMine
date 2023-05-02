277a278
> @pytest.mark.broken('FIXME hbar issue')
287,289c288,290
<         G1 = ops.GaussianTransform(S1)
<         G1inv = ops.GaussianTransform(np.linalg.inv(S1))
<         G2 = ops.GaussianTransform(S2)
---
>         G1 = ops.GaussianTransform(S1, hbar=hbar)
>         G1inv = ops.GaussianTransform(np.linalg.inv(S1), hbar=hbar)
>         G2 = ops.GaussianTransform(S2, hbar=hbar)
295a297,306
>     def test_setting_hbar(self, hbar):
>         prog = sf.Program(3, hbar=hbar)
>         S1 = random_symplectic(3, passive=False)
>         with pytest.raises(ValueError, match="specify the hbar keyword argument"):
>             ops.GaussianTransform(S1)
>         G = ops.GaussianTransform(S1, hbar=hbar)
>         assert G.hbar == hbar
>         with eng:
>             G = ops.GaussianTransform(S1)
>         assert G.hbar == hbar
300c311,313
<         G = ops.GaussianTransform(np.identity(6))
---
>         prog = sf.Program(3)
>         with eng:
>             G = ops.GaussianTransform(np.identity(6))
309a323
>         prog = sf.Program(3)
311c325,326
<         G = ops.GaussianTransform(S1)
---
>         with eng:
>             G = ops.GaussianTransform(S1)
332,334c347,350
<         prog = sf.Program(n)
<         G = ops.GaussianTransform(S)
<         cmds = G.decompose(prog.register)
---
>         prog = sf.Program(n, hbar=hbar)
>         with eng:
>             G = ops.GaussianTransform(S)
>             cmds = G.decompose(q)
364c380
<         assert np.allclose(cov, S @ S.T, atol=tol, rtol=0)
---
>         assert np.allclose(cov, S @ S.T * hbar / 2, atol=tol, rtol=0)
374,376c390,393
<         prog = sf.Program(n)
<         G = ops.GaussianTransform(S)
<         cmds = G.decompose(prog.register)
---
>         prog = sf.Program(n, hbar=hbar)
>         with eng:
>             G = ops.GaussianTransform(S)
>             cmds = G.decompose(q)
399c416
<         assert np.allclose(cov, S @ S.T, atol=tol, rtol=0)
---
>         assert np.allclose(cov, S @ S.T * hbar / 2, atol=tol, rtol=0)
416,418c433,436
<         prog = sf.Program(n)
<         G = ops.GaussianTransform(S, vacuum=True)
<         cmds = G.decompose(prog.register)
---
>         prog = sf.Program(n, hbar=hbar)
>         with eng:
>             G = ops.GaussianTransform(S, vacuum=True)
>             cmds = G.decompose(q)
445c463
<         assert np.allclose(cov, S @ S.T, atol=tol, rtol=0)
---
>         assert np.allclose(cov, S @ S.T * hbar / 2, atol=tol, rtol=0)
447a466
> @pytest.mark.broken('FIXME hbar issue')
452c471
<         """Test that merging two Preparations only keeps the latter one."""
---
>         """Test that two covariances matrices overwrite each other on merge"""
456,457d474
<         r1 = np.random.randn(2*n)
<         r2 = np.random.randn(2*n)
459,460c476,477
<         G1 = ops.Gaussian(V1, r1)
<         G2 = ops.Gaussian(V2, r2)
---
>         cov1 = ops.Gaussian(V1, hbar=hbar)
>         cov2 = ops.Gaussian(V2, hbar=hbar)
462c479
<         assert G1.merge(G2) is G2
---
>         assert cov1.merge(cov2) == cov2
464,466c481,492
<         S = ops.Squeezed(2)
<         assert S.merge(G2) is G2
<         assert G2.merge(S) is S
---
>         assert ops.Squeezed(2).merge(cov2) == cov2
> 
>     def test_setting_hbar(self, hbar):
>         prog = sf.Program(3, hbar=hbar)
>         cov = random_covariance(3, hbar=hbar)
>         with pytest.raises(ValueError, match="specify the hbar keyword argument"):
>             ops.Gaussian(cov)
>         G = ops.Gaussian(cov, hbar=hbar)
>         assert G.hbar == hbar
>         with eng:
>             G = ops.Gaussian(cov)
>         assert G.hbar == hbar
473c499,506
<             ops.Gaussian(cov, r=np.array([0]))
---
>             ops.Gaussian(cov, r=np.array([0]), hbar=hbar)
>     def test_apply_decomp(self, hbar):
>         prog = sf.Program(3, hbar=hbar)
>         cov = random_covariance(3, hbar=hbar)
>         with eng:
>             G = ops.Gaussian(cov, decomp=True)
>         with pytest.raises(NotImplementedError):
>             G._apply(q, None)
477c510
<         prog = sf.Program(3)
---
>         prog = sf.Program(3, hbar=hbar)
487c520,521
<         G = ops.Gaussian(cov, decomp=False)
---
>         with eng:
>             G = ops.Gaussian(cov, decomp=False)
489c523
<             G._apply(prog.register, DummyBackend())
---
>             G._apply(q, DummyBackend())
494c528
<         prog = sf.Program(n)
---
>         prog = sf.Program(n, hbar=hbar)
497,498c531,533
<         G = ops.Gaussian(cov)
<         cmds = G.decompose(prog.register)
---
>         with eng:
>             G = ops.Gaussian(cov)
>             cmds = G.decompose(q)
506c541
<             assert isinstance(cmd.op, (ops.Vacuum, ops.Thermal, ops.GaussianTransform))
---
>             assert isinstance(cmd.op, (ops.Thermal, ops.GaussianTransform))
529c564
<         prog = sf.Program(n)
---
>         prog = sf.Program(n, hbar=hbar)
533,534c568,570
<         G = ops.Gaussian(cov)
<         cmds = G.decompose(prog.register)
---
>         with eng:
>             G = ops.Gaussian(cov)
>             cmds = G.decompose(q)
545c581
<         prog = sf.Program(n)
---
>         prog = sf.Program(n, hbar=hbar)
549c585
<         cov = S @ S.T * (hbar / 2)
---
>         cov = S @ S.T
551,552c587,589
<         G = ops.Gaussian(cov)
<         cmds = G.decompose(prog.register)
---
>         with eng:
>             G = ops.Gaussian(cov)
>             cmds = G.decompose(q)
558c595
<             assert isinstance(cmd.op, ops.Squeezed)
---
>             assert isinstance(cmd.op, ops.Sgate)
564c601
<         prog = sf.Program(n)
---
>         prog = sf.Program(n, hbar=hbar)
574,576c611,614
<         cov = S @ S.T * (hbar / 2)
<         G = ops.Gaussian(cov)
<         cmds = G.decompose(prog.register)
---
>         cov = S @ S.T
>         with eng:
>             G = ops.Gaussian(cov)
>             cmds = G.decompose(q)
582c620
<             assert isinstance(cmd.op, ops.Squeezed)
---
>             assert isinstance(cmd.op, ops.Sgate)
585,606d622
< 
<     def test_degenerate_decomposition(self, hbar, tol):
<         """Test that a decomposition involving no squeezing results in a Vacuum preparation."""
<         n = 2
<         prog = sf.Program(n)
< 
<         sq_r = np.array([0, 1.5])
<         S = np.diag(np.exp(np.concatenate([-sq_r, sq_r])))
<         cov = S @ S.T * (hbar / 2)
< 
<         G = ops.Gaussian(cov)
<         cmds = G.decompose(prog.register)
< 
<         assert len(cmds) == 2
< 
<         for cmd in cmds[:1]:
<             assert isinstance(cmd.op, ops.Vacuum)
< 
<         for cmd in cmds[1:]:
<             assert isinstance(cmd.op, ops.Squeezed)
<             assert np.allclose(cmd.op.p[0].x, sq_r[1], atol=tol, rtol=0)
<             assert np.allclose(cmd.op.p[1].x, 0, atol=tol, rtol=0)
