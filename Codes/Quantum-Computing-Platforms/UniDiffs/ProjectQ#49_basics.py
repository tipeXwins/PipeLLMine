--- ProjectQ/ProjectQ#49/after/_basics.py	2022-01-10 16:02:54.000000000 +0000
+++ ProjectQ/ProjectQ#49/before/_basics.py	2022-01-10 16:02:54.000000000 +0000
@@ -170,10 +170,12 @@
         """
         qubits = self.make_tuple_of_qureg(qubits)
 
-        engines = [q.engine for reg in qubits for q in reg]
-        eng = engines[0]
-        assert all(e is eng for e in engines)
-        return Command(eng, self, qubits)
+        for i in range(len(qubits)):
+            for j in range(len(qubits[i]) - 1):
+                assert(qubits[i][j].engine == qubits[i][j + 1].engine)
+            if i < len(qubits) - 1:
+                assert(qubits[i][-1].engine == qubits[i + 1][0].engine)
+        return Command(qubits[0][0].engine, self, qubits)
 
     def __or__(self, qubits):
         """ Operator| overload which enables the syntax Gate | qubits.
