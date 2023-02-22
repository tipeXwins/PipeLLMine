--- BuggyCodes/shunting_yard.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/shunting_yard.py	2022-08-29 18:38:22.000000000 +0100
@@ -15,34 +15,10 @@
         else:
             while opstack and precedence[token] <= precedence[opstack[-1]]:
                 rpntokens.append(opstack.pop())
+            opstack.append(token)
 
     while opstack:
         rpntokens.append(opstack.pop())
 
     return rpntokens
 
-
-"""
-Infix to RPN Conversion
-shunting-yard
-
-
-Uses Dijkstra's shunting-yard algorithm to transform infix notation into equivalent Reverse Polish Notation.
-
-Input:
-    tokens: A list of tokens in infix notation
-
-Precondition:
-    all(isinstance(token, int) or token in '+-*/' for token in tokens)
-
-Output:
-    The input tokens reordered into Reverse Polish Notation
-
-Examples:
-    >>> shunting_yard([10, '-', 5, '-', 2])
-    [10, 5, '-', 2, '-']
-    >>> shunting_yard([34, '-', 12, '/', 5])
-    [34, 12, 5, '/' ,'-']
-    >>> shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13])
-    [4, 9, 9, '*', '+', 10, '-', 13, '+']
-"""
