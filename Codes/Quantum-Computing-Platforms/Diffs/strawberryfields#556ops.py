870,871c870,871
<         c1 = ((1.0 * alpha) ** l) / np.sqrt(ssp.factorial(l))
<         c2 = ((-1.0 * alpha) ** l) / np.sqrt(ssp.factorial(l))
---
>         c1 = (alpha ** l) / np.sqrt(ssp.factorial(l))
>         c2 = ((-alpha) ** l) / np.sqrt(ssp.factorial(l))
