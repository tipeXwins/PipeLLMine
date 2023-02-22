--- qsharp-runtime/qsharp-runtime#133/after/ToffoliSimulatorTests.cs	2022-01-10 16:02:54.000000000 +0000
+++ qsharp-runtime/qsharp-runtime#133/before/ToffoliSimulatorTests.cs	2022-01-10 16:02:54.000000000 +0000
@@ -222,9 +222,6 @@
         [Fact]
         public void ToffoliDumpState()
         {
-            var NL = System.Environment.NewLine;
-            var expectedHeader = "Offset  \tState Data" + NL +
-                                 "========\t==========" + NL;
             var sim = new ToffoliSimulator();
 
             var allocate = sim.Get<Intrinsic.Allocate>();
@@ -254,20 +251,32 @@
             var testPath = Path.GetTempFileName();
             output.WriteLine($"Dumping machine to {testPath}.");
             dumpMachine.Apply(testPath);
-            var expectedAutomatic = expectedHeader + "00000000\t1001001001001" + NL;
-            Assert.Equal(expectedAutomatic, File.ReadAllText(testPath));
+            var expected = @"Offset  \tState Data
+========\t==========
+00000000\t1001001001001
+"
+                .Replace("\\t", "\t");
+            Assert.Equal(expected, File.ReadAllText(testPath));
 
             sim.DumpFormat = ToffoliDumpFormat.Bits;
             testPath = Path.GetTempFileName();
             dumpMachine.Apply(testPath);
-            var expectedBits = expectedHeader + "00000000\t1001001001001" + NL;
-            Assert.Equal(expectedBits, File.ReadAllText(testPath));
+            expected = @"Offset  \tState Data
+========\t==========
+00000000\t1001001001001
+"
+                .Replace("\\t", "\t");
+            Assert.Equal(expected, File.ReadAllText(testPath));
 
             sim.DumpFormat = ToffoliDumpFormat.Hex;
             testPath = Path.GetTempFileName();
             dumpMachine.Apply(testPath);
-            var expectedHex = expectedHeader + "00000000\t49 12" + NL;
-            Assert.Equal(expectedHex, File.ReadAllText(testPath));
+            expected = @"Offset  \tState Data
+========\t==========
+00000000\t49 12
+"
+                .Replace("\\t", "\t");
+            Assert.Equal(expected, File.ReadAllText(testPath));
 
             // Reset and return our qubits for the next example.
             Prepare(qubits);
@@ -282,26 +291,35 @@
             sim.DumpFormat = ToffoliDumpFormat.Automatic;
             testPath = Path.GetTempFileName();
             dumpMachine.Apply(testPath);
-            var expectedAutomaticLarge =
-                    expectedHeader + "00000000\t49 92 24 49 92 24 49 92" + NL;
-            Assert.Equal(expectedAutomaticLarge, File.ReadAllText(testPath));
+            expected = @"Offset  \tState Data
+========\t==========
+00000000\t49 92 24 49 92 24 49 92
+"
+                .Replace("\\t", "\t");
+            Assert.Equal(expected, File.ReadAllText(testPath));
 
             sim.DumpFormat = ToffoliDumpFormat.Bits;
             testPath = Path.GetTempFileName();
             dumpMachine.Apply(testPath);
-            var expectedBitsLarge = expectedHeader +
-                                    "00000000\t1001001001001001" + NL +
-                                    "00000002\t0010010010010010" + NL +
-                                    "00000004\t0100100100100100" + NL +
-                                    "00000006\t1001001001001001" + NL;
-            Assert.Equal(expectedBitsLarge, File.ReadAllText(testPath));
+            expected = @"Offset  \tState Data
+========\t==========
+00000000\t1001001001001001
+00000002\t0010010010010010
+00000004\t0100100100100100
+00000006\t1001001001001001
+"
+                .Replace("\\t", "\t");
+            Assert.Equal(expected, File.ReadAllText(testPath));
 
             sim.DumpFormat = ToffoliDumpFormat.Hex;
             testPath = Path.GetTempFileName();
             dumpMachine.Apply(testPath);
-            var expectedHexLarge =
-                    expectedHeader + "00000000\t49 92 24 49 92 24 49 92" + NL;
-            Assert.Equal(expectedHexLarge, File.ReadAllText(testPath));
+            expected = @"Offset  \tState Data
+========\t==========
+00000000\t49 92 24 49 92 24 49 92
+"
+                .Replace("\\t", "\t");
+            Assert.Equal(expected, File.ReadAllText(testPath));
 
             // Reset and return our qubits for the next example.
             Prepare(qubits);
