[app]

# Title of your application
title = Fitness Tracker

# Package name
package.name = fitnesstracker

# Package domain (needed for android/ios packaging)
package.domain = org.test

# Source code directory where the main.py lives
source.dir = .

# Source files to include (let empty to include all the files)
source.include_exts =

# List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png,images/*.jpg,fonts/*.ttf

# Application versioning
version = 0.1

# Application requirements
requirements = python3,kivy,kivymd,opencv-python,tensorflow,firebase-admin,requests,Pillow

# Presplash of the application
presplash.filename = %(source.dir)s/logo1.png

# Icon of the application
icon.filename = %(source.dir)s/logo1.png

# Supported orientations
orientation = portrait

# Android Permissions
android.permissions = INTERNET, CAMERA

# Android Architectures
android.archs = arm64-v8a, armeabi-v7a

# Allow Backup
android.allow_backup = True

# Log Level
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1
