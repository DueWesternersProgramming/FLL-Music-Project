"""Module to run PyInstaller to build the project"""
import platform
import PyInstaller.__main__

LOCATION = ""
system = platform.system()

if system == "Windows":
    LOCATION = r'.\fll_presenter\main.py'
    PyInstaller.__main__.run([
    LOCATION,
    #'--onefile',
    '--windowed'
    ])

elif system == "Linux":
    LOCATION = './fll_presenter/main.py'
    PyInstaller.__main__.run([
    LOCATION
    #,'--onefile'
    ])
