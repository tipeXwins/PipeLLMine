184,193c184,186
<         flattened_observables = []
<         for obs in observables:
<             if isinstance(obs, TensorProduct):
<                 for nested_obs in obs.factors:
<                     flattened_observables.append(nested_obs)
<             else:
<                 flattened_observables.append(obs)
<         self._factors = tuple(flattened_observables)
<         qubit_count = sum([obs.qubit_count for obs in flattened_observables])
<         display_name = "@".join([obs.ascii_symbols[0] for obs in flattened_observables])
---
>         self._factors = tuple(observables)
>         qubit_count = sum([obs.qubit_count for obs in observables])
>         display_name = "@".join([obs.ascii_symbols[0] for obs in observables])
246a240,249
>     def __matmul__(self, other):
>         if isinstance(other, TensorProduct):
>             return TensorProduct(list(self.factors) + list(other.factors))
>         if isinstance(other, Observable):
>             return TensorProduct(list(self.factors) + [other])
>         raise ValueError("Can only perform tensor products between observables.")
>     def __rmatmul__(self, other):
>         if isinstance(other, Observable):
>             return TensorProduct([other] + list(self.factors))
>         raise ValueError("Can only perform tensor products between observables.")
