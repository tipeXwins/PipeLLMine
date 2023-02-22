--- amazon-braket-sdk-python/amazon-braket-sdk-python#207/after/aws_device.py	2022-01-10 16:02:54.000000000 +0000
+++ amazon-braket-sdk-python/amazon-braket-sdk-python#207/before/aws_device.py	2022-01-10 16:02:54.000000000 +0000
@@ -327,16 +327,7 @@
         See `braket.aws.aws_qpu.AwsDevice.DEVICE_REGIONS` for the
         AWS Regions the devices are located in.
         """
-        if device_arn in AwsDevice.QPU_REGIONS:
-            return AwsDevice._copy_aws_session(
-                aws_session, AwsDevice.QPU_REGIONS.get(device_arn), None
-            )
-        device_sessions = AwsDevice._get_arn_sessions(
-            [device_arn], None, {AwsDeviceType.QPU}, None, None, aws_session
-        )
-        if device_sessions:
-            return device_sessions[device_arn]
-        raise ValueError(f"QPU {device_arn} not found")
+        return AwsDevice._copy_aws_session(aws_session, AwsDevice.QPU_REGIONS.get(device_arn), None)
 
     @staticmethod
     def _copy_aws_session(
@@ -410,19 +401,11 @@
             raise ValueError(
                 f"order_by '{order_by}' must be in {AwsDevice._GET_DEVICES_ORDER_BY_KEYS}"
             )
+        aws_session = aws_session if aws_session else AwsSession()
         types = (
             frozenset(types) if types else frozenset({device_type for device_type in AwsDeviceType})
         )
-        arn_sessions = AwsDevice._get_arn_sessions(
-            arns, names, types, statuses, provider_names, aws_session
-        )
-        devices = [AwsDevice(arn, arn_sessions[arn]) for arn in arn_sessions]
-        devices.sort(key=lambda x: getattr(x, order_by))
-        return devices
-    @staticmethod
-    def _get_arn_sessions(arns, names, types, statuses, provider_names, aws_session):
-        aws_session = aws_session if aws_session else AwsSession()
-        sessions_for_arns = {}
+        device_map = {}
         session_region = aws_session.boto_session.region_name
         device_regions_set = AwsDevice._get_devices_regions_set(types, arns, session_region)
         for region in device_regions_set:
@@ -441,14 +424,16 @@
                     provider_names=provider_names,
                 )
             ]
-            sessions_for_arns.update(
+            device_map.update(
                 {
-                    arn: session_for_region
+                    arn: AwsDevice(arn, session_for_region)
                     for arn in region_device_arns
-                    if arn not in sessions_for_arns
+                    if arn not in device_map
                 }
             )
-        return sessions_for_arns
+        devices = list(device_map.values())
+        devices.sort(key=lambda x: getattr(x, order_by))
+        return devices
 
     @staticmethod
     def _get_devices_regions_set(
