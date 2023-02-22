--- pyquil/pyquil#710/after/paulis.py	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#710/before/paulis.py	2022-01-10 16:02:54.000000000 +0000
@@ -25,7 +25,7 @@
 from pyquil.quilatom import QubitPlaceholder
 
 from .quil import Program
-from .gates import I, H, RZ, RX, CNOT, X, PHASE, QUANTUM_GATES
+from .gates import H, RZ, RX, CNOT, X, PHASE, QUANTUM_GATES
 from numbers import Number
 from collections import Sequence, OrderedDict
 import warnings
@@ -712,13 +712,7 @@
 
 
 def is_identity(term):
-    if isinstance(term, PauliTerm):
-        return (len(term) == 0) and (not np.isclose(term.coefficient, 0))
-    elif isinstance(term, PauliSum):
-        return (len(term.terms) == 1) and (len(term.terms[0]) == 0) and \
-               (not np.isclose(term.terms[0].coefficient, 0))
-    else:
-        raise TypeError("is_identity only checks PauliTerms and PauliSum objects!")
+    return len(term) == 0
 
 
 def exponentiate(term: PauliTerm):
@@ -753,8 +747,6 @@
             prog.inst(PHASE(-param * coeff, 0))
             prog.inst(X(0))
             prog.inst(PHASE(-param * coeff, 0))
-        elif is_zero(term):
-            pass
         else:
             prog += _exponentiate_general_case(term, param)
         return prog
@@ -878,9 +870,15 @@
     :rtype: bool
     """
     if isinstance(pauli_object, PauliTerm):
-        return np.isclose(pauli_object.coefficient, 0)
+        if pauli_object.id() == '':
+            return True
+        else:
+            return False
     elif isinstance(pauli_object, PauliSum):
-        return len(pauli_object.terms) == 1 and np.isclose(pauli_object.terms[0].coefficient, 0)
+        if len(pauli_object.terms) == 1 and pauli_object.terms[0].id() == '':
+            return True
+        else:
+            return False
     else:
         raise TypeError("is_zero only checks PauliTerms and PauliSum objects!")
 
