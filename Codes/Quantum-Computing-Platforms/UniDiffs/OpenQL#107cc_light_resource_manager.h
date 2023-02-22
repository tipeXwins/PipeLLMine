--- OpenQL/OpenQL#107/after/cc_light_resource_manager.h	2022-01-10 16:02:54.000000000 +0000
+++ OpenQL/OpenQL#107/before/cc_light_resource_manager.h	2022-01-10 16:02:54.000000000 +0000
@@ -30,35 +30,35 @@
     {
         DOUT("constructing resource : " << n);
     }
-    virtual bool available(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)=0;
-    virtual void reserve(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)=0;
+    virtual bool available(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)=0;
+    virtual void reserve(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)=0;
     virtual ~resource_t() {}
 };
 
 class qubit_resource_t : public resource_t
 {
 public:
-    std::vector<size_t> state; // is busy till cycle
+    std::vector<size_t> state; // is busy till cycle number contained in state
     qubit_resource_t(ql::quantum_platform & platform) : resource_t("qubits")
     {
         count = platform.resources[name]["count"];
         state.resize(count);
         for(size_t i=0; i<count; i++)
         {
-            state[i] = 0;
+            state[i] = MAX_CYCLE;
         }
     }
 
-    bool available(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    bool available(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         for( auto q : ins->operands )
         {
-            DOUT(" available? curr op_start_cycle: " << op_start_cycle << "  qubit: " << q 
+            DOUT(" available? curr cycle: " << cycle << "  qubit: " << q 
                 << " is busy till cycle : " << state[q]);
-            if( op_start_cycle < state[q] )
+            if( cycle >= state[q] )
             {
                 DOUT("    qubit resource busy ...");
                 return false;
@@ -68,13 +68,13 @@
         return true;
     }
 
-    void reserve(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    void reserve(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         for( auto q : ins->operands )
         {
-            state[q]  = op_start_cycle + operation_duration;
-            DOUT("reserved. curr op_start_cycle: " << op_start_cycle << " qubit: " << q 
+            state[q] = cycle;
+            DOUT("reserved. curr cycle: " << cycle << " qubit: " << q 
                 << " reserved till cycle: " << state[q]);
         }
     }
@@ -85,7 +85,7 @@
 class qwg_resource_t : public resource_t
 {
 public:
-    std::vector<size_t> state; // is busy till cycle
+    std::vector<size_t> state; // is busy till cycle number contained in state
     std::vector<std::string> operations;
     std::map<size_t,size_t> qubit2qwg;
 
@@ -97,7 +97,7 @@
 
         for(size_t i=0; i<count; i++)
         {
-            state[i] = 0;
+            state[i] = MAX_CYCLE;
             operations[i] = "";
         }
         auto & constraints = platform.resources[name]["connection_map"];
@@ -111,18 +111,18 @@
         }
     }
 
-    bool available(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    bool available(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         bool is_mw = (operation_type == "mw");
         if( is_mw )
         {
             for( auto q : ins->operands )
             {
-                DOUT(" available? curr op_start_cycle: " << op_start_cycle << "  qwg: " << qubit2qwg[q] 
-                       << " is busy till op_start_cycle : " << state[ qubit2qwg[q] ] 
+                DOUT(" available? curr cycle: " << cycle << "  qwg: " << qubit2qwg[q] 
+                       << " is busy till cycle : " << state[ qubit2qwg[q] ] 
                        << " for operation: " << operations[ qubit2qwg[q] ]);
-                if( op_start_cycle < state[ qubit2qwg[q] ] )
+                if( cycle >= state[ qubit2qwg[q] ] )
                 {
                     if( operations[ qubit2qwg[q] ] != operation_name )
                     {
@@ -136,18 +136,17 @@
         return true;
     }
 
-    void reserve(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    void reserve(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         bool is_mw = (operation_type == "mw");
         if( is_mw )
         {
             for( auto q : ins->operands )
             {
-                if( state[ qubit2qwg[q] ] < op_start_cycle + operation_duration)
-                    state[ qubit2qwg[q] ]  = op_start_cycle + operation_duration;
+                state[ qubit2qwg[q] ]  = cycle - (operation_cycles - 1);
                 operations[ qubit2qwg[q] ] = operation_name;
-                DOUT("reserved. curr op_start_cycle: " << op_start_cycle << " qwg: " << qubit2qwg[q] 
+                DOUT("reserved. curr cycle: " << cycle << " qwg: " << qubit2qwg[q] 
                     << " reserved till cycle: " << state[ qubit2qwg[q] ] 
                     << " for operation: " << operations[ qubit2qwg[q] ] );
             }
@@ -160,7 +159,7 @@
 {
 public:
     std::vector<size_t> start_cycle; // last measurement start cycle
-    std::vector<size_t> state; // is busy till cycle
+    std::vector<size_t> state; // is busy till cycle number contained in state
     std::map<size_t,size_t> qubit2meas;
 
     meas_resource_t(ql::quantum_platform & platform) : resource_t("meas_units")
@@ -171,8 +170,8 @@
 
         for(size_t i=0; i<count; i++)
         {
-            start_cycle[i] = 0;
-            state[i] = 0;
+            start_cycle[i] = MAX_CYCLE;            
+            state[i] = MAX_CYCLE;
         }
         auto & constraints = platform.resources[name]["connection_map"];
         for (json::iterator it = constraints.begin(); it != constraints.end(); ++it)
@@ -185,21 +184,21 @@
         }
     }
 
-    bool available(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    bool available(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         bool is_measure = (operation_type == "readout");
         if( is_measure )
         {
             for(auto q : ins->operands)
             {
-                DOUT(" available? curr op_start_cycle: " << op_start_cycle << "  meas: " << qubit2meas[q] 
+                DOUT(" available? curr cycle: " << cycle << "  meas: " << qubit2meas[q] 
                           << " is busy till cycle : " << state[ qubit2meas[q] ] );
-                if( op_start_cycle != start_cycle[ qubit2meas[q] ] )
+                if( cycle != start_cycle[ qubit2meas[q] ] )
                 {
                     // If current measurement on same measurement-unit does not start in the
                     // same cycle, then it should wait for current measurement to finish
-                    if( op_start_cycle < state[ qubit2meas[q] ] )
+                    if( cycle >= state[ qubit2meas[q] ] )
                     {
                         DOUT("    measure resource busy ");
                         return false;
@@ -211,17 +210,17 @@
         return true;
     }
 
-    void reserve(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    void reserve(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         bool is_measure = (operation_type == "readout");
         if( is_measure )
         {
             for(auto q : ins->operands)
             {
-                start_cycle[ qubit2meas[q] ] = op_start_cycle;
-                state[ qubit2meas[q] ] = op_start_cycle + operation_duration;
-                DOUT("reserved. curr op_start_cycle: " << op_start_cycle << " meas: " << qubit2meas[q] 
+                start_cycle[ qubit2meas[q] ] = cycle;
+                state[ qubit2meas[q] ] = cycle - (operation_cycles - 1);
+                DOUT("reserved. curr cycle: " << cycle << " meas: " << qubit2meas[q] 
                     << " reserved till cycle: " << state[ qubit2meas[q] ] );
             }
         }
@@ -232,7 +231,7 @@
 class edge_resource_t : public resource_t
 {
 public:
-    std::vector<size_t> state; // is busy till cycle
+    std::vector<size_t> state; // is busy till cycle number contained in state
     typedef std::pair<size_t,size_t> qubits_pair_t;
     std::map< qubits_pair_t, size_t > qubits2edge;
     std::map<size_t, std::vector<size_t> > edge2edges;
@@ -244,7 +243,7 @@
 
         for(size_t i=0; i<count; i++)
         {
-            state[i] = 0;
+            state[i] = MAX_CYCLE;
         }
 
         for( auto & anedge : platform.topology["edges"] )
@@ -277,8 +276,8 @@
         }
     }
 
-    bool available(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    bool available(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         auto gname = ins->name;
         bool is_flux = (operation_type == "flux");
@@ -292,14 +291,14 @@
             {
                 auto edge_no = qubits2edge[aqpair];
 
-                DOUT(" available? curr op_start_cycle: " << op_start_cycle << ", edge: " << edge_no
+                DOUT(" available? curr cycle: " << cycle << ", edge: " << edge_no
                           << " is busy till cycle : " << state[edge_no] << " for operation: cz");
 
                 std::vector<size_t> edges2check(edge2edges[edge_no]);
                 edges2check.push_back(edge_no);
                 for(auto & e : edges2check)
                 {
-                    if( op_start_cycle < state[e] )
+                    if( cycle >= state[e] )
                     {
                         DOUT("    edge resource busy ");
                         return false;
@@ -316,8 +315,8 @@
         return true;
     }
 
-    void reserve(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    void reserve(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         auto gname = ins->name;
         bool is_flux = (operation_type == "flux");
@@ -327,13 +326,13 @@
             auto q1 = ins->operands[1];
             qubits_pair_t aqpair(q0, q1);
             auto edge_no = qubits2edge[aqpair];
-            state[edge_no] = op_start_cycle + operation_duration;
+            state[edge_no] = cycle - (operation_cycles - 1);
             for(auto & e : edge2edges[edge_no])
             {
-                state[e] = op_start_cycle + operation_duration;
+                state[e] = cycle - (operation_cycles - 1);
             }
 
-            DOUT("reserved. curr op_start_cycle: " << op_start_cycle << " edge: " << edge_no 
+            DOUT("reserved. curr cycle: " << cycle << " edge: " << edge_no 
                 << " reserved till cycle: " << state[ edge_no ] 
                 << " for operation: " << ins->name);
         }
@@ -384,24 +383,24 @@
 
         }
     }
-    bool available(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    bool available(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         // COUT("checking availablility of resources for: " << ins->qasm());
         for(auto rptr : resource_ptrs)
         {
-            if( rptr->available(op_start_cycle, ins, operation_name, operation_type, instruction_type, operation_duration) == false)
+            if( rptr->available(cycle, ins, operation_name, operation_type, instruction_type, operation_cycles) == false)
                 return false;
         }
         return true;
     }
-    void reserve(size_t op_start_cycle, ql::gate * ins, std::string & operation_name,
-        std::string & operation_type, std::string & instruction_type, size_t operation_duration)
+    void reserve(size_t cycle, ql::gate * ins, std::string & operation_name,
+        std::string & operation_type, std::string & instruction_type, size_t operation_cycles)
     {
         // COUT("reserving resources for: " << ins->qasm());
         for(auto rptr : resource_ptrs)
         {
-            rptr->reserve(op_start_cycle, ins, operation_name, operation_type, instruction_type, operation_duration);
+            rptr->reserve(cycle, ins, operation_name, operation_type, instruction_type, operation_cycles);
         }
     }
     ~resource_manager_t()
