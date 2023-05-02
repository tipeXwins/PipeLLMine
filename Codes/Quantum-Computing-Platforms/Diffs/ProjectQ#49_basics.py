173,176c173,178
<         engines = [q.engine for reg in qubits for q in reg]
<         eng = engines[0]
<         assert all(e is eng for e in engines)
<         return Command(eng, self, qubits)
---
>         for i in range(len(qubits)):
>             for j in range(len(qubits[i]) - 1):
>                 assert(qubits[i][j].engine == qubits[i][j + 1].engine)
>             if i < len(qubits) - 1:
>                 assert(qubits[i][-1].engine == qubits[i + 1][0].engine)
>         return Command(qubits[0][0].engine, self, qubits)
