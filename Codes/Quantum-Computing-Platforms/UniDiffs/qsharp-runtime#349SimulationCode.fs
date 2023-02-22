--- qsharp-runtime/qsharp-runtime#349/after/SimulationCode.fs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/SimulationCode.fs	2022-01-10 16:02:54.000000000 +0000
@@ -8,7 +8,6 @@
 open System.Collections.Immutable
 open System.Linq
 open System.Reflection
-open System.Text.RegularExpressions
 
 open Microsoft.CodeAnalysis
 open Microsoft.CodeAnalysis.CSharp.Syntax
@@ -52,22 +51,11 @@
         ("Step",   { Namespace = "Microsoft.Quantum.Core" |> NonNullable<String>.New; Name = "RangeStep" |> NonNullable<String>.New } )
     ]
 
-    let internal userDefinedName (parent : QsQualifiedName option) name =
-        let isReserved =
-            match name with
-            | "Data"
-            | "Deconstruct"
-            | "Info"
-            | "Run" -> true
-            | _ ->
-                Regex.IsMatch (name, @"^Item\d+$") ||
-                parent |> Option.exists (fun current' -> name = current'.Name.Value)
-        if isReserved then name + "__" else name
-
     let isCurrentOp context n = match context.current with | None -> false | Some name ->  name = n
 
     let prependNamespaceString (name : QsQualifiedName) =
-        name.Namespace.Value.Replace (".", "__") + "__" + name.Name.Value
+        let pieces = name.Namespace.Value.Split([|'.'|]) |> String.Concat
+        pieces + name.Name.Value
 
     let needsFullPath context (op:QsQualifiedName) =
         let hasMultipleDefinitions() = if context.byName.ContainsKey op.Name then context.byName.[op.Name].Length > 1 else false
@@ -80,11 +68,6 @@
         else
             not (autoNamespaces |> List.contains op.Namespace.Value)
 
