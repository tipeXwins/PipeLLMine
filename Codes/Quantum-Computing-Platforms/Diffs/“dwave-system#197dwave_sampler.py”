274,277c274
<         nodes = self.solver.nodes
<         edges = self.solver.edges
<         if not (all(v in nodes for v in h) and
<                 all((u, v) in edges or (v, u) in edges for u, v in J)):
---
>         if not self.solver.check_problem(h, J):
325,328c322
<         nodes = self.solver.nodes
<         edges = self.solver.edges
<         if not all(u in nodes if u == v else ((u, v) in edges or (v, u) in edges)
<                    for u, v in Q):
---
>         if not self.solver.check_problem({}, Q):
