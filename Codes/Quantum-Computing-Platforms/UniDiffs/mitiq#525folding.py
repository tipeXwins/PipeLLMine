--- mitiq/mitiq#525/after/folding.py	2022-01-10 16:02:54.000000000 +0000
+++ mitiq/mitiq#525/before/folding.py	2022-01-10 16:02:54.000000000 +0000
@@ -741,11 +741,10 @@
         if fold_method_args:
             folded = fold_method(
                 folded, this_stretch, *fold_method_args, squash_moments=False,
-                **{k: v for k, v in kwargs.items() if k != "squash_moments"},
             )
         else:
             folded = fold_method(folded, this_stretch, squash_moments=False,
-                **{k: v for k, v in kwargs.items() if k != "squash_moments"})
+	    )
         scale_factor /= 3.0
 
     if not (kwargs.get("squash_moments") is False):
