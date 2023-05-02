237,253c237
<     iters = 5000
<     max_iters = kwargs.get('max_iters', 20000)
<     problem_solved = False
<     while not problem_solved:
<         kwargs['max_iters'] = iters
<         prob.solve(**kwargs)
<         if prob.status in ["optimal_inaccurate", "optimal"]:
<             problem_solved = True
<         elif prob.status == "unbounded_inaccurate":
<             if iters < max_iters:
<                 iters *= 2
<             else:
<                 raise RuntimeError("CVX fit failed, probably not enough iterations for the solver")
<         elif prob.status in ["infeasible", "unbounded"]:
<             raise RuntimeError("CVX fit failed, problem status {} which should not happen".format(prob.status))
<         else:
<             raise RuntimeError("CVX fit failed, reason unknown")
---
>     prob.solve(**kwargs)
