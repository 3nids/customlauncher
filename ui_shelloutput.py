# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_shelloutput.ui'
#
# Created: Wed Apr 11 09:16:22 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_shellOutput(object):
    def setupUi(self, shellOutput):
        shellOutput.setObjectName(_fromUtf8("shellOutput"))
        shellOutput.resize(400, 300)
        shellOutput.setWindowTitle(QtGui.QApplication.translate("shellOutput", "Custom Launcher :: shell output", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(shellOutput)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QtGui.QTextBrowser(shellOutput)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(shellOutput)
        QtCore.QMetaObject.connectSlotsByName(shellOutput)

    def retranslateUi(self, shellOutput):
        pass

