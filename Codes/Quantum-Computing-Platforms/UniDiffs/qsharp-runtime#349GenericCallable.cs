--- qsharp-runtime/qsharp-runtime#349/after/GenericCallable.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#349/before/GenericCallable.cs	2022-01-10 16:02:54.000000000 +0000
@@ -54,7 +54,7 @@
             _controlled = new Lazy<GenericControlled>(() => new GenericControlled(this));
         }
 
-        public override void __Init__() { }
+        public override void Init() { }
 
         public Type OperationType { get; }
 
@@ -103,12 +103,12 @@
                 op = FindClosedType(I, O);
             }
 
-            var get = this.__Factory__.GetType()
+            var get = this.Factory.GetType()
                 .GetMethod("Get", new Type[0]);
 
             var result = get
                 .MakeGenericMethod(typeof(ICallable), op)
-                .Invoke(this.__Factory__, new object[] { })
+                .Invoke(this.Factory, new object[] { })
                 as ICallable;
 
             return result;
@@ -162,7 +162,7 @@
 
             // Get the list of Parameters of the Invoke method of the Body of the operation:
             var expectedParameters = this.OperationType
-                .GetProperty("__Body__").PropertyType
+                .GetProperty("Body").PropertyType
                 .GetMethod("Invoke").GetParameters();
 
             // Tuple in...
@@ -171,7 +171,7 @@
 
             // Tuple out...
             var expectedReturn = this.OperationType
-                .GetProperty("__Body__").PropertyType
+                .GetProperty("Body").PropertyType
                 .GetMethod("Invoke").ReturnType;
             Resolve(expectedReturn, O, typeArgs);
 
