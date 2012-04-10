"""
Denis Rouzaud
denis.rouzaud@gmail.com
* * * * * * * * * * * *
Link It 
QGIS module

"""
def name():
    return "Action Customizer"
def description():
    return ""
def version():
    return "Version 1.0.0"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.7"
def classFactory(iface):
    from customizer import customizer
    return customizer(iface)
