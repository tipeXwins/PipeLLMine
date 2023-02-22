--- strawberryfields/strawberryfields#194/after/similarity.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#194/before/similarity.py	2022-01-10 16:02:54.000000000 +0000
@@ -201,18 +201,16 @@
             "max_count_per_mode or reducing the number of photons."
         )
 
-    cards = []
-    orbs = []
+    sample = [0] * modes
+    available_modes = list(range(modes))
 
-    for orb in orbits(photon_number):
-        if max(orb) <= max_count_per_mode:
-            cards.append(orbit_cardinality(orb, modes))
-            orbs.append(orb)
+    for _ in range(photon_number):
+        j = np.random.choice(available_modes)
+        sample[j] += 1
+        if sample[j] == max_count_per_mode:
+            available_modes.remove(j)
 
-    norm = sum(cards)
-    prob = [c / norm for c in cards]
-    orbit = orbs[np.random.choice(len(prob), p=prob)]
-    return orbit_to_sample(orbit, modes)
+    return sample
 
 
 def orbit_cardinality(orbit: list, modes: int) -> int:
@@ -272,9 +270,7 @@
     return cardinality
 
 
-def prob_orbit_mc(
-    graph: nx.Graph, orbit: list, n_mean: float = 5, samples: int = 1000
-) -> float:
+def prob_orbit_mc(graph: nx.Graph, orbit: list, n_mean: float = 5, samples: int = 1000) -> float:
     """Gives a Monte Carlo estimate of the probability of a given orbit for a GBS device encoded
     according to the input graph.
 
