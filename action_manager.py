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
from ui_actionmanager import Ui_ActionManager
from ui_action   import Ui_Action

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


# create the dialog to connect layers
class actionManager(QDialog, Ui_ActionManager):
	def __init__(self,iface):
		QDialog.__init__(self)
		self.setupUi(self)
		QObject.connect(self , SIGNAL( "accepted()" ) , self.saveActions)
		self.settings = QSettings("CustomLauncher","CustomLauncher")
		self.actions  = []
		self.iface = iface

	def showEvent(self,e):
		self.drawActions()
	
	def drawActions(self):
		for i in range(self.actionsLayout.count()): self.actionsLayout.itemAt(i).widget().close()
		self.actions  = []
		numActions = self.settings.value( "number_of_actions" , 0 ).toInt()[0]
		for i in range(numActions):
			action = actionItem(i,self.iface)
			action.iconEdit.setText(    self.settings.value( "icon_%u"    % i , ""   ).toString() )
			action.actionEdit.setText(  self.settings.value( "action_%u"  % i , ""   ).toString() )
			action.shellBox.setChecked( self.settings.value( "shell_%u"   % i , False).toInt()[0] )
			action.tooltipEdit.setText( self.settings.value( "tooltip_%u" % i , ""   ).toString() )
			self.connectAction(action)
			self.actionsLayout.addWidget(action)
			self.actions.append(action)

	def saveActions(self):
		self.settings.setValue( "number_of_actions" , len(self.actions) )
		for i,action in enumerate(self.actions):
			self.settings.setValue( "icon_%u"    % i ,     action.iconEdit.text()       )
			self.settings.setValue( "action_%u"  % i ,     action.actionEdit.text()     )
			self.settings.setValue( "shell_%u"   % i , int(action.shellBox.isChecked()) )
			self.settings.setValue( "tooltip_%u" % i ,     action.tooltipEdit.text()    )

	def connectAction(self,action):
		QObject.connect(action,SIGNAL("actionDeleted(int)"),self.deleteAction)
		QObject.connect(action,SIGNAL("actionMove(int,int)"),self.actionMove)

	def actionMove(self,actionIndex,way):
		# way: -1= up, +1=down
		if way == -1 and actionIndex <= 0                  : return
		if way ==  1 and actionIndex >= len(self.actions)-1: return
		action2move = self.actions[actionIndex]
		self.actions[actionIndex    ] = self.actions[actionIndex+way]
		self.actions[actionIndex+way] = action2move
		self.saveActions()
		self.drawActions()			

	def deleteAction(self,actionIndex):
		self.actions.pop(actionIndex)
		for actionIndex,action in enumerate(self.actions):
			action.actionIndex = actionIndex

	@pyqtSignature("on_addActionButton_clicked()")
	def on_addActionButton_clicked(self):
		actionIndex = len(self.actions)
		self.actions.append( actionItem(actionIndex,self.iface) )
		self.connectAction(self.actions[actionIndex])
		self.actionsLayout.addWidget(self.actions[actionIndex])


class actionItem(QFrame, Ui_Action):
	def __init__(self,actionIndex,iface):
		QFrame.__init__(self)
		self.setupUi(self)
		self.actionIndex = actionIndex
		self.iface = iface

	@pyqtSignature("on_iconButton_clicked()")
	def on_iconButton_clicked(self):
		icoFile = QFileDialog.getOpenFileName(self , "Choose icon file" , "" , "Images (*.png *.xpm *.jpg *.tig *.bmp)" )
		if icoFile != "": self.iconEdit.setText(icoFile)
		
	@pyqtSignature("on_deleteButton_clicked()")
	def on_deleteButton_clicked(self):
		reply = QMessageBox.question( self.iface.mainWindow() , "Custom Launcher", "Are you sure to delete this action?", QMessageBox.Yes, QMessageBox.No )			
		if reply == QMessageBox.No: return
		self.close()
		self.emit(SIGNAL("actionDeleted(int)"),self.actionIndex)

	@pyqtSignature("on_upButton_clicked()")
	def on_upButton_clicked(self):
		self.emit(SIGNAL("actionMove(int,int)"),self.actionIndex,-1)
		
	@pyqtSignature("on_downButton_clicked()")
	def on_downButton_clicked(self):
		self.emit(SIGNAL("actionMove(int,int)"),self.actionIndex,+1)
