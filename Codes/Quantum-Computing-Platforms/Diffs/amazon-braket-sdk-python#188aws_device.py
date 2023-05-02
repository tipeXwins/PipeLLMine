402,423c402,415
<             session_region = aws_session.boto_session.region_name
<             if region == session_region or types != {AwsDeviceType.SIMULATOR}:
<                 session_for_region = AwsDevice._copy_aws_session(aws_session, [region])
<                 region_device_types = sorted(
<                     types if region == session_region else types - {AwsDeviceType.SIMULATOR}
<                 )
<                 region_device_arns = [
<                     result["deviceArn"]
<                     for result in session_for_region.search_devices(
<                         arns=arns,
<                         names=names,
<                         types=region_device_types,
<                         statuses=statuses,
<                         provider_names=provider_names,
<                     )
<                 ]
<                 device_map.update(
<                     {
<                         arn: AwsDevice(arn, session_for_region)
<                         for arn in region_device_arns
<                         if arn not in device_map
<                     }
---
>             session_for_region = AwsDevice._copy_aws_session(aws_session, [region])
>             region_device_types = sorted(
>                 types
>                 if region == aws_session.boto_session.region_name
>                 else types - {AwsDeviceType.SIMULATOR}
>             )
>             region_device_arns = [
>                 result["deviceArn"]
>                 for result in session_for_region.search_devices(
>                     arns=arns,
>                     names=names,
>                     types=region_device_types,
>                     statuses=statuses,
>                     provider_names=provider_names,
424a417,424
>             ]
>             device_map.update(
>                 {
>                     arn: AwsDevice(arn, session_for_region)
>                     for arn in region_device_arns
>                     if arn not in device_map
>                 }
>             )
