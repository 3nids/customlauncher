# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_actionmanager.ui'
#
# Created: Tue May 15 16:08:30 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ActionManager(object):
    def setupUi(self, ActionManager):
        ActionManager.setObjectName(_fromUtf8("ActionManager"))
        ActionManager.resize(665, 289)
        self.gridLayout = QtGui.QGridLayout(ActionManager)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(ActionManager)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.addActionButton = QtGui.QPushButton(ActionManager)
        self.addActionButton.setObjectName(_fromUtf8("addActionButton"))
        self.gridLayout.addWidget(self.addActionButton, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(ActionManager)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 645, 236))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setMargin(3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.actionsLayout = QtGui.QVBoxLayout()
        self.actionsLayout.setSpacing(3)
        self.actionsLayout.setObjectName(_fromUtf8("actionsLayout"))
        self.gridLayout_3.addLayout(self.actionsLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)

        self.retranslateUi(ActionManager)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ActionManager.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ActionManager.reject)
        QtCore.QMetaObject.connectSlotsByName(ActionManager)

    def retranslateUi(self, ActionManager):
        ActionManager.setWindowTitle(QtGui.QApplication.translate("ActionManager", "Custom Launcher", None, QtGui.QApplication.UnicodeUTF8))
        self.addActionButton.setText(QtGui.QApplication.translate("ActionManager", "Add action", None, QtGui.QApplication.UnicodeUTF8))

