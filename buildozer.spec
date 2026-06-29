[app]

title = Calculadora

package.name = calculadora
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy==2.3.0,pillow

orientation = portrait

fullscreen = 0

presplash.filename = %(source.dir)s/calcu.png
icon.filename = %(source.dir)s/calcul.png


# -------------------------
# Android
# -------------------------

android.api = 33
android.minapi = 21

android.ndk = 25b

android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

android.debug_artifact = apk


# -------------------------
# Buildozer
# -------------------------

[buildozer]

log_level = 2

warn_on_root = 1
