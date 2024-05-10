[app]
# (str) Title of your application
title = Fitness Tracker

# (str) Package name
package.name = fitnesstracker

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = 

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png,images/*.jpg,fonts/*.ttf

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd,opencv-python,tensorflow,firebase-admin,requests,Pillow

# (str) Presplash of the application
presplash.filename = %(source.dir)s/logo1.png

# (str) Icon of the application
icon.filename = %(source.dir)s/logo1.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (str) Android entry point
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
android.permissions = INTERNET, CAMERA

[buildozer]
# Buildozer settings
log_level = 2
warn_on_root = 1
# Log Level
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1
