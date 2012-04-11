"""
Denis Rouzaud
denis.rouzaud@gmail.com
* * * * * * * * * * * *
Custom Launcher
QGIS plugin
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_settings import Ui_Settings
from ui_action   import Ui_Action

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


# create the dialog to connect layers
class customLauncherSettings(QDialog, Ui_Settings):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		QObject.connect(self , SIGNAL( "accepted()" ) , self.applySettings)
		self.settings = QSettings("CustomLauncher","CustomLauncher")
		self.actions  = []

		numActions = self.settings.value( "number_of_actions" , 0 ).toInt()[0]
		for i in range(numActions):
			action = actionItem(i)
			action.iconEdit.setText(    self.settings.value( "icon_%u"    % i , ""   ).toString() )
			action.actionEdit.setText(  self.settings.value( "action_%u"  % i , ""   ).toString() )
			action.shellBox.setChecked( self.settings.value( "shell_%u"   % i , False).toInt()[0] )
			action.tooltipEdit.setText( self.settings.value( "tooltip_%u" % i , ""   ).toString() )
			QObject.connect(action,SIGNAL("actionDeleted(int)"),self.deleteAction)
			self.actionsLayout.addWidget(action)
			self.actions.append(action)

	def applySettings(self):
		self.settings.setValue( "number_of_actions" , len(self.actions) )
		for i,action in enumerate(self.actions):
			self.settings.setValue( "icon_%u"    % i ,     action.iconEdit.text()       )
			self.settings.setValue( "action_%u"  % i ,     action.actionEdit.text()     )
			self.settings.setValue( "shell_%u"   % i , int(action.shellBox.isChecked()) )
			self.settings.setValue( "tooltip_%u" % i ,     action.tooltipEdit.text()    )

	def deleteAction(self,actionIndex):
		self.actions.pop(actionIndex)
		for actionIndex,action in enumerate(self.actions):
			action.actionIndex = actionIndex

	@pyqtSignature("on_addActionButton_clicked()")
	def on_addActionButton_clicked(self):
		actionIndex = len(self.actions)
		self.actions.append( actionItem(actionIndex) )
		QObject.connect(self.actions[actionIndex],SIGNAL("actionDeleted(int)"),self.deleteAction)
		self.actionsLayout.addWidget(self.actions[actionIndex])

		
class actionItem(QFrame, Ui_Action):
	def __init__(self,actionIndex):
		QFrame.__init__(self)
		self.setupUi(self)
		self.actionIndex = actionIndex

	@pyqtSignature("on_iconButton_clicked()")
	def on_iconButton_clicked(self):
		icoFile = QFileDialog.getOpenFileName(self , "Choose icon file" , "" , "Images (*.png *.xpm *.jpg)" )
		if icoFile != "": self.iconEdit.setText(icoFile)
		
	@pyqtSignature("on_deleteButton_clicked()")
	def on_deleteButton_clicked(self):
		self.close()
		self.emit(SIGNAL("actionDeleted(int)"),self.actionIndex)
