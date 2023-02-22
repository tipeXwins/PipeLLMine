--- xacc/xacc#238/after/GateMergeOptimizer.cpp	2022-01-10 16:02:54.000000000 +0000
+++ xacc/xacc#238/before/GateMergeOptimizer.cpp	2022-01-10 16:02:54.000000000 +0000
@@ -109,12 +109,11 @@
                 }
                 else
                 {
-                    auto locationToInsert = sequence[0];
+                    const auto locationToInsert = sequence[0];
                     for (auto& newInst: zyz->getInstructions())
                     {
                         newInst->setBits({bitIdx});
                         program->insertInstruction(locationToInsert, newInst->clone());
-                        locationToInsert++;
                     }
                 }
                 
@@ -284,12 +283,11 @@
                 }
                 else
                 {
-                    auto locationToInsert = sequence[0];
+                    const auto locationToInsert = sequence[0];
                     for (auto& newInst: kak->getInstructions())
                     {
                         newInst->setBits(remapBits(newInst->bits()));
                         program->insertInstruction(locationToInsert, newInst->clone());
-                        locationToInsert++;
                     }
                 }
                 // Jump forward since we don't want to re-analyze this block.
