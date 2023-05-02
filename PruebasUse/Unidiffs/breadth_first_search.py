--- BuggyCodes/breadth_first_search.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/breadth_first_search.py	2022-08-29 18:38:22.000000000 +0100
@@ -8,7 +8,7 @@
     nodesseen = set()
     nodesseen.add(startnode)
 
-    while True:
+    while queue:
         node = queue.popleft()
 
         if node is goalnode:
@@ -20,15 +20,69 @@
     return False
 
 
-
 """
-Breadth-First Search
+from collections import deque as Queue
+
+def breadth_first_search(startnode, goalnode):
+    queue = Queue()
+    queue.append(startnode)
+
+    nodesseen = set()
+    nodesseen.add(startnode)
+
+    while len(queue):
+        node = queue.popleft()
+
+        if node is goalnode:
+            return True
+        else:
+            queue.extend(node for node in node.successors if node not in nodesseen)
+            nodesseen.update(node.successors)
+
+    return False
+
+
+
+from collections import deque as Queue
 
+def breadth_first_search(startnode, goalnode):
+    queue = Queue()
+    queue.append(startnode)
 
-Input:
-    startnode: A digraph node
-    goalnode: A digraph node
+    nodesseen = set()
+    nodesseen.add(startnode)
+
+    while len(queue) > 0:
+        node = queue.popleft()
+
+        if node is goalnode:
+            return True
+        else:
+            queue.extend(node for node in node.successors if node not in nodesseen)
+            nodesseen.update(node.successors)
+
+    return False
+
+
+
+from collections import deque as Queue
+
+def breadth_first_search(startnode, goalnode):
+    queue = Queue()
+    queue.append(startnode)
+
+    nodesseen = set()
+    nodesseen.add(startnode)
+
+    while len(queue) != 0:
+        node = queue.popleft()
+
+        if node is goalnode:
+            return True
+        else:
+            queue.extend(node for node in node.successors if node not in nodesseen)
+            nodesseen.update(node.successors)
+
+    return False
 
-Output:
-    Whether goalnode is reachable from startnode
 """
