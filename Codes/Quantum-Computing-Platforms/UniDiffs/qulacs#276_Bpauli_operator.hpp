--- qulacs/qulacs#276_B/after/pauli_operator.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qulacs/qulacs#276_B/before/pauli_operator.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -82,11 +82,6 @@
         return res;
     }
 
-    UINT get_qubit_count() const{
-        std::vector<UINT> index_list = get_index_list();
-        if (index_list.size() == 0) return 0;
-        return *std::max_element(index_list.begin(), index_list.end()) + 1;
-    }
     /**
      * \~japanese-en
      * 自身が保持するパウリ演算子を返す。
