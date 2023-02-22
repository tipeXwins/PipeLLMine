--- qiskit-aer/qiskit-aer#1089/after/creg.hpp	2022-01-10 16:02:54.000000000 +0000
+++ qiskit-aer/qiskit-aer#1089/before/creg.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -178,18 +178,13 @@
   } else {
     // We need to use big ints so we implement the bit-mask via the binary string
     // representation rather than using a big integer class
-    std::string mask_bin = Utils::hex2bin(mask, false);
-    size_t length = std::min(mask_bin.size(), creg_register_.size());
+    std::string mask_bin = Utils::hex2bin(mask); // has 0b prefix while creg_register_ doesn't
+    size_t length = std::min(mask_bin.size() - 2, creg_register_.size()); // -2 to remove 0b
     std::string masked_val = std::string(length, '0');
     for (size_t rev_pos = 0; rev_pos < length; rev_pos++) {
       masked_val[length - 1 - rev_pos] = (mask_bin[mask_bin.size() - 1 - rev_pos] 
                                           & creg_register_[creg_register_.size() - 1 - rev_pos]);
     }
-    size_t end_i = masked_val.find('1');
-    if (end_i == std::string::npos)
-        masked_val = "0";
-    else
-        masked_val.erase(0, end_i);
     masked_val = Utils::bin2hex(masked_val); // convert to hex string
     // Using string comparison to compare to target value
     compared = masked_val.compare(target_val);
