--- BuggyCodes/detect_cycle.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/detect_cycle.py	2022-08-29 18:38:22.000000000 +0100
@@ -2,7 +2,7 @@
     hare = tortoise = node
 
     while True:
-        if hare.successor is None:
+        if hare is None or hare.successor is None:
             return False
 
         tortoise = tortoise.successor
@@ -12,16 +12,17 @@
             return True
 
 
-
 """
-Linked List Cycle Detection
-tortoise-hare
+def detect_cycle(node):
+    hare = tortoise = node
 
-Implements the tortoise-and-hare method of cycle detection.
+    while True:
+        if hare.successor is None or hare.successor.successor is None:
+            return False
 
-Input:
-    node: The head node of a linked list
+        tortoise = tortoise.successor
+        hare = hare.successor.successor
 
-Output:
-    Whether the linked list is cyclic
+        if hare is tortoise:
+            return True
 """
