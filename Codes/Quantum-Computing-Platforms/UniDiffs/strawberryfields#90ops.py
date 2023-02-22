--- strawberryfields/strawberryfields#90/after/ops.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#90/before/ops.py	2022-01-10 16:02:54.000000000 +0000
@@ -304,7 +304,6 @@
 
 # numerical tolerances
 _decomposition_merge_tol = 1e-13
-_decomposition_tol = 1e-13  # TODO this tolerance is used for various purposes and is not well-defined
 
 
 def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
@@ -348,6 +347,7 @@
         self._extra_deps = set()
         #: list[Parameter]
         self.p = []
+        self.decomp = True
 
         if par:
             # convert each parameter into a Parameter instance, keep track of dependenciens
@@ -583,7 +583,6 @@
 
     The first parameter p[0] of the Decomposition is always a square matrix.
     """
-    ns = None  # overridden by child classes in __init__
 
     def merge(self, other):
         # can be merged if they are the same class
@@ -1600,36 +1599,37 @@
 
 
 class Interferometer(Decomposition):
+    ns = None
 
     def __init__(self, U, tol=1e-11):
         super().__init__([U])
-        self.ns = U.shape[0]
 
         if np.all(np.abs(U - np.identity(len(U))) < _decomposition_merge_tol):
             self.identity = True
         else:
             self.identity = False
             self.BS1, self.BS2, self.R = clements(U, tol=tol)
+            self.ns = U.shape[0]
 
     def _decompose(self, reg):
         cmds = []
 
         if not self.identity:
             for n, m, theta, phi, _ in self.BS1:
-                if np.abs(phi) >= _decomposition_tol:
+                if np.abs(phi) >= _decomposition_merge_tol:
                     cmds.append(Command(Rgate(phi), reg[n]))
-                if np.abs(theta) >= _decomposition_tol:
+                if np.abs(theta) >= _decomposition_merge_tol:
                     cmds.append(Command(BSgate(theta, 0), (reg[n], reg[m])))
 
             for n, expphi in enumerate(self.R):
-                if np.abs(expphi - 1) >= _decomposition_tol:
+                if np.abs(expphi - 1) >= _decomposition_merge_tol:
                     q = log(expphi).imag
                     cmds.append(Command(Rgate(q), reg[n]))
 
             for n, m, theta, phi, _ in reversed(self.BS2):
-                if np.abs(theta) >= _decomposition_tol:
+                if np.abs(theta) >= _decomposition_merge_tol:
                     cmds.append(Command(BSgate(-theta, 0), (reg[n], reg[m])))
-                if np.abs(phi) >= _decomposition_tol:
+                if np.abs(phi) >= _decomposition_merge_tol:
                     cmds.append(Command(Rgate(-phi), reg[n]))
 
         return cmds
@@ -1651,10 +1651,10 @@
         tol (float): the tolerance used when checking if the input matrix is symmetric:
             :math:`|A-A^T| <` tol
     """
+    ns = None
 
     def __init__(self, A, max_mean_photon=1.0, make_traceless=True, tol=1e-6):
         super().__init__([A])
-        self.ns = A.shape[0]
 
         if np.all(np.abs(A - np.identity(len(A))) < _decomposition_merge_tol):
             self.identity = True
@@ -1662,49 +1662,53 @@
             self.identity = False
             self.sq, self.U = graph_embed(
                 A, max_mean_photon=max_mean_photon, make_traceless=make_traceless, tol=tol)
+            self.ns = self.U.shape[0]
 
     def _decompose(self, reg):
         cmds = []
 
         if not self.identity:
             for n, s in enumerate(self.sq):
-                if np.abs(s) >= _decomposition_tol:
+                if np.abs(s) >= _decomposition_merge_tol:
                     cmds.append(Command(Sgate(s), reg[n]))
 
-            if np.all(np.abs(self.U - np.identity(len(self.U))) >= _decomposition_tol):
+            if np.all(np.abs(self.U - np.identity(len(self.U))) >= _decomposition_merge_tol):
                 cmds.append(Command(Interferometer(self.U), reg))
 
         return cmds
 
 
 class GaussianTransform(Decomposition):
+    ns = None
 
     def __init__(self, S, vacuum=False, tol=1e-10):
         super().__init__([S])
-        self.ns = S.shape[0] // 2
-        self.vacuum = vacuum  #: bool: if True, ignore the first unitary matrix when applying the gate
-        N = self.ns  # shorthand
+        N = S.shape[0]//2
 
         # check if input symplectic is passive (orthogonal)
         diffn = np.linalg.norm(S @ S.T - np.identity(2*N))
-        self.active = (np.abs(diffn) > _decomposition_tol)  #: bool: S is an active symplectic transformation
 
-        if not self.active:
+        if np.abs(diffn) <= _decomposition_merge_tol:
             # The transformation is passive, do Clements
+            self.active = False
             X1 = S[:N, :N]
             P1 = S[N:, :N]
             self.U1 = X1+1j*P1
         else:
             # transformation is active, do Bloch-Messiah
+            self.active = True
             O1, smat, O2 = bloch_messiah(S, tol=tol)
+            N = S.shape[0]//2
             X1 = O1[:N, :N]
             P1 = O1[N:, :N]
             X2 = O2[:N, :N]
             P2 = O2[N:, :N]
 
