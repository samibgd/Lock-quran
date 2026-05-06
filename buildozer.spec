[app]
title = Premium App Locker
package.name = premiumlocker
package.domain = com.samibgd
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# المكتبات المطلوبة والمدعومة
requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 1

# الإعدادات الرسمية المتوافقة لضمان نجاح الـ toolchain
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a

# تفعيل الصلاحية المطلوبة للظهور في الأعلى وقبول الرخص
android.permissions = SYSTEM_ALERT_WINDOW
android.accept_sdk_license = True

# إعدادات المترجم لـ جيت هاب
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

