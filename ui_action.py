# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_action.ui'
#
# Created: Tue Apr 10 17:01:02 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Action(object):
    def setupUi(self, Action):
        Action.setObjectName(_fromUtf8("Action"))
        Action.resize(522, 107)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Action.sizePolicy().hasHeightForWidth())
        Action.setSizePolicy(sizePolicy)
        Action.setWindowTitle(QtGui.QApplication.translate("Action", "action", None, QtGui.QApplication.UnicodeUTF8))
        Action.setFrameShape(QtGui.QFrame.StyledPanel)
        Action.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(Action)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Action)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Action", "Icon", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.iconEdit = QtGui.QLineEdit(Action)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.iconEdit.setFont(font)
        self.iconEdit.setObjectName(_fromUtf8("iconEdit"))
        self.gridLayout.addWidget(self.iconEdit, 0, 2, 1, 1)
        self.iconButton = QtGui.QToolButton(Action)
        self.iconButton.setText(QtGui.QApplication.translate("Action", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.iconButton.setObjectName(_fromUtf8("iconButton"))
        self.gridLayout.addWidget(self.iconButton, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Action)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("Action", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.actionEdit = QtGui.QLineEdit(Action)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionEdit.setFont(font)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.gridLayout.addWidget(self.actionEdit, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Action)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("Action", "Tooltip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.tooltipEdit = QtGui.QLineEdit(Action)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tooltipEdit.setFont(font)
        self.tooltipEdit.setObjectName(_fromUtf8("tooltipEdit"))
        self.gridLayout.addWidget(self.tooltipEdit, 2, 2, 1, 1)
        self.deleteButton = QtGui.QToolButton(Action)
        self.deleteButton.setText(QtGui.QApplication.translate("Action", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 1, 0, 1, 1)

        self.retranslateUi(Action)
        QtCore.QMetaObject.connectSlotsByName(Action)

    def retranslateUi(self, Action):
        pass

