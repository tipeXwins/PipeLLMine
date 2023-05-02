21c21
< from dwave.cloud.exceptions import ConfigFileError, SolverNotFoundError
---
> from dwave.cloud.exceptions import ConfigFileError
34c34
<         except (ValueError, ConfigFileError, SolverNotFoundError):
---
>         except (ValueError, ConfigFileError):
