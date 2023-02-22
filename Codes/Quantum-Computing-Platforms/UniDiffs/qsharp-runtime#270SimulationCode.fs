--- qsharp-runtime/qsharp-runtime#270/after/SimulationCode.fs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#270/before/SimulationCode.fs	2022-01-10 16:02:54.000000000 +0000
@@ -1454,22 +1454,16 @@
                     []
                 ``}``
             :> MemberDeclarationSyntax
-        let buildNamedItemFields =
-            let produceProperty (decl : LocalVariableDeclaration<NonNullable<_>>) valueExpr =
-                ``property-arrow_get`` (roslynTypeName context decl.Type) decl.VariableName.Value [ ``public`` ]
-                    ``get`` (``=>`` valueExpr) :> MemberDeclarationSyntax
-            let rec buildProps current = function
-                | QsTuple items -> items |> Seq.mapi (fun i x -> buildProps (current <|.|> ``ident`` ("Item" + (i+1).ToString())) x) |> Seq.collect id
-                | QsTupleItem (Anonymous _) -> Seq.empty
-                | QsTupleItem (Named decl) -> seq { yield produceProperty decl current }
-            let rec readType typeItem =
-                match typeItem with
-                | QsTuple items when items.IsEmpty -> Seq.empty
-                | QsTuple items when items.Length = 1 -> items |> Seq.head |> readType
-                | QsTuple _ -> buildProps (``ident`` "Data") typeItem
-                | QsTupleItem (Anonymous _) -> Seq.empty
-                | QsTupleItem (Named decl) -> seq { yield produceProperty decl (``ident`` "Data") }
-            readType udt.TypeItems |> Seq.toList
+        let buildNamedItemFields = 
+            let items = getAllItems (``ident`` "Data") qsharpType
+            let rec buildProps = function 
+                | QsTuple items -> items |> Seq.collect (fun i -> buildProps i)
+                | QsTupleItem (Anonymous _) -> items.Dequeue() |> ignore; Seq.empty
+                | QsTupleItem (Named decl) -> seq { yield
+                    ``property-arrow_get`` (roslynTypeName context decl.Type) decl.VariableName.Value [ ``public`` ] 
+                        ``get`` (``=>`` (items.Dequeue()))
+                    :> MemberDeclarationSyntax}
+            buildProps udt.TypeItems |> Seq.toList
         let buildItemFields =
             let buildOne i t =
                 ``property-arrow_get`` (roslynTypeName context t) (sprintf "Item%d" (i+1)) [ ``public`` ]
