1303c1303
<                         #spin_indices.append([2 * key[0], 2 * key[1], 2 * key[2] + 1, 2 * key[3] + 1])
---
>                         spin_indices.append([2 * key[0], 2 * key[1], 2 * key[2] + 1, 2 * key[3] + 1])
1306c1306
<                             #spin_indices.append([2 * key[0] + 1, 2 * key[1] + 1, 2 * key[2] + 1, 2 * key[3] + 1])
---
>                             spin_indices.append([2 * key[0] + 1, 2 * key[1] + 1, 2 * key[2] + 1, 2 * key[3] + 1])
1313,1314c1313,1314
<                         variables.append(2.0*Variable(name=key))  # abab
<                         #variables.append(Variable(name=key))  # baba
---
>                         variables.append(Variable(name=key))  # abab
>                         variables.append(Variable(name=key))  # baba
1316,1317c1316,1317
<                             variables.append(2.0*(Variable(name=key) - Variable(partner))) # aaaa
<                             #variables.append(Variable(name=key) - Variable(partner))  # bbbb
---
>                             variables.append(Variable(name=key) - Variable(partner))  # aaaa
>                             variables.append(Variable(name=key) - Variable(partner))  # bbbb
1319,1320c1319,1320
<                         variables.append(2.0*t)
<                         #variables.append(t)
---
>                         variables.append(t)
>                         variables.append(t)
1322,1323c1322,1323
<                             variables.append(2.0*(t - amplitudes[partner]))
<                             #variables.append(t - amplitudes[partner])
---
>                             variables.append(t - amplitudes[partner])
>                             variables.append(t - amplitudes[partner])
