--- qsharp-runtime/qsharp-runtime#76/after/SimulationCode.fs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#76/before/SimulationCode.fs	2022-01-10 16:02:54.000000000 +0000
@@ -550,7 +550,6 @@
             // they don't need to have the return type explicitly in the apply.
             let isNonGenericCallable() =     
                 match op.Expression with
-                | Identifier (_, Value tArgs) when tArgs.Length > 0 -> false
                 | Identifier (id, _) -> 
                     match id with
                     | GlobalCallable n ->
@@ -558,7 +557,7 @@
                         if sameName then        // when called recursively, we always need to specify the return type.
                             false
                         else
-                            not (hasTypeParameters [op.ResolvedType]) 
+                            not (hasTypeParameters [op.ResolvedType])
                     | _ -> 
                         false
                 | _ ->
