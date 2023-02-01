22c22
< from dwave.cloud.exceptions import ConfigFileError, SolverNotFoundError
---
> from dwave.cloud.exceptions import ConfigFileError
24d23
< from dwave_networkx.generators.pegasus import pegasus_graph
36c35
<         except (ValueError, ConfigFileError, SolverNotFoundError):
---
>         except (ValueError, ConfigFileError):
138,147c137,138
<             with Client.from_config() as client:
<                 solvers = client.get_solvers(qpu=True)
<             if not solvers:
<                 raise unittest.SkipTest("no qpu found")
<             for solver in solvers:
<                 if solver.num_active_qubits < solver.num_qubits:
<                     cls.qpu = DWaveSampler(solver=solver.id)
<                     return
<             raise unittest.SkipTest("no qpu with less than 100% yield found")
<         except (ValueError, ConfigFileError, SolverNotFoundError):
---
>             cls.qpu = DWaveSampler(solver=dict(num_active_qubits__lt=2048))
>         except (ValueError, ConfigFileError):
157c148
<         h = [0 for _ in range(self.qpu.solver.num_qubits)]
---
>         h = [0 for _ in range(2048)]
163c154
<         self.assertLessEqual(len(sampleset.variables), self.qpu.solver.num_qubits)  # sanity check
---
>         assert len(sampleset.variables) < 2048  # sanity check
