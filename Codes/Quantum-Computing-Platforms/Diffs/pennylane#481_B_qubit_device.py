22d21
< import itertools
294c293
<         return (states_sampled_base_ten > 0).astype(int)[:, ::-1]
---
>         return (states_sampled_base_ten > 0).astype(int)
341,342c340
<         if wires is None:
<             return prob
---
>         wires = list(wires or range(self.num_wires))
346,349c344
<         prob = np.apply_over_axes(np.sum, prob, inactive_wires).flatten()
<         basis_states = np.array(list(itertools.product([0, 1], repeat=len(wires))))
<         perm = np.ravel_multi_index(basis_states[:, np.argsort(np.argsort(wires))].T, [2] * len(wires))
<         return prob[perm]
---
>         return np.apply_over_axes(np.sum, prob, inactive_wires).flatten()
