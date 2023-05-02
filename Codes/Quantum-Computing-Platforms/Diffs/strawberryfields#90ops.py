307d306
< _decomposition_tol = 1e-13  # TODO this tolerance is used for various purposes and is not well-defined
350a350
>         self.decomp = True
586d585
<     ns = None  # overridden by child classes in __init__
1602a1602
>     ns = None
1606d1605
<         self.ns = U.shape[0]
1612a1612
>             self.ns = U.shape[0]
1619c1619
<                 if np.abs(phi) >= _decomposition_tol:
---
>                 if np.abs(phi) >= _decomposition_merge_tol:
1621c1621
<                 if np.abs(theta) >= _decomposition_tol:
---
>                 if np.abs(theta) >= _decomposition_merge_tol:
1625c1625
<                 if np.abs(expphi - 1) >= _decomposition_tol:
---
>                 if np.abs(expphi - 1) >= _decomposition_merge_tol:
1630c1630
<                 if np.abs(theta) >= _decomposition_tol:
---
>                 if np.abs(theta) >= _decomposition_merge_tol:
1632c1632
<                 if np.abs(phi) >= _decomposition_tol:
---
>                 if np.abs(phi) >= _decomposition_merge_tol:
1653a1654
>     ns = None
1657d1657
<         self.ns = A.shape[0]
1664a1665
>             self.ns = self.U.shape[0]
1671c1672
<                 if np.abs(s) >= _decomposition_tol:
---
>                 if np.abs(s) >= _decomposition_merge_tol:
1674c1675
<             if np.all(np.abs(self.U - np.identity(len(self.U))) >= _decomposition_tol):
---
>             if np.all(np.abs(self.U - np.identity(len(self.U))) >= _decomposition_merge_tol):
1680a1682
>     ns = None
1684,1686c1686
<         self.ns = S.shape[0] // 2
<         self.vacuum = vacuum  #: bool: if True, ignore the first unitary matrix when applying the gate
<         N = self.ns  # shorthand
---
>         N = S.shape[0]//2
1690d1689
<         self.active = (np.abs(diffn) > _decomposition_tol)  #: bool: S is an active symplectic transformation
1692c1691
<         if not self.active:
---
>         if np.abs(diffn) <= _decomposition_merge_tol:
1693a1693
>             self.active = False
1698a1699
>             self.active = True
1699a1701
>             N = S.shape[0]//2
1705,1707c1707,1711
<             self.U1 = X1+1j*P1  #: array[complex]: unitary matrix corresponding to O_1
<             self.U2 = X2+1j*P2  #: array[complex]: unitary matrix corresponding to O_2
<             self.Sq = np.diagonal(smat)[:N]  #: array[complex]: diagonal vector of the squeezing matrix R
---
>             self.U1 = X1+1j*P1
>             self.U2 = X2+1j*P2
>             self.Sq = np.diagonal(smat)[:N]
>         self.ns = N
>         self.vacuum = vacuum
1717c1721
<                 if np.abs(expr - 1) >= _decomposition_tol:
---
>                 if np.abs(expr - 1) >= _decomposition_merge_tol:
1735,1736c1739,1740
<         V = V / (sf.hbar / 2)
<         self.ns = V.shape[0] // 2
---
>         self.hbar = sf.hbar
>         self.ns = V.shape[0]//2
1739c1743
<             r = np.zeros(2*self.ns)
---
>             r = [0] * (2*self.ns)
1745,1746d1748
<         super().__init__([V, r])  # V is hbar-independent, r is not
< 
1752,1753c1754,1755
<             self.pure = np.abs(np.linalg.det(V) - 1.0) < tol
<             self.nbar = 0.5 * (np.diag(th)[:self.ns] - 1.0)
---
>             self.pure = np.abs(np.linalg.det(V) - (self.hbar/2)**(2*self.ns)) < tol
>             self.nbar = np.diag(th)[:self.ns]/self.hbar - 0.5
1755c1757,1758
<         self.decomp = decomp  #: bool: if False, use the backend API call instead of decomposition
---
>         super().__init__([V, r])
>         self.decomp = decomp
1760c1763
<         backend.prepare_gaussian_state(p[1]/s, p[0], reg)
---
>         backend.prepare_gaussian_state(p[1]/s, p[0]/(s*s), reg)
1777,1778c1780,1781
<             for n, expr in enumerate(D[:self.ns]):
<                 if np.abs(expr - 1) >= _decomposition_tol:
---
>             for n, expr in enumerate(D[:self.ns]*2/self.hbar):
>                 if np.abs(expr - 1) >= _decomposition_merge_tol:
1780,1782c1783
<                     cmds.append(Command(Squeezed(r, 0), reg[n]))
<                 else:
<                     cmds.append(Command(Vac, reg[n]))
---
>                     cmds.append(Command(Sgate(r, 0), reg[n]))
1787,1792c1788,1791
<                 if not np.all(v - np.identity(2) < _decomposition_tol):
<                     r = np.abs(arccosh(np.sum(np.diag(v)) / 2)) / 2
<                     phi = arctan(2 * v[0, 1] / np.sum(np.diag(v) * [1, -1]))
<                     cmds.append(Command(Squeezed(r, phi), reg[n]))
<                 else:
<                     cmds.append(Command(Vac, reg[n]))
---
>                 if not np.all(v - np.identity(2)*self.hbar/2 < 1e-10):
>                     r = np.abs(arccosh(np.sum(np.diag(v/self.hbar)))/2)
>                     phi = arctan(2*v[0, 1] / np.sum(np.diag(v)*[1, -1]))
>                     cmds.append(Command(Sgate(r, phi), reg[n]))
1796,1797c1795,1796
<             for n, nbar in enumerate(0.5 * (D[:self.ns] - 1.0)):
<                 if nbar >= _decomposition_tol:
---
>             for n, nbar in enumerate(D[:self.ns]/self.hbar - 0.5):
>                 if nbar >= _decomposition_merge_tol:
1799,1800d1797
<                 else:
<                     cmds.append(Command(Vac, reg[n]))
1806c1803
<                     if np.abs(nbar) >= _decomposition_tol:
---
>                     if np.abs(nbar) >= _decomposition_merge_tol:
1808,1812d1804
<                     else:
<                         cmds.append(Command(Vac, reg[n]))
<             else:
<                 for r in reg:
<                     cmds.append(Command(Vac, r))
