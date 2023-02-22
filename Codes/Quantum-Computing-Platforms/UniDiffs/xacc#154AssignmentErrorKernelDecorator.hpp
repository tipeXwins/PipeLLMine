--- xacc/xacc#154/after/AssignmentErrorKernelDecorator.hpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#154/before/AssignmentErrorKernelDecorator.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -71,14 +71,14 @@
     auto provider = xacc::getIRProvider("quantum");
     for (int i = 0; i < pow_bits; i++) {
       auto circuit = provider->createComposite(permutations[i]);
-      int j = num_bits-1;
+      int j = 0;
       for (char c : permutations[i]) {
         if (c == '1') {
           // std::cout<<"1 found at position: "<<j<<std::endl;
           auto x = provider->createInstruction("X", j);
           circuit->addInstruction(x);
         }
-        j = (j-1)%num_bits;
+        j++;
       }
       for(int i = 0; i < num_bits; i++){
         circuit->addInstruction(provider->createInstruction("Measure", i));
