[app]
title = Premium App Locker
package.name = premiumlocker
package.domain = com.samibgd
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# المتطلبات الأساسية والمستقرة
requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 1

# التوليفة الذهبية المتوافقة مع سيرفرات جيت هاب لمنع تعطل الـ Toolchain
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a

# تفعيل قبول رخص جوجل تلقائياً والصلاحيات
android.accept_sdk_license = True
android.permissions = SYSTEM_ALERT_WINDOW

[buildozer]
log_level = 2
warn_on_root = 1

