--- ProjectQ/ProjectQ#368/after/ibm.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#368/before/ibm.py	2022-01-10 16:02:54.000000000 +0000
@@ -53,7 +53,7 @@
     if token is None:
         token = getpass.getpass(prompt='IBM Q token > ')
     if device is None:
-        device = getpass.getpass(prompt='IBM device > ')
+        token = getpass.getpass(prompt='IBM device > ')
     # create main compiler engine for the IBM back-end
     eng = MainEngine(IBMBackend(use_hardware=True, token=token, num_runs=1024,
                                 verbose=False, device=device),
