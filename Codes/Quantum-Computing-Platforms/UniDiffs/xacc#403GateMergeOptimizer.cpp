--- xacc/xacc#403/after/GateMergeOptimizer.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#403/before/GateMergeOptimizer.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -64,30 +64,11 @@
   io_composite->clear();
   io_composite->addInstructions(flatten);
 }
-std::vector<std::string>
-getBufferList(const std::shared_ptr<CompositeInstruction> &program) {
-  std::set<std::string> allBuffers;
-  InstructionIterator it(program);
-  while (it.hasNext()) {
-    auto nextInst = it.next();
-    for (const auto &bufferName : nextInst->getBufferNames()) {
-      allBuffers.emplace(bufferName);
-    }
-  }
-  std::vector<std::string> result(allBuffers.begin(), allBuffers.end());
-  return result;
 }
-} // namespace
 namespace xacc {
 namespace quantum {
 void MergeSingleQubitGatesOptimizer::apply(std::shared_ptr<CompositeInstruction> program, const std::shared_ptr<Accelerator> accelerator, const HeterogeneousMap &options)
 {
-    const auto buffer_names = getBufferList(program);
-    if (buffer_names.size() > 1) 
-    {
-        return;
-    }
-
     auto gateRegistry = xacc::getService<xacc::IRProvider>("quantum");
     flattenComposite(program);
     for (size_t instIdx = 0; instIdx < program->nInstructions(); ++instIdx)
@@ -139,7 +120,6 @@
                     for (auto& newInst: zyz->getInstructions())
                     {
                         newInst->setBits({bitIdx});
-                        newInst->setBufferNames({ buffer_names[0] });
                         program->addInstruction(newInst->clone());
                     }
                 }
@@ -149,7 +129,6 @@
                     for (auto& newInst: zyz->getInstructions())
                     {
                         newInst->setBits({bitIdx});
-                        newInst->setBufferNames({ buffer_names[0] });
                         program->insertInstruction(locationToInsert, newInst->clone());
                         locationToInsert++;
                     }
@@ -209,11 +188,6 @@
 
 void MergeTwoQubitBlockOptimizer::apply(std::shared_ptr<CompositeInstruction> program, const std::shared_ptr<Accelerator> accelerator, const HeterogeneousMap& options)
 {
-    const auto buffer_names = getBufferList(program);
-    if (buffer_names.size() > 1) 
-    {
-        return;
-    }
     auto gateRegistry = xacc::getService<xacc::IRProvider>("quantum");
     flattenComposite(program);
     // No need to optimize block with less than 6 gates
@@ -321,7 +295,6 @@
                     for (auto& newInst: kak->getInstructions())
                     {
                         newInst->setBits(remapBits(newInst->bits()));
-                        newInst->setBufferNames(std::vector<std::string>(newInst->bits().size(), buffer_names[0]));
                         program->addInstruction(newInst->clone());
                     }
                 }
@@ -331,7 +304,6 @@
                     for (auto& newInst: kak->getInstructions())
                     {
                         newInst->setBits(remapBits(newInst->bits()));
-                        newInst->setBufferNames(std::vector<std::string>(newInst->bits().size(), buffer_names[0]));
                         program->insertInstruction(locationToInsert, newInst->clone());
                         locationToInsert++;
                     }
