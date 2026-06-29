[app]

# Nombre de la aplicación
title = Calculadora

# Nombre interno del paquete
package.name = calculadora

# Dominio del paquete
package.domain = org.test

# Carpeta donde está main.py
source.dir = .

# Archivos que se incluirán
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

# Versión de la aplicación
version = 0.1


# Dependencias Python/Kivy
requirements = python3,kivy,pillow


# Orientación
orientation = portrait

# Pantalla completa
fullscreen = 0


# Imagen de carga
presplash.filename = %(source.dir)s/calcu.png

# Icono
icon.filename = %(source.dir)s/calcul.png



# ==========================
# ANDROID
# ==========================

# Android

android.api = 33

android.minapi = 21

android.ndk = 25b

android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a

android.debug_artifact = apk


# ==========================
# PERMISOS (opcional)
# ==========================

# Si necesitas internet activa esta línea:
# android.permissions = android.permission.INTERNET



# ==========================
# PYTHON-FOR-ANDROID
# ==========================

# Bootstrap recomendado para Kivy
p4a.bootstrap = sdl2



# ==========================
# BUILDORIZER
# ==========================

[buildozer]

# Nivel de detalle del log
log_level = 2

# Aviso si se ejecuta como root
warn_on_root = 1
