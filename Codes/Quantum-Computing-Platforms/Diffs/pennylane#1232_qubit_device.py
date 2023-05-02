190d189
<         multiple_sampled_jobs = circuit.is_sampled and self._has_partitioned_shots()
207c206
<                     results.append(r.T)
---
>                     results.append(r)
211,212c210
<             if not multiple_sampled_jobs:
<                 results = qml.math.stack(results)
---
>             results = qml.math.stack(results)
217c215
<         if (circuit.all_sampled or not circuit.is_sampled) and not multiple_sampled_jobs:
---
>         if circuit.all_sampled or not circuit.is_sampled:
