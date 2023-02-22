--- BuggyCodes/rpn_eval.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/rpn_eval.py	2022-08-29 18:38:22.000000000 +0100
@@ -17,27 +17,32 @@
             a = stack.pop()
             b = stack.pop()
             stack.append(
-                op(token, a, b)
+                op(token, b, a)
             )
 
     return stack.pop()
 
-
-
 """
-Reverse Polish Notation
-
-Four-function calculator with input given in Reverse Polish Notation (RPN).
-
-Input:
-    A list of values and operators encoded as floats and strings
-
-Precondition:
-    all(
-        isinstance(token, float) or token in ('+', '-', '*', '/') for token in tokens
-    )
+def rpn_eval(tokens):
+    def op(symbol, a, b):
+        return {
+            '+': lambda a, b: a + b,
+            '-': lambda a, b: a - b,
+            '*': lambda a, b: a * b,
+            '/': lambda a, b: a / b
+        }[symbol](b, a)
+
+    stack = Stack()
+
+    for token in tokens:
+        if isinstance(token, float):
+            stack.push(token)
+        else:
+            a = stack.pop()
+            b = stack.pop()
+            stack.push(
+                op(token, a, b)
+            )
 
-Example:
-    >>> rpn_eval([3.0, 5.0, '+', 2.0, '/'])
-    4.0
+    return stack.pop()
 """
