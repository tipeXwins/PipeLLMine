--- xacc/xacc#164/after/PulseScheduler.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#164/before/PulseScheduler.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -4,39 +4,6 @@
 
 #include "xacc.hpp"
 
-namespace {
-  void processComposite(std::shared_ptr<xacc::CompositeInstruction> composite, size_t compositeStartTime, std::map<std::string, std::size_t>& io_channel2times) {
-    for (auto& inst: composite->getInstructions()) {
-      if (inst->isEnabled() && !inst->isComposite()) {
-        auto pulse = std::dynamic_pointer_cast<xacc::quantum::Pulse>(inst);
-        if (!pulse) {
-            xacc::error("Invalid instruction in pulse program.");
-        }
-        if (io_channel2times.find(pulse->channel()) == io_channel2times.end()) {
-          io_channel2times.insert({pulse->channel(), compositeStartTime});
-        }
-        auto& currentTimeOnChannel = io_channel2times[pulse->channel()];
-        auto pulseExpectedStart = pulse->start() + compositeStartTime;
-        if (pulseExpectedStart >= currentTimeOnChannel) {
-          pulse->setStart(pulseExpectedStart);
-        } else {
-          pulse->setStart(currentTimeOnChannel);
-        }
-        currentTimeOnChannel = pulse->start() + pulse->duration();
-      } else if (inst->isEnabled() && inst->isComposite()) {
-        size_t nextCompositeStartTime = 0;
-        for (const auto& kv : io_channel2times) {
-          nextCompositeStartTime = kv.second > nextCompositeStartTime ? kv.second  : nextCompositeStartTime;
-        }
-        auto compositeInstPtr = std::dynamic_pointer_cast<xacc::CompositeInstruction>(inst);
-        if (!compositeInstPtr) {
-            xacc::error("Invalid instruction in pulse program.");
-        }
-        processComposite(compositeInstPtr, nextCompositeStartTime, io_channel2times);
-      }
-    } 
-  }
-}
 namespace xacc {
 namespace quantum {
 
@@ -44,8 +11,30 @@
 
   // Remember that sub-composites have timings relative to each other internally
   std::map<std::string, std::size_t> channel2times;
-  // Run the recursive scheduler, starting at this root composite at time 0:
-  processComposite(program, 0, channel2times);
+   InstructionIterator it(program);
+   while (it.hasNext()) {
+     auto nextInst = it.next();
+     if (nextInst->isEnabled() && !nextInst->isComposite()) {
+         auto pulse = std::dynamic_pointer_cast<Pulse>(nextInst);
+         if (!pulse) {
+             xacc::error("Invalid instruction in pulse program.");
+         }
+         if (!channel2times.count(pulse->channel())) {
+             channel2times.insert({pulse->channel(), 0});
+         }
+     }
+   }
+     InstructionIterator it2(program);
+   while (it2.hasNext()) {
+     auto nextInst = it2.next();
+     if (nextInst->isEnabled() && !nextInst->isComposite()) {
+         auto pulse = std::dynamic_pointer_cast<Pulse>(nextInst);
+         auto duration = pulse->duration();
+         auto currentTimeOnChannel = channel2times[pulse->channel()];
+         pulse->setStart(currentTimeOnChannel);
+         channel2times[pulse->channel()] += duration;
+     } 
+   }
 }
 
 }
