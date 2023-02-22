--- xacc/xacc#154/after/AssignmentErrorKernelDecorator.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#154/before/AssignmentErrorKernelDecorator.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -38,10 +38,7 @@
   }
   if (params.keyExists<std::vector<int>>("layout")){
     auto tmp = params.get<std::vector<int>>("layout");
-    for (auto& a : tmp){
-      layout.push_back(a);
-      std::cout<<a <<" ";
-    }
+    for (auto& a : tmp) layout.push_back(a);
     std::cout<<"layout recieved"<<std::endl;
     
   }
