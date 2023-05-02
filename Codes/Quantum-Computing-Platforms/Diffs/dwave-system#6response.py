70c70
<         nodes = future.solver.nodes
---
>         nodelist = future.solver._encoding_qubits
78c78
<                 sample = {v: sample[v] for v in nodes}
---
>                 sample = dict(zip(nodelist, sample))
