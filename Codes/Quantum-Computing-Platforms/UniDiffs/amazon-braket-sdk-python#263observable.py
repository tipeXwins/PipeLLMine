--- amazon-braket-sdk-python/amazon-braket-sdk-python#263/after/observable.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#263/before/observable.py	2022-01-10 16:02:54.000000000 +0000
@@ -71,6 +71,8 @@
         setattr(cls, observable.__name__, observable)
 
     def __matmul__(self, other) -> Observable.TensorProduct:
+        if isinstance(other, Observable.TensorProduct):
+            return other.__rmatmul__(self)
         if isinstance(other, Observable):
             return Observable.TensorProduct([self, other])
 
