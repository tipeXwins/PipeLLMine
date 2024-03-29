--- BuggyCodes/wrap.py	2022-08-29 18:38:22.000000000 +0100
+++ CorrectCodes/wrap.py	2022-08-29 18:38:22.000000000 +0100
@@ -1,3 +1,4 @@
+
 def wrap(text, cols):
     lines = []
     while len(text) > cols:
@@ -7,22 +8,6 @@
         line, text = text[:end], text[end:]
         lines.append(line)
 
+    lines.append(text)
     return lines
 
-"""
-Wrap Text
-
-Given a long string and a column width, break the string on spaces into a list of lines such that each line is no longer than the column width.
-
-Input:
-    text: The starting text.
-    cols: The target column width, i.e. the maximum length of any single line after wrapping.
-
-Precondition:
-    cols > 0.
-
-Output:
-    An ordered list of strings, each no longer than the column width, such that the concatenation of the strings returns the original text,
-and such that no word in the original text is broken into two parts unless necessary.  The original amount of spaces are preserved (e.g. spaces
-at the start or end of each line aren't trimmed.),Wrapping Text
-"""
