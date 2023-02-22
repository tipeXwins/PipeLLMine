--- QuantumLibraries/QuantumLibraries#216/after/EstimateFrequency.cs	2022-01-10 16:02:54.000000000 +0000
+++ QuantumLibraries/QuantumLibraries#216/before/EstimateFrequency.cs	2022-01-10 16:02:54.000000000 +0000
@@ -1,13 +1,11 @@
 using System;
 using System.Linq;
 using System.Runtime.InteropServices;
-using System.Runtime.ExceptionServices;
 
 using Microsoft.Quantum.Intrinsic;
 using Microsoft.Quantum.Simulation;
 using Microsoft.Quantum.Simulation.Core;
 using Microsoft.Quantum.Simulation.Simulators;
-using Microsoft.Quantum.Simulation.Simulators.Exceptions;
 using Microsoft.Quantum.Standard.Emulation;
 
 namespace Microsoft.Quantum.Characterization
@@ -36,7 +34,6 @@
 
             protected Allocate Allocate { get; set; }
             protected Release Release { get; set; }
-            protected ResetAll ResetAll { get; set; }
 
             public Native(IOperationFactory m) : base(m)
             {
@@ -49,7 +46,6 @@
 
                 this.Allocate = this.Factory.Get<Allocate>(typeof(Microsoft.Quantum.Intrinsic.Allocate));
                 this.Release = this.Factory.Get<Release>(typeof(Microsoft.Quantum.Intrinsic.Release));
-                this.ResetAll = this.Factory.Get<ResetAll>(typeof(Microsoft.Quantum.Intrinsic.ResetAll));
             }
 
             /// <summary>
@@ -70,45 +66,19 @@
                 if (paulis.Length != count) throw new InvalidOperationException("The number of paulis must match the number of qubits.");
 
                 var qubits = this.Allocate.Apply(count);
-                Exception? innerException = null;
-                double result = 0.0;
                 try
                 {
                     preparation.Apply(qubits);
                     var p = 1.0 - JointEnsembleProbability(Simulator.Id, (uint)count, paulis, qubits.GetIds());
+                    preparation.Adjoint.Apply(qubits);
 
                     var random = this.Simulator.Seed == 0 ? new System.Random() : new System.Random((int)this.Simulator.Seed);
                     var dist = new BinomialDistribution(samples, p, random);
-                    result = (double)dist.NextSample() / (double)samples;
-                    return result;
-                }
-                catch (ExecutionFailException ex)
-                {
-                    innerException = ex;
-                    return result;
+                    return (double)dist.NextSample() / (double)samples;
                 }
                 finally
                 {
-                    try
-                    {
-                        ResetAll.Apply(qubits);
-                        Release.Apply(qubits);
-                        if (innerException != null)
-                        {
-                            ExceptionDispatchInfo.Capture(innerException).Throw();
-                        }
-                    }
-                    catch (Exception ex)
-                    {
-                        if (innerException != null)
-                        {
-                            throw new AggregateException(ex, innerException);
-                        }
-                        else
-                        {
-                            ExceptionDispatchInfo.Capture(ex).Throw();
-                        }
-                    }
+                    Release.Apply(qubits);
                 }
             };
 
@@ -144,4 +114,4 @@
                     (measure.FullName == typeof(Primitive.Measure).FullName || measure.FullName == typeof(Intrinsic.Measure).FullName || measure.FullName == typeof(MeasureAllZ).FullName);
         }
     }
-}
+}
\ No newline at end of file
