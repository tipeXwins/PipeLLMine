--- xacc/xacc#423/after/py_observable.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#423/before/py_observable.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -41,9 +41,7 @@
       .def("fromString",
            (void (xacc::Observable::*)(const std::string)) &
                xacc::Observable::fromString,
-           "")
-      .def("postProcess", &xacc::Observable::postProcess,
-           "Post-process the execution results.");
+           "");
 
   m.def("getObservable",
         [](const std::string &type,
