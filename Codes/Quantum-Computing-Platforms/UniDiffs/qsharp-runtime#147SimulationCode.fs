--- qsharp-runtime/qsharp-runtime#147/after/SimulationCode.fs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#147/before/SimulationCode.fs	2022-01-10 16:02:54.000000000 +0000
@@ -787,8 +787,9 @@
                 releases    
                 
             let symbols = removeDiscarded using.Binding.Lhs
-            let deallocationFlagName = nextArgName()
-            let deallocationFlagIdentifier = ``ident`` deallocationFlagName
+            let exDispatchInfoName = nextArgName() 
+            let exDispatchInfoHandle = ``ident`` exDispatchInfoName
+            let caughtEx = nextArgName()
 
             // allocations and deallocations
             let lhs = symbols |> buildSymbolNames id
@@ -799,14 +800,18 @@
             // To force that exceptions thrown during the execution of the allocation scope take precedence over the ones thrown upon release
             // we catch all exceptions in a variable and throw after releaseing if necessary. 
 
-            let deallocationFlagDeclaration = ``typed var`` "bool" deallocationFlagName (``:=`` ``true`` |> Some) |> ``#line hidden`` :> StatementSyntax
+            let exceptionHandle = ``typed var`` "System.Runtime.ExceptionServices.ExceptionDispatchInfo" exDispatchInfoName (``:=`` ``null`` |> Some) |> ``#line hidden`` :> StatementSyntax
             
             let catch = 
-                let setFlagToFalse = deallocationFlagIdentifier <-- ``false`` |> statement
-                ``catch`` None [setFlagToFalse; ``throw`` None] // use standard mechanism to rethrow the exception by using "throw;"
-            let finallyBlock = [``if`` ``(`` deallocationFlagIdentifier ``)`` deallocation None]
+                let setEx = exDispatchInfoHandle <-- ``invoke`` (``ident`` "System.Runtime.ExceptionServices.ExceptionDispatchInfo.Capture") ``(`` [``ident`` caughtEx] ``)`` |> statement
+                ``catch`` (Some ("Exception", caughtEx)) [setEx; ``throw`` None] // use standard mechanism to rethrow the exception by using "throw;"
+            let finallyBlock = 
+                let condition = exDispatchInfoHandle .!=. ``null``
+                let rethrow = ``invoke`` (exDispatchInfoHandle <|.|> (``ident`` "Throw")) ``(`` [] ``)`` |> statement // rethrow that keeps the call stack unchanged
+                let throwIfNecessary = ``if`` ``(`` condition ``)`` [rethrow] None 
+                throwIfNecessary :: deallocation
             let body = ``try`` (buildBlock using.Body) [catch |> ``#line hidden``] (``finally`` finallyBlock |> ``#line hidden`` |> Some)
-            let statements = [allocation; deallocationFlagDeclaration; body]
+            let statements = [allocation; exceptionHandle; body]
 
             // Put all statements into their own brackets so variable names have their own context.
             // Make sure the brackets get #line hidden:
