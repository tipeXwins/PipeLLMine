--- dwave-system/dwave-system#276/after/embedding.py	2022-01-10 16:02:54.000000000 +0000
+++ dwave-system/dwave-system#276/before/embedding.py	2022-01-10 16:02:54.000000000 +0000
@@ -235,7 +235,7 @@
 
         warninghandler = WarningHandler(warnings)
 
-        warninghandler.chain_strength(bqm, chain_strength, embedding)
+        warninghandler.chain_strength(bqm, chain_strength)
         warninghandler.chain_length(embedding)
 
         if bqm and not embedding:
