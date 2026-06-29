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


# Cambia esta línea:
requirements = python3,kivy,kivymd,pillow


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

# ==========================
# ANDROID
# ==========================

# (int) Versión de la API de Android objetivo
android.api = 33

# (int) Versión mínima del SDK de Android
android.minapi = 21

# (int) Versión del NDK de Android
android.ndk = 25b

# (bool) Indicar si aceptas la licencia del SDK
android.accept_sdk_license = True

# (list) Arquitecturas soportadas
android.archs = arm64-v8a,armeabi-v7a

# (str) Tipo de artefacto de debug
android.debug_artifact = apk

# (bool) CRÍTICO: Necesario para que KivyMD funcione correctamente
android.enable_androidx = True

# (list) Permisos necesarios (descomenta si necesitas Internet)
# android.permissions = android.permission.INTERNET

# (str) Opcional: Nombre del paquete de Java
# android.package = org.test.calculadora

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
