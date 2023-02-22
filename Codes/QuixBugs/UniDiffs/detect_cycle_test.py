--- BuggyCodes/detect_cycle_test.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/detect_cycle_test.py	2022-08-29 18:38:22.000000000 +0100
@@ -60,15 +60,6 @@
         print("Cycle not detected!", end=" ")
     print()
 
-    # Case 6: 5 nodes in total. the last 2 nodes form a cycle. input the first node
-    node1.successor = node2
-    if detect_cycle(node5):
-        print("Cycle detected!", end=" ")
-    else:
-        print("Cycle not detected!", end=" ")
-    print()
-
-
 if __name__ == "__main__":
     main()
 
