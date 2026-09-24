[app]
title = Mini Roblox Game
package.name = miniroblox
package.domain = org.roblox.clone
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 0.1
requirements = python3,kivy,ursina,pygame
orientation = landscape
fullscreen = 1
android.permissions = INTERNET
android.api = 31
android.min_api = 21
android.sdk = 20
android.ndk = 23b
android.archs = armeabi-v7a,arm64-v8a
allow_bsd = True

[buildozer]
log_level = 2
warn_on_root = 1
