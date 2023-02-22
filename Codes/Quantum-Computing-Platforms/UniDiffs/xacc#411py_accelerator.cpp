--- xacc/xacc#411/after/py_accelerator.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#411/before/py_accelerator.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -64,10 +64,6 @@
                   py::object functor = _circ.attr("out");
                   auto composite = mapper(functor, "quilc");
                   programs.push_back(composite);
-                } else {
-                  std::shared_ptr<CompositeInstruction> composite =
-                      _circ.cast<std::shared_ptr<CompositeInstruction>>();
-                  programs.push_back(composite);
                 }
               }
 
