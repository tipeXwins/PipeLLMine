--- xacc/xacc#370/after/py_heterogeneous_map.hpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#370/before/py_heterogeneous_map.hpp	2022-01-10 16:02:54.000000000 +0000
@@ -55,7 +55,7 @@
 // associated map to fake like it is a HeterogeneousMap
 using PyHeterogeneousMapTypes =
     xacc::Variant<bool, int, double, std::string, std::vector<std::string>,
-                  std::vector<std::complex<double>>, std::vector<double>, std::vector<int>, std::complex<double>,
+                  std::vector<double>, std::vector<int>, std::complex<double>, std::vector<std::complex<double>>,
                   std::shared_ptr<CompositeInstruction>,
                   std::shared_ptr<Instruction>, std::shared_ptr<Accelerator>,
                   std::shared_ptr<Observable>, std::shared_ptr<Optimizer>, Eigen::MatrixXcd>;
