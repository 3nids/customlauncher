"""
Denis Rouzaud
denis.rouzaud@gmail.com
* * * * * * * * * * * *
Link It 
QGIS module
"""

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from settings import customLauncherSettings
from connect_layer import connectLayer

import resources

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class customLauncher():

	def __init__(self, iface):
		self.iface = iface
		self.settings = customLauncherSettings()
	
	def initGui(self):
		self.connectLayerDlg = connectLayer(self.iface)
		QObject.connect(self.connectLayerDlg, SIGNAL("accepted()"), self.connect)
		# run connection when new layers are loaded
		QObject.connect(self.iface.mapCanvas() , SIGNAL("layersChanged ()") , self.connect )
		
		# Connect layers
		self.connectLayerAction = QAction(QIcon(":/plugins/linkit/icons/connect.png"), "Connect layer", self.iface.mainWindow())
		QObject.connect(self.connectLayerAction, SIGNAL("triggered()"), self.connectLayerDlg.exec_)
		self.iface.addPluginToMenu("&Link It", self.connectLayerAction)
		# help
		self.helpAction = QAction(QIcon(":/plugins/linkit/icons/help.png"), "Help", self.iface.mainWindow())
		QObject.connect(self.helpAction, SIGNAL("triggered()"), lambda: QDesktopServices.openUrl(QUrl("https://github.com/3nids/linkit/wiki")))
		self.iface.addPluginToMenu("&Link It", self.helpAction)
				
	def unload(self):
		self.iface.removePluginMenu("&Link It",self.connectLayerAction)
		self.iface.removePluginMenu("&Link It",self.helpAction)
		self.iface.removeToolBarIcon(self.connectLayerAction)
		
	def connect(self):
		self.layer = next( ( layer for layer in self.iface.legendInterface().layers() if layer.id() == self.settings.value("layer") ), False )
		if self.layer is not False:
			self.linker = linker(self.iface,self.layer)
			QObject.connect( self.layer , SIGNAL("browserCurrentItem(int)") , self.linker.itemChanged )
			QObject.connect( self.layer , SIGNAL("browserNoItem()")         , self.linker.clear )
			QObject.connect( self.layer , SIGNAL("layerDeleted()")          , self.linker.unload )