-            self.U1 = X1+1j*P1  #: array[complex]: unitary matrix corresponding to O_1
-            self.U2 = X2+1j*P2  #: array[complex]: unitary matrix corresponding to O_2
-            self.Sq = np.diagonal(smat)[:N]  #: array[complex]: diagonal vector of the squeezing matrix R
+            self.U1 = X1+1j*P1
+            self.U2 = X2+1j*P2
+            self.Sq = np.diagonal(smat)[:N]
+        self.ns = N
+        self.vacuum = vacuum
 
     def _decompose(self, reg):
         cmds = []
@@ -1714,7 +1718,7 @@
                 cmds = [Command(Interferometer(self.U2), reg)]
 
             for n, expr in enumerate(self.Sq):
-                if np.abs(expr - 1) >= _decomposition_tol:
+                if np.abs(expr - 1) >= _decomposition_merge_tol:
                     r = abs(log(expr))
                     phi = np.angle(log(expr))
                     cmds.append(Command(Sgate(-r, phi), reg[n]))
@@ -1732,32 +1736,31 @@
     ns = None
 
     def __init__(self, V, r=None, decomp=True, tol=1e-6):
-        V = V / (sf.hbar / 2)
-        self.ns = V.shape[0] // 2
+        self.hbar = sf.hbar
+        self.ns = V.shape[0]//2
 
         if r is None:
-            r = np.zeros(2*self.ns)
+            r = [0] * (2*self.ns)
         r = np.asarray(r)
 
         if len(r) != V.shape[0]:
             raise ValueError('Vector of means must have the same length as the covariance matrix.')
 
-        super().__init__([V, r])  # V is hbar-independent, r is not
-
         self.x_disp = r[:self.ns]
         self.p_disp = r[self.ns:]
 
         if decomp:
             th, self.S = williamson(V, tol=tol)
-            self.pure = np.abs(np.linalg.det(V) - 1.0) < tol
-            self.nbar = 0.5 * (np.diag(th)[:self.ns] - 1.0)
+            self.pure = np.abs(np.linalg.det(V) - (self.hbar/2)**(2*self.ns)) < tol
+            self.nbar = np.diag(th)[:self.ns]/self.hbar - 0.5
 
-        self.decomp = decomp  #: bool: if False, use the backend API call instead of decomposition
+        super().__init__([V, r])
+        self.decomp = decomp
 
     def _apply(self, reg, backend, **kwargs):
         p = _unwrap(self.p)
         s = sqrt(sf.hbar / 2)  # scaling factor, since the backend API call is hbar-independent
-        backend.prepare_gaussian_state(p[1]/s, p[0], reg)
+        backend.prepare_gaussian_state(p[1]/s, p[0]/(s*s), reg)
 
     def _decompose(self, reg):
         # pylint: disable=too-many-branches
@@ -1774,42 +1777,31 @@
 
         if self.pure and is_diag:
             # covariance matrix consists of x/p quadrature squeezed state
-            for n, expr in enumerate(D[:self.ns]):
-                if np.abs(expr - 1) >= _decomposition_tol:
+            for n, expr in enumerate(D[:self.ns]*2/self.hbar):
+                if np.abs(expr - 1) >= _decomposition_merge_tol:
                     r = abs(log(expr)/2)
-                    cmds.append(Command(Squeezed(r, 0), reg[n]))
-                else:
-                    cmds.append(Command(Vac, reg[n]))
+                    cmds.append(Command(Sgate(r, 0), reg[n]))
 
         elif self.pure and is_block_diag:
             # covariance matrix consists of rotated squeezed states
             for n, v in enumerate(BD_modes):
-                if not np.all(v - np.identity(2) < _decomposition_tol):
-                    r = np.abs(arccosh(np.sum(np.diag(v)) / 2)) / 2
-                    phi = arctan(2 * v[0, 1] / np.sum(np.diag(v) * [1, -1]))
-                    cmds.append(Command(Squeezed(r, phi), reg[n]))
-                else:
-                    cmds.append(Command(Vac, reg[n]))
+                if not np.all(v - np.identity(2)*self.hbar/2 < 1e-10):
+                    r = np.abs(arccosh(np.sum(np.diag(v/self.hbar)))/2)
+                    phi = arctan(2*v[0, 1] / np.sum(np.diag(v)*[1, -1]))
+                    cmds.append(Command(Sgate(r, phi), reg[n]))
 
         elif not self.pure and is_diag and np.all(D[:self.ns] == D[self.ns:]):
             # covariance matrix consists of thermal states
-            for n, nbar in enumerate(0.5 * (D[:self.ns] - 1.0)):
-                if nbar >= _decomposition_tol:
+            for n, nbar in enumerate(D[:self.ns]/self.hbar - 0.5):
+                if nbar >= _decomposition_merge_tol:
                     cmds.append(Command(Thermal(nbar), reg[n]))
-                else:
-                    cmds.append(Command(Vac, reg[n]))
 
         else:
             if not self.pure:
                 # mixed state, must initialise thermal states
                 for n, nbar in enumerate(self.nbar):
-                    if np.abs(nbar) >= _decomposition_tol:
+                    if np.abs(nbar) >= _decomposition_merge_tol:
                         cmds.append(Command(Thermal(nbar), reg[n]))
-                    else:
-                        cmds.append(Command(Vac, reg[n]))
-            else:
-                for r in reg:
-                    cmds.append(Command(Vac, r))
 
             cmds.append(Command(GaussianTransform(self.S, vacuum=self.pure), reg))
 
