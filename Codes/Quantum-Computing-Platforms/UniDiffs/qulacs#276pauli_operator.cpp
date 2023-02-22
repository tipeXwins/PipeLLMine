--- qulacs/qulacs#276/after/pauli_operator.cpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#276/before/pauli_operator.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -35,16 +35,8 @@
     std::string pauli_str;
     UINT index, pauli_type=0;
     while(!ss.eof()){
-        pauli_str.clear();
-        index = UINT_MAX - 1;
         ss >> pauli_str >> index;
-        if (index == UINT_MAX - 1) {
-            if (pauli_str.empty() == false) {
-                std::cerr << "Warning: PauliOperator::PauliOperator(std::string, CPPCTYPE) : detected pauli_str without indexs. Maybe mistyped?" << std::endl;
-                std::cerr << "Original Pauli string: " << strings << std::endl;
-            }
-            break;
-        }
+        if (pauli_str.length() == 0) break;
         if(pauli_str=="I" || pauli_str=="i") pauli_type = 0;
         else if(pauli_str=="X" || pauli_str=="x") pauli_type = 1;
         else if(pauli_str=="Y" || pauli_str=="y") pauli_type = 2;
