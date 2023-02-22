--- qsharp-runtime/qsharp-runtime#278/after/DepthCounter.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#278/before/DepthCounter.cs	2022-01-10 16:02:54.000000000 +0000
@@ -87,8 +87,8 @@
             OperationCallRecord caller = operationCallStack.Peek();
             HashedString callerName = caller.OperationName;
 
-            caller.ReleasedQubitsAvailableTime = Max(opRec.ReleasedQubitsAvailableTime, caller.ReleasedQubitsAvailableTime);
-            caller.ReturnedQubitsAvailableTime = Max(opRec.ReturnedQubitsAvailableTime, caller.ReturnedQubitsAvailableTime);
+            caller.ReleasedQubitsAvailableTime = Max(opRec.ReleasedQubitsAvailableTime, caller.ReleasedQubitsAvailableTime );
+            caller.ReleasedQubitsAvailableTime = Max(opRec.ReleasedQubitsAvailableTime, caller.ReleasedQubitsAvailableTime );
 
             double[] metrics =
                 StatisticsRecord( 
