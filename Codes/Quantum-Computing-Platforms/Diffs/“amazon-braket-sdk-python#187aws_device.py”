62d61
<     _GET_DEVICES_ORDER_BY_KEYS = frozenset({"arn", "name", "type", "provider_name", "status"})
348c347
<             boto_session = boto3.Session(region_name=regions[0]) if regions else None
---
>             boto_session = boto3.Session(region_name=regions[0])
392,399c391,395
<         if order_by not in AwsDevice._GET_DEVICES_ORDER_BY_KEYS:
<             raise ValueError(
<                 f"order_by '{order_by}' must be in {AwsDevice._GET_DEVICES_ORDER_BY_KEYS}"
<             )
<         aws_session = aws_session if aws_session else AwsSession()
<         types = set(types) if types else {AwsDeviceType.QPU, AwsDeviceType.SIMULATOR}
<         device_map = {}
<         device_regions_set = AwsDevice._get_devices_regions_set(arns, provider_names)
---
>         order_by_list = ["arn", "name", "type", "provider_name", "status"]
>         if order_by not in order_by_list:
>             raise ValueError(f"order_by '{order_by}' must be in {order_by_list}")
>         device_regions_set = AwsDevice._get_devices_regions_set(arns, provider_names, types)
>         results = []
401,409c397,399
<             session_for_region = AwsDevice._copy_aws_session(aws_session, [region])
<             region_device_types = sorted(
<                 types
<                 if region == aws_session.boto_session.region_name
<                 else types - {AwsDeviceType.SIMULATOR}
<             )
<             region_device_arns = [
<                 result["deviceArn"]
<                 for result in session_for_region.search_devices(
---
>             aws_session = AwsDevice._copy_aws_session(aws_session, [region])
>             results.extend(
>                 aws_session.search_devices(
412c402
<                     types=region_device_types,
---
>                     types=types,
416,422d405
<             ]
<             device_map.update(
<                 {
<                     arn: AwsDevice(arn, session_for_region)
<                     for arn in region_device_arns
<                     if arn not in device_map
<                 }
424c407,408
<         devices = list(device_map.values())
---
>         arns = set([result["deviceArn"] for result in results])
>         devices = [AwsDevice(arn, aws_session) for arn in arns]
431a416
>         types: Optional[List[AwsDeviceType]],
447a433,436
>         if types and types == [AwsDeviceType.SIMULATOR]:
>             device_regions_set = device_regions_set.intersection(
>                 [AwsDevice.DEVICE_REGIONS["amazon"][0]]
>             )
