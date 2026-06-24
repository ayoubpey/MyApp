[app]
title = MyApp
package.name = myapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

android.api = 34
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1