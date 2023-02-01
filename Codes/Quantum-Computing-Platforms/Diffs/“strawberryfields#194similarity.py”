204,205c204,205
<     cards = []
<     orbs = []
---
>     sample = [0] * modes
>     available_modes = list(range(modes))
207,210c207,211
<     for orb in orbits(photon_number):
<         if max(orb) <= max_count_per_mode:
<             cards.append(orbit_cardinality(orb, modes))
<             orbs.append(orb)
---
>     for _ in range(photon_number):
>         j = np.random.choice(available_modes)
>         sample[j] += 1
>         if sample[j] == max_count_per_mode:
>             available_modes.remove(j)
212,215c213
<     norm = sum(cards)
<     prob = [c / norm for c in cards]
<     orbit = orbs[np.random.choice(len(prob), p=prob)]
<     return orbit_to_sample(orbit, modes)
---
>     return sample
275,277c273
< def prob_orbit_mc(
<     graph: nx.Graph, orbit: list, n_mean: float = 5, samples: int = 1000
< ) -> float:
---
> def prob_orbit_mc(graph: nx.Graph, orbit: list, n_mean: float = 5, samples: int = 1000) -> float:
