--- amazon-braket-sdk-python/amazon-braket-sdk-python#188/after/aws_device.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#188/before/aws_device.py	2022-01-10 16:02:54.000000000 +0000
@@ -399,29 +399,29 @@
         device_map = {}
         device_regions_set = AwsDevice._get_devices_regions_set(arns, provider_names)
         for region in device_regions_set:
-            session_region = aws_session.boto_session.region_name
-            if region == session_region or types != {AwsDeviceType.SIMULATOR}:
-                session_for_region = AwsDevice._copy_aws_session(aws_session, [region])
-                region_device_types = sorted(
-                    types if region == session_region else types - {AwsDeviceType.SIMULATOR}
-                )
-                region_device_arns = [
-                    result["deviceArn"]
-                    for result in session_for_region.search_devices(
-                        arns=arns,
-                        names=names,
-                        types=region_device_types,
-                        statuses=statuses,
-                        provider_names=provider_names,
-                    )
-                ]
-                device_map.update(
-                    {
-                        arn: AwsDevice(arn, session_for_region)
-                        for arn in region_device_arns
-                        if arn not in device_map
-                    }
+            session_for_region = AwsDevice._copy_aws_session(aws_session, [region])
+            region_device_types = sorted(
+                types
+                if region == aws_session.boto_session.region_name
+                else types - {AwsDeviceType.SIMULATOR}
+            )
+            region_device_arns = [
+                result["deviceArn"]
+                for result in session_for_region.search_devices(
+                    arns=arns,
+                    names=names,
+                    types=region_device_types,
+                    statuses=statuses,
+                    provider_names=provider_names,
                 )
+            ]
+            device_map.update(
+                {
+                    arn: AwsDevice(arn, session_for_region)
+                    for arn in region_device_arns
+                    if arn not in device_map
+                }
+            )
         devices = list(device_map.values())
         devices.sort(key=lambda x: getattr(x, order_by))
         return devices
