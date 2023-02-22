--- qsharp-compiler/qsharp-compiler#987/after/ScopeManager.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#987/before/ScopeManager.cs	2022-01-10 16:02:54.000000000 +0000
@@ -25,8 +25,7 @@
     {
         private class Scope
         {
-            private readonly Action<Func<ITypeRef, string?>, (IValue, bool)[]> increaseCounts;
-            private readonly Action<Func<ITypeRef, string?>, (IValue, bool)[]> decreaseCounts;
+            private readonly ScopeManager parent;
 
             /// <summary>
             /// Maps variable names to the corresponding value.
@@ -50,12 +49,11 @@
             /// Contains the values that require invoking a release function upon closing the scope,
             /// as well as the name of the release function to invoke.
             /// </summary>
-            private readonly List<Action> requiredReleases = new List<Action>();
+            private readonly List<(IValue, string)> requiredReleases = new List<(IValue, string)>();
 
-            public Scope(Action<Func<ITypeRef, string?>, (IValue, bool)[]> increaseCounts, Action<Func<ITypeRef, string?>, (IValue, bool)[]> decreaseCounts)
+            public Scope(ScopeManager parent)
             {
-                this.increaseCounts = increaseCounts;
-                this.decreaseCounts = decreaseCounts;
+                this.parent = parent;
             }
 
             private static bool ValueEquals((IValue, bool) tracked, IValue expected) =>
@@ -137,15 +135,14 @@
                 // Since the value is necessarily created in the current or a parent scope,
                 // it won't go out of scope before the variable does.
                 // There is hence no need to increase the reference count if the variable is never rebound.
-                var change = new[] { (value, true) }; // true refers to whether the change also applies to inner items
-                this.increaseCounts(AliasCountUpdateFunctionForType, change);
+                this.parent.ModifyCounts(this.parent.AliasCountUpdateFunctionForType, this.parent.plusOne, value, recurIntoInnerItems: true);
                 if (value is PointerValue)
                 {
                     // If the variable can be rebound, however, then updating an item via a copy-and-reassign statement
                     // potentially leads to the updated item(s) being unreferenced in an inner scope, i.e. before the
                     // pending reference count increases of this scope are applied.
                     // We hence need to make sure to increase the reference count immediately when binding to a mutable variable.
-                    this.increaseCounts(ReferenceCountUpdateFunctionForType, change);
+                    this.parent.ModifyCounts(this.parent.ReferenceCountUpdateFunctionForType, this.parent.plusOne, value, recurIntoInnerItems: true);
                 }
             }
 
@@ -158,7 +155,7 @@
             /// </summary>
             public void RegisterValue(IValue value, bool shallow = false)
             {
-                if (RequiresReferenceCount(value.LlvmType))
+                if (this.parent.RequiresReferenceCount(value.LlvmType))
                 {
                     this.requiredUnreferences.Add((LoadValue(value), !shallow));
                 }
@@ -168,11 +165,8 @@
             /// Adds the release function for the given value to the list of releases that need to be executed when closing or exiting the scope.
             /// If the given value to register is a pointer, recursively loads its content such that the release is applied to the loaded value.
             /// </summary>
-            public void RegisterRelease(IValue value, Action<IValue> releaseFunction)
-            {
-                var loadedValue = LoadValue(value);
-                this.requiredReleases.Add(() => releaseFunction(loadedValue));
-            }
+            public void RegisterRelease(IValue value, string releaseFunction) =>
+                this.requiredReleases.Add((LoadValue(value), releaseFunction));
 
             /// <summary>
             /// Adds the given value to the list of values which have been referenced.
@@ -180,7 +174,7 @@
             /// </summary>
             internal void ReferenceValue(IValue value, bool recurIntoInnerItems)
             {
-                if (RequiresReferenceCount(value.LlvmType))
+                if (this.parent.RequiresReferenceCount(value.LlvmType))
                 {
                     this.pendingReferences.Add((LoadValue(value), recurIntoInnerItems));
                 }
@@ -199,7 +193,12 @@
             {
                 var pending = this.pendingReferences.ToArray();
                 this.pendingReferences.Clear();
-                this.increaseCounts(ReferenceCountUpdateFunctionForType, pending);
+                this.parent.ModifyCounts(this.parent.ReferenceCountUpdateFunctionForType, this.parent.plusOne, pending);
+            }
+            internal void MigratePendingReferences(Scope scope)
+            {
+                scope.pendingReferences.AddRange(this.pendingReferences);
+                this.pendingReferences.Clear();
             }
 
             /// <summary>
@@ -218,7 +217,7 @@
             /// </summary>
             internal void UnreferenceValue(IValue value, bool recurIntoInnerItems)
             {
-                if (RequiresReferenceCount(value.LlvmType))
+                if (this.parent.RequiresReferenceCount(value.LlvmType))
                 {
                     this.requiredUnreferences.Add((LoadValue(value), recurIntoInnerItems));
                 }
@@ -231,26 +230,32 @@
             /// </summary>
             internal bool TryRemoveValue(IValue value) =>
                 TryRemoveValue(this.requiredUnreferences, tracked => ValueEquals(tracked, value));
+            internal void ExecutePendingCalls(bool applyReferences = true) =>
+                ExecutePendingCalls(this.parent, applyReferences, this);
 
-            internal void ExecutePendingCalls(params Scope[] parentScopes)
+            internal static void ExecutePendingCalls(ScopeManager parent, bool forceApplyReferences, params Scope[] scopes)
             {
+                if (!scopes.Any())
+                {
+                    return;
+                }
                 // Not the most efficient way to go about this, but it will do for now.
 
-                var allScopes = parentScopes.Prepend(this);
-                var pendingAliasCounts = allScopes.SelectMany(s => s.variables).Select(kv => (kv.Value, true)).ToArray();
+                var pendingAliasCounts = scopes.SelectMany(s => s.variables).Select(kv => (kv.Value, true)).ToArray();
+                var appliesUnreferences = pendingAliasCounts.Any(v => v.Value is PointerValue) || scopes.Any(s => s.requiredUnreferences.Any());
 
-                var pendingReferences = this.ClearPendingReferences()
-                    .Concat(parentScopes.SelectMany(scope => scope.pendingReferences))
-                    .ToList();
+                var pendingReferences = forceApplyReferences || appliesUnreferences
+                    ? scopes.First().ClearPendingReferences()
+                    : new List<(IValue, bool)>();
 
-                var pendingUnreferences = allScopes
+                var pendingUnreferences = scopes
                     .SelectMany(s => s.requiredUnreferences)
                     .Concat(pendingAliasCounts.Where(v => v.Value is PointerValue))
-                    .SelectMany(v => Expand(ReferenceCountUpdateFunctionForType, v.Item1, v.Item2, pendingReferences))
+                    .SelectMany(v => Expand(parent.ReferenceCountUpdateFunctionForType, v.Item1, v.Item2, pendingReferences))
                     .ToList();
 
                 pendingReferences = pendingReferences
-                    .SelectMany(v => Expand(ReferenceCountUpdateFunctionForType, v.Item1, v.Item2))
+                    .SelectMany(v => Expand(parent.ReferenceCountUpdateFunctionForType, v.Item1, v.Item2))
                     .ToList();
 
                 var lookup1 = pendingReferences.ToLookup(x => (x.Item1.Value, x.Item2));
@@ -263,13 +268,14 @@
                     Debug.Assert(removedFromRefs && removedFromUnrefs);
                 }
 
-                this.increaseCounts(ReferenceCountUpdateFunctionForType, pendingReferences.ToArray());
-                this.decreaseCounts(AliasCountUpdateFunctionForType, pendingAliasCounts);
-                this.decreaseCounts(ReferenceCountUpdateFunctionForType, pendingUnreferences.ToArray());
+                parent.ModifyCounts(parent.ReferenceCountUpdateFunctionForType, parent.plusOne, pendingReferences.ToArray());
+                parent.ModifyCounts(parent.AliasCountUpdateFunctionForType, parent.minusOne, pendingAliasCounts);
+                parent.ModifyCounts(parent.ReferenceCountUpdateFunctionForType, parent.minusOne, pendingUnreferences.ToArray());
 
-                foreach (var release in allScopes.SelectMany(s => s.requiredReleases))
+                foreach (var (value, funcName) in scopes.SelectMany(s => s.requiredReleases))
                 {
-                    release();
+                    var func = parent.sharedState.GetOrCreateRuntimeFunction(funcName);
+                    parent.sharedState.CurrentBuilder.Call(func, value.Value);
                 }
             }
         }
@@ -308,7 +314,7 @@
         /// </summary>
         /// <param name="t">The LLVM type</param>
         /// <returns>The name of the function to update the alias count for this type</returns>
-        private static string? AliasCountUpdateFunctionForType(ITypeRef t)
+        private string? AliasCountUpdateFunctionForType(ITypeRef t)
         {
             if (t.IsPointer)
             {
@@ -333,7 +339,7 @@
         /// </summary>
         /// <param name="t">The LLVM type</param>
         /// <returns>The name of the function to update the reference count for this type</returns>
-        private static string? ReferenceCountUpdateFunctionForType(ITypeRef t)
+        private string? ReferenceCountUpdateFunctionForType(ITypeRef t)
         {
             if (t.IsPointer)
             {
@@ -444,15 +450,6 @@
             }
         }
 
-        private void ExecutePendingCalls(bool keepCurrentScope = false)
-        {
-            var current = keepCurrentScope ? this.scopes.Peek() : this.scopes.Pop();
-            if (current.HasPendingReferences && keepCurrentScope)
-            {
-                throw new InvalidOperationException("scope contains pending calls to increase reference counts");
-            }
-            current.ExecutePendingCalls();
-        }
         // public and internal methods
 
         /// <summary>
@@ -463,10 +460,10 @@
         /// The reason is that for optimization purposes we omit increasing (and subsequently decreasing) counts when possible.
         /// Some of these optimizations rely on the restrictions enforced by the Q# language.
         /// </summary>
-        public void OpenScope() =>
-            this.scopes.Push(new Scope(
-                increaseCounts: (fct, items) => this.ModifyCounts(fct, this.plusOne, items),
-                decreaseCounts: (fct, items) => this.ModifyCounts(fct, this.minusOne, items)));
+        public void OpenScope()
+        {
+            this.scopes.Push(new Scope(this));
+        }
 
         /// <summary>
         /// Closes the current scope by popping it off of the stack.
@@ -481,35 +478,43 @@
         /// <exception cref="InvalidOperationException">The scope has pending calls to increase the reference count for values</exception>
         public void CloseScope(bool isTerminated)
         {
+            var scope = this.scopes.Peek();
             if (!isTerminated)
             {
-                this.ExecutePendingCalls();
+                scope.ExecutePendingCalls();
             }
-            else
+            if (scope.HasPendingReferences)
             {
-                var scope = this.scopes.Pop();
-                if (scope.HasPendingReferences)
-                {
-                    throw new InvalidOperationException("cannot close scope that has pending calls to increase reference counts");
-                }
+                throw new InvalidOperationException("cannot close scope that has pending calls to increase reference counts");
             }
+            _ = this.scopes.Pop();
         }
 
         /// <summary>
         /// Closes the current scope by popping it off of the stack.
         /// Emits the queued calls to unreference, release, and/or decrease the alias counts for values going out of scope.
         /// Increases the reference count of the returned value by 1, either by omitting to unreference it or by explicitly increasing it.
+        /// Delays applying pending calls to increase reference counts if no values are unreferenced unless allowDelayReferencing is set to false.
         /// IMPORTANT:
         /// This function is meant to be used only for closing Q# scopes, and *not* for blocks that have been inserted
         /// only as part of QIR generation such as e.g. for-loops to modify reference and alias counts.
         /// The reason is that for optimization purposes we omit increasing (and subsequently decreasing) counts when possible.
         /// Some of these optimizations rely on the restrictions enforced by the Q# language.
         /// </summary>
-        public void CloseScope(IValue returned)
+        public void CloseScope(IValue returned, bool allowDelayReferencing = true)
         {
+            var scope = this.scopes.Peek();
             this.IncreaseReferenceCount(returned);
-            this.ExecutePendingCalls();
+            scope.ExecutePendingCalls(applyReferences: !allowDelayReferencing);
+            scope = this.scopes.Pop();
+
+            if (allowDelayReferencing)
+            {
+                scope.MigratePendingReferences(this.scopes.Peek());
+            }
         }
+        internal void ApplyPendingReferences() =>
+            this.scopes.Peek().ApplyPendingReferences();
 
         /// <summary>
         /// Exits the current scope by emitting the calls to unreference, release,
@@ -524,14 +529,22 @@
         /// Some of these optimizations rely on the restrictions enforced by the Q# language.
         /// </summary>
         /// <exception cref="InvalidOperationException">The scope has pending calls to increase the reference count for values</exception>
-        public void ExitScope() =>
-            this.ExecutePendingCalls(keepCurrentScope: true);
-        internal void ApplyPendingReferences() =>
-            this.scopes.Peek().ApplyPendingReferences();
+        public void ExitScope(bool isTerminated)
+        {
+            var scope = this.scopes.Peek();
+            if (scope.HasPendingReferences)
+            {
+                throw new InvalidOperationException("cannot exit scope that has pending calls to increase reference counts");
+            }
+            if (!isTerminated)
+            {
+                scope.ExecutePendingCalls();
+            }
+        }
 
         /// <returns>True if reference counts are tracked for values of the given type.</returns>
-        internal static bool RequiresReferenceCount(ITypeRef type) =>
-            ReferenceCountUpdateFunctionForType(type) != null;
+        internal bool RequiresReferenceCount(ITypeRef type) =>
+            this.ReferenceCountUpdateFunctionForType(type) != null;
 
         /// <summary>
         /// Adds a call to a runtime library function to increase the reference count for the given value if necessary.
@@ -558,7 +571,7 @@
         internal void UpdateReferenceCount(Value change, IValue value, bool shallow = false)
         {
             this.scopes.Peek().ApplyPendingReferences();
-            this.ModifyCounts(ReferenceCountUpdateFunctionForType, change, value, !shallow);
+            this.ModifyCounts(this.ReferenceCountUpdateFunctionForType, change, value, !shallow);
         }
 
         /// <summary>
@@ -580,8 +593,8 @@
         /// <param name="value">The value which is assigned to a handle</param>
         internal void IncreaseAliasCount(IValue value, bool shallow = false)
         {
-            this.ModifyCounts(ReferenceCountUpdateFunctionForType, this.plusOne, value, !shallow);
-            this.ModifyCounts(AliasCountUpdateFunctionForType, this.plusOne, value, !shallow);
+            this.ModifyCounts(this.ReferenceCountUpdateFunctionForType, this.plusOne, value, !shallow);
+            this.ModifyCounts(this.AliasCountUpdateFunctionForType, this.plusOne, value, !shallow);
         }
 
         /// <summary>
@@ -593,7 +606,7 @@
         internal void DecreaseAliasCount(IValue value, bool shallow = false)
         {
             this.DecreaseReferenceCount(value, shallow);
-            this.ModifyCounts(AliasCountUpdateFunctionForType, this.minusOne, value, !shallow);
+            this.ModifyCounts(this.AliasCountUpdateFunctionForType, this.minusOne, value, !shallow);
         }
 
         /// <summary>
@@ -604,7 +617,7 @@
         /// <param name="change">The amount by which to change the alias count given as i64</param>
         /// <param name="value">The value for which to change the alias count</param>
         internal void UpdateAliasCount(Value change, IValue value, bool shallow = false) =>
-            this.ModifyCounts(AliasCountUpdateFunctionForType, change, value, !shallow);
+            this.ModifyCounts(this.AliasCountUpdateFunctionForType, change, value, !shallow);
 
         /// <summary>
         /// Registers the given value with the current scope, such that a call to a suitable runtime library function
@@ -621,12 +634,11 @@
         /// </summary>
         public void RegisterAllocatedQubits(IValue value)
         {
-            var releaseFunctionName =
+            var releaser =
                 Types.IsArray(value.LlvmType) ? RuntimeLibrary.QubitReleaseArray :
                 Types.IsQubit(this.sharedState.Types.Qubit) ? RuntimeLibrary.QubitRelease :
                 throw new ArgumentException("AddQubitValue expects an argument of type Qubit or Qubit[]");
-            var release = this.sharedState.GetOrCreateRuntimeFunction(releaseFunctionName);
-            this.scopes.Peek().RegisterRelease(value, loaded => this.sharedState.CurrentBuilder.Call(release, loaded.Value));
+            this.scopes.Peek().RegisterRelease(value, releaser);
         }
 
         /// <summary>
@@ -701,8 +713,9 @@
             // d) We can't modify the pending calls; they may be used by other execution paths that
             //    don't return the same value.
 
+            var currentScopes = this.scopes.ToArray();
             this.IncreaseReferenceCount(returned);
-            this.scopes.Peek().ExecutePendingCalls(this.scopes.Skip(1).ToArray());
+            Scope.ExecutePendingCalls(this, true, currentScopes);
         }
     }
 }
