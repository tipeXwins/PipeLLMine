45d44
<     N = 150
47c46
<     for i in range(N):
---
>     for i in range(150):
64,65c63,64
<     assert num_phase / N >= 0.35, "Statistics phase calculation are not correct (%f vs. %f)" % (
<         num_phase / N,
---
>     assert num_phase / 100.0 >= 0.35, "Statistics phase calculation are not correct (%f vs. %f)" % (
>         num_phase / 100.0,
79d77
<     N = 150
81c79
<     for i in range(N):
---
>     for i in range(150):
97,98c95,96
<     assert num_phase / N >= 0.35, "Statistics phase calculation are not correct (%f vs. %f)" % (
<         num_phase / N,
---
>     assert num_phase / 100.0 >= 0.35, "Statistics phase calculation are not correct (%f vs. %f)" % (
>         num_phase / 100.0,
118d115
<     N = 150
120c117
<     for i in range(N):
---
>     for i in range(150):
135,136c132,133
<     assert num_phase / N >= 0.34, "Statistics phase calculation are not correct (%f vs. %f)" % (
<         num_phase / N,
---
>     assert num_phase / 100.0 >= 0.34, "Statistics phase calculation are not correct (%f vs. %f)" % (
>         num_phase / 100.0,
149d145
<     N = 100
153c149
<     for i in range(N):
---
>     for i in range(100):
181,182c177,178
<     plus_probability = len(results_plus) / N
<     assert total == pytest.approx(N, abs=5)
---
>     plus_probability = len(results_plus) / 100.0
>     assert total == pytest.approx(100, abs=5)