-    let getOpName context n =
-        if isCurrentOp context n then Directives.Self
-        elif needsFullPath context n then prependNamespaceString n
-        else n.Name.Value + "__"
-
     let getTypeParameters types =
         let findAll (t: ResolvedType) = t.ExtractAll (fun item -> item.Resolution |> function
             | QsTypeKind.TypeParameter tp -> seq{ yield tp }
@@ -105,8 +88,7 @@
     let hasTypeParameters types = not (getTypeParameters types).IsEmpty
 
     let justTheName context (n: QsQualifiedName) =
-        let name = userDefinedName None n.Name.Value
-        if needsFullPath context n then n.Namespace.Value + "." + name else name
+        if needsFullPath context n then n.Namespace.Value + "." + n.Name.Value else n.Name.Value
 
     let isGeneric context (n: QsQualifiedName) =
         if context.allCallables.ContainsKey n then
@@ -178,7 +160,7 @@
 
     and roslynCallableTypeName context (name:QsQualifiedName) =
         if not (context.allCallables.ContainsKey name) then
-            userDefinedName None name.Name.Value
+            name.Name.Value
         else
             let signature = context.allCallables.[name].Signature
             let tIn = signature.ArgumentType
@@ -411,16 +393,9 @@
 
         and buildNamedItem ex acc =
             match acc with
-            | LocalVariable name ->
-                let name' =
-                    match ex.ResolvedType.Resolution with
-                    | UserDefinedType udt ->
-                        name.Value |> userDefinedName (Some { Namespace = udt.Namespace; Name = udt.Name })
-                    | _ -> name.Value
-                buildExpression ex <|.|> ident name'
-            | _ ->
-                // TODO: Diagnostics
-                failwith "Invalid identifier for named item"
+            | LocalVariable name -> (buildExpression ex) <|.|> (``ident`` name.Value)
+// TODO: Diagnostics
+            | _ -> failwith "Invalid identifier for named item"
 
         and buildAddExpr (exType : ResolvedType) lhs rhs =
             match exType.Resolution |> QArrayType with
@@ -435,10 +410,16 @@
 
         and buildId id : ExpressionSyntax =
             match id with
-            | LocalVariable n -> n.Value |> ident :> ExpressionSyntax
-            | GlobalCallable n -> getOpName context n |> ident :> ExpressionSyntax
+            | LocalVariable n-> n.Value |> ``ident`` :> ExpressionSyntax
+            | GlobalCallable n ->
+                if isCurrentOp context n then
+                    Directives.Self |> ``ident`` :> ExpressionSyntax
+                elif needsFullPath context n then
+                    prependNamespaceString n |> ``ident`` :> ExpressionSyntax
+                else
+                    n.Name.Value |> ``ident`` :> ExpressionSyntax
+// TODO: Diagnostics
             | InvalidIdentifier ->
-                // TODO: Diagnostics
                 failwith "Received InvalidIdentifier"
 
         and buildCopyAndUpdateExpression (lhsEx : TypedExpression, accEx : TypedExpression, rhsEx) =
@@ -780,8 +761,8 @@
         override this.OnQubitScope (using:QsQubitScope) =
             let (alloc, release) =
                 match using.Kind with
-                | Allocate -> "Allocate__", "Release__"
-                | Borrow   -> "Borrow__", "Return__"
+                | Allocate -> ("Allocate", "Release")
+                | Borrow   -> ("Borrow", "Return")
             let rec removeDiscarded sym =
                 match sym with
                 | VariableName _         -> sym
@@ -867,13 +848,15 @@
         seeker.Namespaces.OnCallableDeclaration od |> ignore
         seeker.SharedState |> Seq.toList
 
+    let getOpName context n =
+        if needsFullPath context n then prependNamespaceString n
+        else if isCurrentOp context n then Directives.Self
+        else n.Name.Value
+
     let getTypeOfOp context (n: QsQualifiedName) =
         let name =
             let sameNamespace = match context.current with | None -> false | Some o -> o.Namespace = n.Namespace
-            let opName =
-                if sameNamespace
-                then userDefinedName None n.Name.Value
-                else "global::" + n.Namespace.Value + "." + userDefinedName None n.Name.Value
+            let opName = if sameNamespace then n.Name.Value else "global::" + n.Namespace.Value + "." + n.Name.Value
             if isGeneric context n then
                 let signature = context.allCallables.[n].Signature
                 let count = signature.TypeParameters.Length
@@ -894,12 +877,12 @@
                         "this" |> ``ident`` :> ExpressionSyntax
                     else
                         let signature = roslynCallableTypeName context n
-                        let factoryGet = (``ident`` "this" <|.|> ``ident`` "__Factory__" <|.|> (generic "Get" ``<<`` [ signature ] ``>>``))
+                        let factoryGet = (``ident`` "this" <|.|> ``ident`` "Factory" <|.|> (generic "Get" ``<<`` [ signature ] ``>>``))
                         (``invoke`` factoryGet ``(`` [ (getTypeOfOp context n) ] ``)``)
                 statement (lhs <-- rhs)
             operations
             |> List.map buildOne
-        ``method`` "void"  "__Init__" ``<<`` [] ``>>``
+        ``method`` "void"  "Init" ``<<`` [] ``>>``
             ``(`` parameters ``)``
             [  ``public``; ``override``  ]
             ``{`` body ``}``
@@ -996,10 +979,10 @@
         | Generated SelfInverse ->
             let adjointedBodyName =
                 match sp.Kind with
-                | QsAdjoint           -> "__Body__"
-                | QsControlledAdjoint -> "__ControlledBody__"
+                | QsAdjoint           -> "Body"
+                | QsControlledAdjoint -> "ControlledBody"
 //TODO: diagnostics.
-                | _ -> "__Body__"
+                | _ -> "Body"
             Some (``ident`` adjointedBodyName :> ExpressionSyntax)
         | _ ->
             None
@@ -1038,7 +1021,7 @@
 
         match body with
         | Some body ->
-            let bodyName = if bodyName = "Body" then "__Body__" else "__" + bodyName + "Body__"
+            let bodyName = if bodyName = "Body" then bodyName else bodyName + "Body"
             let impl =
                 ``property-arrow_get`` propertyType bodyName [``public``; ``override``]
                     ``get``
@@ -1290,7 +1273,7 @@
         let buildMethod t body =
             let baseType = (roslynTypeName context t)
             let args     = [ (``param`` "data" ``of`` (``type`` (roslynTypeName context t)) ) ]
-            ``arrow_method`` "IApplyData" (sprintf "__Data%s__" name) ``<<`` [] ``>>``
+            ``arrow_method`` "IApplyData" (sprintf "__data%s" name) ``<<`` [] ``>>``
                 ``(`` args ``)``
                 [``public``; ``override``]
                 ( Some ( ``=>`` body) )
@@ -1312,8 +1295,8 @@
         let name = function | ValidName n -> sprintf "__%s__" n.Value | InvalidName -> "__"
         signature.TypeParameters |> Seq.map name  |> Seq.sort |> Seq.toList
 
-    let findClassName (op: QsCallable)  =
-        let name = userDefinedName None op.FullName.Name.Value
+    let findClassName context (op: QsCallable)  =
+        let name = op.FullName.Name.Value
         let typeParameters = typeParametersNames op.Signature
         let nonGeneric = if typeParameters.IsEmpty then name else sprintf "%s<%s>" name (String.Join(",", typeParameters))
         (name, nonGeneric)
@@ -1363,7 +1346,7 @@
     // Builds the .NET class for the given operation.
     let buildOperationClass (globalContext:CodegenContext) (op: QsCallable) =
         let context = globalContext.setCallable op
-        let (name, nonGenericName) = findClassName op
+        let (name, nonGenericName) = findClassName context op
         let opNames = operationDependencies op
         let inType   = op.Signature.ArgumentType |> roslynTypeName context
         let outType  = op.Signature.ReturnType   |> roslynTypeName context
@@ -1441,7 +1424,7 @@
 
     let buildUdtClass (globalContext:CodegenContext) (udt: QsCustomType) =
         let context = globalContext.setUdt udt
-        let name = userDefinedName None udt.FullName.Name.Value
+        let name = udt.FullName.Name.Value
         let qsharpType = udt.Type
         let buildEmtpyConstructor =
             let baseTupleType =
@@ -1469,11 +1452,8 @@
             :> MemberDeclarationSyntax
         let buildNamedItemFields =
             let produceProperty (decl : LocalVariableDeclaration<NonNullable<_>>) valueExpr =
-                ``property-arrow_get``
-                    (roslynTypeName context decl.Type)
-                    (userDefinedName context.current decl.VariableName.Value)
-                    [ ``public`` ] ``get`` (``=>`` valueExpr)
-                :> MemberDeclarationSyntax
+                ``property-arrow_get`` (roslynTypeName context decl.Type) decl.VariableName.Value [ ``public`` ]
+                    ``get`` (``=>`` valueExpr) :> MemberDeclarationSyntax
             let rec buildProps current = function
                 | QsTuple items -> items |> Seq.mapi (fun i x -> buildProps (current <|.|> ``ident`` ("Item" + (i+1).ToString())) x) |> Seq.collect id
                 | QsTupleItem (Anonymous _) -> Seq.empty
