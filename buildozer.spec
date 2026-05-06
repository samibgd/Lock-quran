[app]
title = Premium App Locker
package.name = premiumlocker
package.domain = com.samibgd
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius
android.permissions = SYSTEM_ALERT_WINDOW
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a

# الأسطر السحرية لحل مشكلة الرخص والـ Aidl نهائياً على سيرفر GitHub:
android.accept_sdk_license = True
android.skip_apk_rescale = True
android.api = 34
android.minapi = 21
android.ndk_api = 21
