import PyInstaller.__main__
import platform

location = ""
system = platform.system()

if system == "Windows":
    location = (r'.\fll_presenter\Main.py')
    PyInstaller.__main__.run([
    location,
    '--onefile',
    '--windowed'
    ])

else:
    location = './fll_presenter/Main.py'
    PyInstaller.__main__.run([
    location,
    '--onefile'
    ])