--- xacc/xacc#288/after/qaoa_maxcut.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#288/before/qaoa_maxcut.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -16,14 +16,11 @@
 
 int main(int argc, char **argv) {
   xacc::Initialize(argc, argv);
-  auto acc = xacc::getAccelerator("tnqvm",{
-              std::make_pair("tnqvm-visitor", "exatn:float"),
-              std::make_pair("exatn-buffer-size-gb", 6)
-             });
-  const size_t nbNodes = 24;
+  auto acc = xacc::getAccelerator("qpp");
+  const size_t nbNodes = 8;
   const int nbSteps = 1;
   auto buffer = xacc::qalloc(nbNodes);
-  auto optimizer = xacc::getOptimizer("nlopt",{{"nlopt-maxeval",1}});
+  auto optimizer = xacc::getOptimizer("nlopt");
   auto qaoa = xacc::getService<xacc::Algorithm>("QAOA");
   auto graph = xacc::getService<xacc::Graph>("boost-digraph")->gen_random_graph(nbNodes, 3.0 / nbNodes); 
   const bool initOk = qaoa->initialize({std::make_pair("accelerator", acc),
@@ -33,6 +30,4 @@
 			std::make_pair("parameter-scheme", "Standard")});
   qaoa->execute(buffer);
   std::cout << "Min Val: " << (*buffer)["opt-val"].as<double>() << "\n";
-  xacc::Finalize();
-  return 0;
 }
