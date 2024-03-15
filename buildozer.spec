[app]

title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,toml
source.include_patterns = myapp/**/*
source.exclude_patterns = setup.py, pyproject.toml
requirements = python3,kivy
orientation = portrait
version = 0.0.1

#
# Android specific
#
fullscreen = 0
android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18), android.permission.READ_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
p4a.branch = master
p4a.setup_py = False
# android.no-byte-compile-python = False

[buildozer]

log_level = 2
warn_on_root = 1

