330,339c330
<         if device_arn in AwsDevice.QPU_REGIONS:
<             return AwsDevice._copy_aws_session(
<                 aws_session, AwsDevice.QPU_REGIONS.get(device_arn), None
<             )
<         device_sessions = AwsDevice._get_arn_sessions(
<             [device_arn], None, {AwsDeviceType.QPU}, None, None, aws_session
<         )
<         if device_sessions:
<             return device_sessions[device_arn]
<         raise ValueError(f"QPU {device_arn} not found")
---
>         return AwsDevice._copy_aws_session(aws_session, AwsDevice.QPU_REGIONS.get(device_arn), None)
412a404
>         aws_session = aws_session if aws_session else AwsSession()
416,425c408
<         arn_sessions = AwsDevice._get_arn_sessions(
<             arns, names, types, statuses, provider_names, aws_session
<         )
<         devices = [AwsDevice(arn, arn_sessions[arn]) for arn in arn_sessions]
<         devices.sort(key=lambda x: getattr(x, order_by))
<         return devices
<     @staticmethod
<     def _get_arn_sessions(arns, names, types, statuses, provider_names, aws_session):
<         aws_session = aws_session if aws_session else AwsSession()
<         sessions_for_arns = {}
---
>         device_map = {}
444c427
<             sessions_for_arns.update(
---
>             device_map.update(
446c429
<                     arn: session_for_region
---
>                     arn: AwsDevice(arn, session_for_region)
448c431
<                     if arn not in sessions_for_arns
---
>                     if arn not in device_map
451c434,436
<         return sessions_for_arns
---
>         devices = list(device_map.values())
>         devices.sort(key=lambda x: getattr(x, order_by))
>         return devices
