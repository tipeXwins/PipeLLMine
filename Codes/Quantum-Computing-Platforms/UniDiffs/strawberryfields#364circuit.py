--- strawberryfields/strawberryfields#364/after/circuit.py	2022-01-10 16:02:54.000000000 +0000
+++ strawberryfields/strawberryfields#364/before/circuit.py	2022-01-10 16:02:54.000000000 +0000
@@ -763,7 +763,6 @@
             # Numpy also does not use the log probabilities
             probs = rho_dist.flatten().real
             probs /= np.sum(probs)
-            probs[np.abs(probs) < 1e-10] = 0
             sample_hist = np.random.multinomial(1, probs)
             sample_idx = list(sample_hist).index(1)
             homodyne_sample = q_tensor[sample_idx]
