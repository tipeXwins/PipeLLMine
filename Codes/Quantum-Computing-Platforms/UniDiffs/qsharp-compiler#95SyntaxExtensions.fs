--- qsharp-compiler/qsharp-compiler#95/after/SyntaxExtensions.fs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#95/before/SyntaxExtensions.fs	2022-01-10 16:02:54.000000000 +0000
@@ -298,29 +298,27 @@
 
 // active pattern for tuple matching
 
- // not the nicest solution, but unfortunatly type extensions cannot be used to satisfy member constraints...
-let private TupleItems<'T when 'T :> ITuple> (arg: 'T): 'T list option =
-    let cast a = box >> unbox |> List.map |> Option.map <| a
-    match box arg with
-    | :? QsExpression               as arg -> cast arg.TupleItems
-    | :? TypedExpression            as arg -> cast arg.TupleItems
-    | :? QsType                     as arg -> cast arg.TupleItems
-    | :? ResolvedType               as arg -> cast arg.TupleItems
-    | :? QsInitializer              as arg -> cast arg.TupleItems
-    | :? ResolvedInitializer        as arg -> cast arg.TupleItems
+let private TupleItems<'I> (arg : ITuple) = arg |> function  // not the nicest solution, but unfortunatly type extensions cannot be used to satisfy member constraints...
+    | :? QsExpression               as arg -> arg.TupleItems |> Option.map (List.map box)
+    | :? TypedExpression            as arg -> arg.TupleItems |> Option.map (List.map box)
+    | :? QsType                     as arg -> arg.TupleItems |> Option.map (List.map box)
+    | :? ResolvedType               as arg -> arg.TupleItems |> Option.map (List.map box)
+    | :? QsInitializer              as arg -> arg.TupleItems |> Option.map (List.map box)
+    | :? ResolvedInitializer        as arg -> arg.TupleItems |> Option.map (List.map box)
     // TODO: can be made an ITuple again once empty symbol tuples are no longer valid for functor specialiations...
-    //| :? QsSymbol                   as arg -> arg.TupleItems |> Option.map (List.map box)
-    | :? SymbolTuple                as arg -> cast arg.TupleItems
+    //| :? QsSymbol                   as arg -> arg.TupleItems |> Option.map (List.map box) 
+    | :? SymbolTuple                as arg -> arg.TupleItems |> Option.map (List.map box)
     | _ -> InvalidOperationException("no extension provided for tuple matching of the given ITuple object") |> raise
 
 let (| Item | _ |) arg =         
     match TupleItems arg with
-    | Some [item] -> Some item
+    | Some [item] -> Some (item |> unbox)
     | _ -> None
 
 let (| Tuple | _ |) arg =         
-    match TupleItems arg with
-    | Some items when items.Length > 1 -> Some items
+    match TupleItems arg with 
+    | Some [] | Some [_] -> None
+    | Some items when items.Length > 1 -> Some (items |> List.map unbox)
     | _ -> None
 
 let (| Missing | _ |) arg = 
@@ -346,4 +344,4 @@
         | QsCallable c -> Some (c.FullName, c)
         | _ -> None))
     callables.ToImmutableDictionary(fst, snd)
-    
+    
\ No newline at end of file
