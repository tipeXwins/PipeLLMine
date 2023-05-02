22,26d21
<     if ("" -ne "$Env:ASSEMBLY_CONSTANTS") {
<         $args = @("/property:DefineConstants=$Env:ASSEMBLY_CONSTANTS");
<     }  else {
<         $args = @();
<     }
31c26
<         @args `
---
>         /property:DefineConstants=$Env:ASSEMBLY_CONSTANTS `
