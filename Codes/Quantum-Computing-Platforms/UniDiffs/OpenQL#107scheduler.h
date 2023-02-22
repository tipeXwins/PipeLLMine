--- OpenQL/OpenQL#107/after/scheduler.h	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#107/before/scheduler.h	2022-01-10 16:02:54.000000000 +0000
@@ -685,17 +685,17 @@
 
 
     // with rc and latency compensation
-    void ScheduleASAP( ListDigraph::NodeMap<size_t> & cycle, std::vector<ListDigraph::Node> & order,
+    void ScheduleALAP( ListDigraph::NodeMap<size_t> & cycle, std::vector<ListDigraph::Node> & order,
                        ql::arch::resource_manager_t & rm, ql::quantum_platform & platform, bool verbose=false )
     {
-        if(verbose) COUT("Performing RC ASAP Scheduling");
+        if(verbose) COUT("Performing RC ALAP Scheduling");
         TopologicalSort(order);
 
-        std::vector<ListDigraph::Node>::reverse_iterator currNode = order.rbegin();
-        size_t currCycle=0;
-        cycle[*currNode]=currCycle; // source node
+        std::vector<ListDigraph::Node>::iterator currNode = order.begin();
+        size_t currCycle=MAX_CYCLE;
+        cycle[*currNode]=currCycle;
         ++currNode;
-        while(currNode != order.rend() )
+        while(currNode != order.end() )
         {
             DOUT("");
             auto & curr_ins = instruction[*currNode];
@@ -703,7 +703,7 @@
 
             std::string operation_name(id);
             std::string operation_type; // MW/FLUX/READOUT etc
-            std::string instruction_type; // single / two qubit
+            std::string instruction_type; // sing/two qubit
             if ( !platform.instruction_settings[id]["cc_light_instr"].is_null() )
             {
                 operation_name = platform.instruction_settings[id]["cc_light_instr"];
@@ -717,38 +717,35 @@
                 instruction_type = platform.instruction_settings[id]["cc_light_instr_type"];
             }
 
-            size_t operation_duration = std::ceil( static_cast<float>(curr_ins->duration) / cycle_time);
-            size_t op_start_cycle=0;
-            DOUT("Scheduling " << name[*currNode]);
-            for( ListDigraph::InArcIt arc(graph,*currNode); arc != INVALID; ++arc )
-            {
-                ListDigraph::Node srcNode  = graph.source(arc);
-                size_t srcCycle = cycle[srcNode];
-                if(op_start_cycle < (srcCycle + weight[arc]))
+            size_t operation_cycles = std::ceil( static_cast<float>(curr_ins->duration) / cycle_time);
+            for( ListDigraph::OutArcIt arc(graph,*currNode); arc != INVALID; ++arc )
+            {
+                ListDigraph::Node targetNode  = graph.target(arc);
+                size_t targetCycle = cycle[targetNode];
+                if( currCycle > (targetCycle - weight[arc]) )
                 {
-                    op_start_cycle = srcCycle + weight[arc];
+                    currCycle = targetCycle - weight[arc];
                 }
             }
 
-            while(op_start_cycle < MAX_CYCLE)
+            while(currCycle > 0)
             {
-                DOUT("Trying to schedule: " << name[*currNode] << "  in cycle: " << op_start_cycle);
-                DOUT("current operation_duration: " << operation_duration);
-                if( rm.available(op_start_cycle, curr_ins, operation_name, operation_type, instruction_type, operation_duration) )
+                DOUT("Trying to schedule: " << name[*currNode] << "  in cycle: " << currCycle);
+                if( rm.available(currCycle, curr_ins, operation_name, operation_type, instruction_type, operation_cycles) )
                 {
                     DOUT("Resources available, Scheduled.");
 
-                    rm.reserve(op_start_cycle, curr_ins, operation_name, operation_type, instruction_type, operation_duration);
-                    cycle[*currNode]=op_start_cycle;
+                    rm.reserve(currCycle, curr_ins, operation_name, operation_type, instruction_type, operation_cycles);
+                    cycle[*currNode]=currCycle;
                     break;
                 }
                 else
                 {
                     DOUT("Resources not available, trying again ...");
-                    ++op_start_cycle;
+                    --currCycle; // TODO --operation_cycles
                 }
             }
-            if(op_start_cycle >= MAX_CYCLE)
+            if(currCycle <= 0)
             {
                 EOUT("Error: could not find schedule");
                 throw ql::exception("[x] Error : could not find schedule !",false);
@@ -794,7 +791,7 @@
         //     DOUT( cycle[*it] << "     =     " << MAX_CYCLE-cycle[*it] << "        " << name[*it] );
         // }
 
-        if(verbose) COUT("Performing RC ASAP Scheduling [Done].");
+        if(verbose) COUT("Performing RC ALAP Scheduling [Done].");
     }
 
 
@@ -1052,13 +1049,13 @@
 
 
     // the following with rc and buffer-buffer delays
-    Bundles GetBundlesScheduleASAP( ql::arch::resource_manager_t & rm, ql::quantum_platform & platform, bool verbose=false )
+    Bundles GetBundlesScheduleALAP( ql::arch::resource_manager_t & rm, ql::quantum_platform & platform, bool verbose=false )
     {
-        if(verbose) COUT("RC Scheduling ASAP to get bundles ...");
+        if(verbose) COUT("RC Scheduling ALAP to get bundles ...");
         Bundles bundles;
         ListDigraph::NodeMap<size_t> cycle(graph);
         std::vector<ListDigraph::Node> order;
-        ScheduleASAP(cycle, order, rm, platform, verbose);
+        ScheduleALAP(cycle, order, rm, platform, verbose);
 
         typedef std::vector<ql::gate*> insInOneCycle;
         std::map<size_t,insInOneCycle> insInAllCycles;
@@ -1070,17 +1067,17 @@
                  instruction[*it]->type() != ql::gate_type_t::__dummy_gate__ 
                )
             {
-                insInAllCycles[ cycle[*it] ].push_back( instruction[*it] );
+                insInAllCycles[ MAX_CYCLE - cycle[*it] ].push_back( instruction[*it] );
             }
         }
 
         size_t TotalCycles = 0;
         if( ! order.empty() )
         {
-            TotalCycles =  cycle[ *( order.begin() ) ];
+            TotalCycles =  MAX_CYCLE - cycle[ *( order.rbegin() ) ];
         }
 
-        for(size_t currCycle = 0; currCycle<=TotalCycles; ++currCycle)
+        for(int currCycle = TotalCycles; currCycle>=0; --currCycle)
         {
             auto it = insInAllCycles.find(currCycle);
             if( it != insInAllCycles.end() )
@@ -1097,7 +1094,7 @@
                     size_t iduration = ins->duration;
                     bduration = std::max(bduration, iduration);
                 }
-                abundle.start_cycle = currCycle;
+                abundle.start_cycle = TotalCycles - currCycle;
                 abundle.duration_in_cycles = std::ceil(static_cast<float>(bduration)/cycle_time);
                 bundles.push_back(abundle);
             }
@@ -1141,7 +1138,7 @@
             operations_prev_bundle = operations_curr_bundle;
         }
 
-        if(verbose) COUT("RC Scheduling ASAP to get bundles [DONE]");
+        if(verbose) COUT("RC Scheduling ALAP to get bundles [DONE]");
         return bundles;
     }
 
