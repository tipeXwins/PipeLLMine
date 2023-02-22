--- pyquil/pyquil#174/after/Quil.g4	2022-01-10 16:02:54.000000000 +0000
+++ pyquil/pyquil#174/before/Quil.g4	2022-01-10 16:02:54.000000000 +0000
@@ -4,7 +4,7 @@
 // PARSER
 ////////////////////
 
-quil                : allInstr (NEWLINE+ allInstr)* EOF ;
+quil                : allInstr (NEWLINE+ allInstr)* NEWLINE* EOF ;
 
 allInstr            : defGate
                     | defCircuit
@@ -114,7 +114,7 @@
 // Numbers
 // We suffix -N onto these names so they don't conflict with already defined Python types
 
-number              : realN | imaginaryN | I | PI ;
+number              : realN | imaginaryN | I ;
 imaginaryN          : realN I ;
 realN               : floatN | intN ;
 
