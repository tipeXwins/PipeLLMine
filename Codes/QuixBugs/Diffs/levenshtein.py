0a1
> 
6c7
<         return 1 + levenshtein(source[1:], target[1:])
---
>         return levenshtein(source[1:], target[1:])
15,32d15
< """
< Levenshtein Distance
< 
< 
< Calculates the Levenshtein distance between two strings.  The Levenshtein distance is defined as the minimum amount of single-character edits (either removing a character, adding a character, or changing a character) necessary to transform a source string into a target string.
< 
< Input:
<     source: The string you begin with.
<     target: The string to transform into.
< 
< Output:
<     The Levenshtein distance between the source and target.
< 
< Example:
<     electron can be transformed into neutron by removing the e, turning the l into n, and turning the c into u.
<     >>> levenshtein(electron, neutron)
<     3
< """
