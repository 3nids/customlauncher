"""
Denis Rouzaud
denis.rouzaud@gmail.com
* * * * * * * * * * * *
Custom Launcher
QGIS plugin
"""

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from settings import customLauncherSettings
import resources
import subprocess

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class customLauncher():

	def __init__(self, iface):
		self.iface = iface
		self.settingsDialog = customLauncherSettings()
		QObject.connect( self.settingsDialog , SIGNAL("accepted()") , self.loadActions )
		self.settings = QSettings("CustomLauncher","CustomLauncher")
		self.actions = []
	
	def initGui(self):
		# Custom toolbar
		self.toolBar = self.iface.addToolBar("Custom Launcher")
		self.toolBar.setObjectName("Custom Launcher")
		# Settings
		self.settingsAction = QAction("Settings", self.iface.mainWindow())
		QObject.connect(self.settingsAction, SIGNAL("triggered()"), self.settingsDialog.exec_)
		self.iface.addPluginToMenu("&Custom Launcher", self.settingsAction)
		# help
		self.helpAction = QAction(QIcon(":/plugins/linkit/icons/help.png"), "Help", self.iface.mainWindow())
		QObject.connect(self.helpAction, SIGNAL("triggered()"), lambda: QDesktopServices.openUrl(QUrl("https://github.com/3nids/customlauncher/wiki")))
		self.iface.addPluginToMenu("&Custom Launcher", self.helpAction)
		# launch actions
		self.loadActions()
	
	def unload(self):
		self.unloadActions()
		self.iface.removePluginMenu("&Custom Launcher",self.settingsAction)
		self.iface.removePluginMenu("&Custom Launcher",self.helpAction)

	def unloadActions(self):
		self.toolBar.clear()
		self.actions = []

	def loadActions(self):
		self.unloadActions()
		numActions = self.settings.value( "number_of_actions" , 0 ).toInt()[0]
		for i in range(numActions):
			ico = self.settings.value( "icon_%u"    % i , "").toString()
			act = self.settings.value( "action_%u"  % i , "").toString()
			too = self.settings.value( "tooltip_%u" % i , "").toString()
			
			print act

			action = QAction(QIcon(ico), too , self.iface.mainWindow())
			QObject.connect( action, SIGNAL("triggered()"), lambda: subprocess.call( "%s" % act ) )
			self.toolBar.addAction(action)
			self.actions.append(action)
			
