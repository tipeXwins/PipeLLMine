--- qsharp-runtime/qsharp-runtime#349/after/EntryPoint.fs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/EntryPoint.fs	2022-01-10 16:02:54.000000000 +0000
@@ -112,9 +112,7 @@
 
 /// A tuple of the callable's name, argument type name, and return type name.
 let private callableTypeNames context (callable : QsCallable) =
-    let callableName =
-        SimulationCode.userDefinedName None callable.FullName.Name.Value
-        |> sprintf "global::%s.%s" callable.FullName.Namespace.Value
+    let callableName = sprintf "global::%s.%s" callable.FullName.Namespace.Value callable.FullName.Name.Value
     let argTypeName = SimulationCode.roslynTypeName context callable.Signature.ArgumentType
     let returnTypeName = SimulationCode.roslynTypeName context callable.Signature.ReturnType
     callableName, argTypeName, returnTypeName
