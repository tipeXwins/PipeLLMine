--- amazon-braket-sdk-python/amazon-braket-sdk-python#187/after/aws_device.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#187/before/aws_device.py	2022-01-10 16:02:54.000000000 +0000
@@ -59,7 +59,6 @@
     DEFAULT_SHOTS_SIMULATOR = 0
     DEFAULT_MAX_PARALLEL = 10
 
-    _GET_DEVICES_ORDER_BY_KEYS = frozenset({"arn", "name", "type", "provider_name", "status"})
     def __init__(self, arn: str, aws_session: Optional[AwsSession] = None):
         """
         Args:
@@ -345,7 +344,7 @@
                 )
                 return AwsSession(boto_session=boto_session, config=config)
         else:
-            boto_session = boto3.Session(region_name=regions[0]) if regions else None
+            boto_session = boto3.Session(region_name=regions[0])
             return AwsSession(boto_session=boto_session, config=config)
 
     def __repr__(self):
@@ -389,39 +388,24 @@
         Returns:
             List[AwsDevice]: list of AWS devices
         """
-        if order_by not in AwsDevice._GET_DEVICES_ORDER_BY_KEYS:
-            raise ValueError(
-                f"order_by '{order_by}' must be in {AwsDevice._GET_DEVICES_ORDER_BY_KEYS}"
-            )
-        aws_session = aws_session if aws_session else AwsSession()
-        types = set(types) if types else {AwsDeviceType.QPU, AwsDeviceType.SIMULATOR}
-        device_map = {}
-        device_regions_set = AwsDevice._get_devices_regions_set(arns, provider_names)
+        order_by_list = ["arn", "name", "type", "provider_name", "status"]
+        if order_by not in order_by_list:
+            raise ValueError(f"order_by '{order_by}' must be in {order_by_list}")
+        device_regions_set = AwsDevice._get_devices_regions_set(arns, provider_names, types)
+        results = []
         for region in device_regions_set:
-            session_for_region = AwsDevice._copy_aws_session(aws_session, [region])
-            region_device_types = sorted(
-                types
-                if region == aws_session.boto_session.region_name
-                else types - {AwsDeviceType.SIMULATOR}
-            )
-            region_device_arns = [
-                result["deviceArn"]
-                for result in session_for_region.search_devices(
+            aws_session = AwsDevice._copy_aws_session(aws_session, [region])
+            results.extend(
+                aws_session.search_devices(
                     arns=arns,
                     names=names,
-                    types=region_device_types,
+                    types=types,
                     statuses=statuses,
                     provider_names=provider_names,
                 )
-            ]
-            device_map.update(
-                {
-                    arn: AwsDevice(arn, session_for_region)
-                    for arn in region_device_arns
-                    if arn not in device_map
-                }
             )
-        devices = list(device_map.values())
+        arns = set([result["deviceArn"] for result in results])
+        devices = [AwsDevice(arn, aws_session) for arn in arns]
         devices.sort(key=lambda x: getattr(x, order_by))
         return devices
 
@@ -429,6 +413,7 @@
     def _get_devices_regions_set(
         arns: Optional[List[str]],
         provider_names: Optional[List[str]],
+        types: Optional[List[AwsDeviceType]],
     ) -> Set[str]:
         """Get the set of regions to call `SearchDevices` API given filters"""
         device_regions_set = set(
@@ -445,4 +430,8 @@
         if arns:
             arns_region_set = set([AwsDevice.DEVICE_REGIONS[arn.split("/")[-2]][0] for arn in arns])
             device_regions_set = device_regions_set.intersection(arns_region_set)
+        if types and types == [AwsDeviceType.SIMULATOR]:
+            device_regions_set = device_regions_set.intersection(
+                [AwsDevice.DEVICE_REGIONS["amazon"][0]]
+            )
         return device_regions_set
