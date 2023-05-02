18c18
< from dwave.cloud.exceptions import ConfigFileError, SolverNotFoundError
---
> from dwave.cloud.exceptions import ConfigFileError
30c30
<         except (ValueError, ConfigFileError, SolverNotFoundError):
---
>         except (ValueError, ConfigFileError):
