# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(318, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inputValidaCpf = QtWidgets.QLineEdit(self.centralwidget)
        self.inputValidaCpf.setObjectName("inputValidaCpf")
        self.gridLayout.addWidget(self.inputValidaCpf, 0, 1, 1, 1)
        self.btnVerificaCpf = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerificaCpf.setObjectName("btnVerificaCpf")
        self.gridLayout.addWidget(self.btnVerificaCpf, 0, 2, 1, 1)
        self.respostaValidaCpf = QtWidgets.QLabel(self.centralwidget)
        self.respostaValidaCpf.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.respostaValidaCpf.setFrameShape(QtWidgets.QFrame.Box)
        self.respostaValidaCpf.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.respostaValidaCpf.setText("")
        self.respostaValidaCpf.setAlignment(QtCore.Qt.AlignCenter)
        self.respostaValidaCpf.setObjectName("respostaValidaCpf")
        self.gridLayout.addWidget(self.respostaValidaCpf, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validar CPF"))
        self.label.setText(_translate("MainWindow", "CPF"))
        self.btnVerificaCpf.setText(_translate("MainWindow", "validar"))