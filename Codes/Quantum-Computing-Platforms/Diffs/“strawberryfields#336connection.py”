18a19
> import json
156c157
<             self._url(path), headers=self._headers, json={"circuit": circuit},
---
>             self._url(path), headers=self._headers, data=json.dumps({"circuit": circuit}),
246c247
<             self._url(path), headers=self._headers, json={"status": JobStatus.CANCELLED.value},
---
>             self._url(path), headers=self._headers, data={"status": JobStatus.CANCELLED.value},
