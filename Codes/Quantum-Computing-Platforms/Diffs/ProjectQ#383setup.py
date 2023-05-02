373,375c373,376
<             major_version = int(platform.mac_ver()[0].split('.')[0])
<             minor_version = int(platform.mac_ver()[0].split('.')[1])
<             if major_version <= 10 and minor_version < 14:
---
>             _, minor_version, _ = [
>                 int(i) for i in platform.mac_ver()[0].split('.')
>             ]
>             if minor_version < 14:
