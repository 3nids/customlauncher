"""
Denis Rouzaud
denis.rouzaud@gmail.com
* * * * * * * * * * * *
Custom Launcher
QGIS module

"""
def name():
    return "Custom Launcher"
def description():
    return "A QGIS plugin to customize actions to launch your preferred apps or commands from QGIS."
def version():
    return "Version 1.1.0"
def icon():
    return "icons/customlauncher.png"
def qgisMinimumVersion():
    return "1.7"
def classFactory(iface):
    from customlauncher import customLauncher
    return customLauncher(iface)
