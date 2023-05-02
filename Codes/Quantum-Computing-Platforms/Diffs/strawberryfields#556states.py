308,309c308,309
<     c1 = ((1.0 * a) ** k) / np.sqrt(fac(k))
<     c2 = ((-1.0 * a) ** k) / np.sqrt(fac(k))
---
>     c1 = (a ** k) / np.sqrt(fac(k))
>     c2 = ((-a) ** k) / np.sqrt(fac(k))
