7c7
< quil                : allInstr (NEWLINE+ allInstr)* EOF ;
---
> quil                : allInstr (NEWLINE+ allInstr)* NEWLINE* EOF ;
117c117
< number              : realN | imaginaryN | I | PI ;
---
> number              : realN | imaginaryN | I ;
