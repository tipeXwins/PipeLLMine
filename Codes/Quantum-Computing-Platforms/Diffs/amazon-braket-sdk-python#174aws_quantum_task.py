230c230
<         if not use_cached_value or not self._metadata:
---
>         if not use_cached_value:
257,260d256
<     def _update_status_if_nonterminal(self):
<         metadata_absent = self._metadata is None
<         cached = self._status(True)
<         return cached if cached in self.TERMINAL_STATES else self._status(metadata_absent)
300c296
<             and self._update_status_if_nonterminal() not in self.NO_RESULT_TERMINAL_STATES
---
>             and self._status() not in self.NO_RESULT_TERMINAL_STATES  # timed out and no result
356,357c352,355
<             task_status = self._update_status_if_nonterminal()
<             current_metadata = self.metadata(True)
---
>             current_metadata = self.metadata(
>                 self._status(False) not in AwsQuantumTask.TERMINAL_STATES
>             )
>             task_status = self._status(False)
