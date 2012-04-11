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
# settings dialog
from settings import customLauncherSettings
# output dialog for shell command
from ui_shelloutput import Ui_shellOutput
# icons
import resources
# launch thread
import subprocess as sb
# split the command args when no shell
# see 17.1.1.2 in http://docs.python.org/library/subprocess.html
import shlex 

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
			self.actions.append( actionItem(i,self.iface,self.settings,self.toolBar) )
			
class actionItem(QAction):
	def __init__(self,actionIndex,iface,settings,toolBar):
		self.shellOutput = shellOutput()
		# load action
		self.icon      =      settings.value( "icon_%u"    % actionIndex , "").toString()
		self.action    =      settings.value( "action_%u"  % actionIndex , "").toString()
		self.tooltip   =      settings.value( "tooltip_%u" % actionIndex , "").toString()
		self.shellMode = bool(settings.value( "shell_%u"   % actionIndex , False).toInt()[0])
		# create action
		QAction.__init__(self , QIcon(self.icon) , self.tooltip , iface.mainWindow())
		QObject.connect( self , SIGNAL("triggered()"), self.run )
		toolBar.addAction(self)
			
	def run(self):
		if self.shellMode is True:
			output = sb.Popen( "%s" % self.action , shell=True , stdout = sb.PIPE, stderr= sb.PIPE).communicate()
			self.shellOutput.textBrowser.setText(''.join(output))
			self.shellOutput.show()
		else:
			action = shlex.split(str("%s" % self.action))
			sb.call(action)
			
class shellOutput(QDialog, Ui_shellOutput):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
