--- qsharp-compiler/qsharp-compiler#1000/after/Context.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-compiler/qsharp-compiler#1000/before/Context.cs	2022-01-10 16:02:54.000000000 +0000
@@ -120,43 +120,21 @@
 
         #region Control flow context tracking
 
-        private int uniqueControlFlowId = 0;
+        internal bool IsWithinLoop = false;
 
-        private readonly Stack<int> branchIds = new Stack<int>(new[] { 0 });
-        internal int CurrentBranch => this.branchIds.Peek();
-        internal bool IsOpenBranch(int id) => this.branchIds.Contains(id);
+        private (int, Stack<int>) branchIds = (0, new Stack<int>(new[] { 0 }));
+        internal int CurrentBranch => this.branchIds.Item2.Peek();
+        internal bool IsOpenBranch(int id) => this.branchIds.Item2.Contains(id);
 
         internal void StartBranch()
         {
-            this.uniqueControlFlowId += 1;
-            this.branchIds.Push(this.uniqueControlFlowId);
+            var (lastUsedId, stack) = this.branchIds;
+            stack.Push(lastUsedId + 1);
+            this.branchIds = (stack.Peek(), stack);
         }
 
         internal void EndBranch() =>
-            this.branchIds.Pop();
-        private readonly Stack<int> loopIds = new Stack<int>();
-        internal bool IsWithinLoop => this.loopIds.Any();
-        internal bool IsWithinCurrentLoop(int branchId)
-        {
-            if (!this.loopIds.TryPeek(out var currentLoopId))
-            {
-                return false;
-            }
-            var branchesWithinCurrentLoop = this.branchIds.TakeWhile(id => id >= currentLoopId);
-            return branchesWithinCurrentLoop.Contains(branchId);
-        }
-        internal void StartLoop()
-        {
-            // We need to mark the loop and also mark the branching
-            // to ensure that pointers are properly loaded when needed.
-            this.StartBranch();
-            this.loopIds.Push(this.CurrentBranch);
-        }
-        internal void EndLoop()
-        {
-            this.loopIds.Pop();
-            this.EndBranch();
-        }
+            this.branchIds.Item2.Pop();
 
         internal bool IsInlined => this.inlineLevels.Any();
 
@@ -1174,39 +1152,37 @@
             this.CurrentBuilder.Branch(condition, trueBlock, falseBlock);
             var entryBlock = this.CurrentBlock!;
 
-            Value ProcessConditionalBlock(BasicBlock block, Func<IValue>? evaluate)
+            IValue ProcessBlock(Func<IValue>? evaluate)
             {
-                this.SetCurrentBlock(block);
-                this.StartBranch();
-                IValue evaluated;
                 if (increaseReferenceCount)
                 {
                     this.ScopeMgr.OpenScope();
-                    evaluated = evaluate?.Invoke() ?? defaultValue!;
+                    var evaluated = evaluate?.Invoke() ?? defaultValue!;
                     this.ScopeMgr.CloseScope(evaluated); // forces that the ref count is increased within the branch
+                    return evaluated;
                 }
                 else
                 {
-                    evaluated = evaluate?.Invoke() ?? defaultValue!;
+                    return evaluate?.Invoke() ?? defaultValue!;
                 }
-                var res = evaluated.Value;
-                this.EndBranch();
-                this.CurrentBuilder.Branch(contBlock);
-                return res;
             }
 
             var (evaluatedOnTrue, afterTrue) = (defaultValue?.Value, entryBlock);
             if (requiresTrueBlock)
             {
-                var onTrue = ProcessConditionalBlock(trueBlock, onCondTrue);
-                (evaluatedOnTrue, afterTrue) = (onTrue, this.CurrentBlock!);
+                this.SetCurrentBlock(trueBlock);
+                var onTrue = ProcessBlock(onCondTrue);
+                this.CurrentBuilder.Branch(contBlock);
+                (evaluatedOnTrue, afterTrue) = (onTrue.Value, this.CurrentBlock!);
             }
 
             var (evaluatedOnFalse, afterFalse) = (defaultValue?.Value, entryBlock);
             if (requiresFalseBlock)
             {
-                var onFalse = ProcessConditionalBlock(falseBlock, onCondFalse);
-                (evaluatedOnFalse, afterFalse) = (onFalse, this.CurrentBlock!);
+                this.SetCurrentBlock(falseBlock);
+                var onFalse = ProcessBlock(onCondFalse);
+                this.CurrentBuilder.Branch(contBlock);
+                (evaluatedOnFalse, afterFalse) = (onFalse.Value, this.CurrentBlock!);
             }
 
             this.SetCurrentBlock(contBlock);
@@ -1370,9 +1346,12 @@
         /// <param name="loop">The loop to execute</param>
         internal void ExecuteLoop(BasicBlock continuation, Action loop)
         {
-            this.StartLoop();
+            bool withinOuterLoop = this.IsWithinLoop;
+            this.IsWithinLoop = true;
+            this.StartBranch();
             loop();
-            this.EndLoop();
+            this.EndBranch();
+            this.IsWithinLoop = withinOuterLoop;
             this.SetCurrentBlock(continuation);
         }
 
