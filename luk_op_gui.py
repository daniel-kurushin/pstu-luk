# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'luk_operator_prototype.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 434)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ctgt = QtWidgets.QLCDNumber(self.centralwidget)
        self.ctgt.setGeometry(QtCore.QRect(40, 240, 128, 64))
        self.ctgt.setDigitCount(4)
        self.ctgt.setProperty("intValue", 60)
        self.ctgt.setObjectName("ctgt")
        self.btn_gt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gt.setGeometry(QtCore.QRect(430, 210, 91, 23))
        self.btn_gt.setObjectName("btn_gt")
        self.btn_ku = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ku.setGeometry(QtCore.QRect(430, 240, 91, 23))
        self.btn_ku.setObjectName("btn_ku")
        self.btn_pg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pg.setGeometry(QtCore.QRect(430, 300, 91, 23))
        self.btn_pg.setObjectName("btn_pg")
        self.btn_vtg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vtg.setGeometry(QtCore.QRect(430, 270, 91, 23))
        self.btn_vtg.setObjectName("btn_vtg")
        self.gt = QtWidgets.QLabel(self.centralwidget)
        self.gt.setGeometry(QtCore.QRect(20, 30, 404, 122))
        self.gt.setPixmap(QtGui.QPixmap("img/зугт0.png"))
        self.gt.setScaledContents(True)
        self.gt.setObjectName("gt")
        self.ss = QtWidgets.QLabel(self.centralwidget)
        self.ss.setGeometry(QtCore.QRect(230, 210, 125, 125))
        self.ss.setText("")
        self.ss.setPixmap(QtGui.QPixmap("img/сс0.png"))
        self.ss.setScaledContents(True)
        self.ss.setObjectName("ss")
        self.btn_gb = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gb.setGeometry(QtCore.QRect(430, 330, 91, 23))
        self.btn_gb.setObjectName("btn_gb")
        self.btn_call = QtWidgets.QPushButton(self.centralwidget)
        self.btn_call.setGeometry(QtCore.QRect(430, 360, 91, 41))
        self.btn_call.setObjectName("btn_call")
        self.zuku = QtWidgets.QLabel(self.centralwidget)
        self.zuku.setGeometry(QtCore.QRect(440, 30, 125, 125))
        self.zuku.setText("")
        self.zuku.setPixmap(QtGui.QPixmap("img/зуку0.png"))
        self.zuku.setScaledContents(True)
        self.zuku.setObjectName("zuku")
        self.vtg = QtWidgets.QLabel(self.centralwidget)
        self.vtg.setGeometry(QtCore.QRect(570, 30, 125, 125))
        self.vtg.setText("")
        self.vtg.setPixmap(QtGui.QPixmap("img/втг1.png"))
        self.vtg.setScaledContents(True)
        self.vtg.setObjectName("vtg")
        self.zapg = QtWidgets.QLabel(self.centralwidget)
        self.zapg.setGeometry(QtCore.QRect(700, 30, 125, 125))
        self.zapg.setText("")
        self.zapg.setPixmap(QtGui.QPixmap("img/запг1.png"))
        self.zapg.setScaledContents(True)
        self.zapg.setObjectName("zapg")
        self.zagb = QtWidgets.QLabel(self.centralwidget)
        self.zagb.setGeometry(QtCore.QRect(830, 30, 125, 125))
        self.zagb.setText("")
        self.zagb.setPixmap(QtGui.QPixmap("img/загб1.png"))
        self.zagb.setScaledContents(True)
        self.zagb.setObjectName("zagb")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(535, 210, 421, 192))
        self.log.setObjectName("log")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(10, 380, 141, 23))
        self.btn_start.setObjectName("btn_start")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_gt.setText(_translate("MainWindow", "Закрыть ЗУ ГТ"))
        self.btn_ku.setText(_translate("MainWindow", "Закрыть ЗУ КУ"))
        self.btn_pg.setText(_translate("MainWindow", "Открыть ЗА ПГ"))
        self.btn_vtg.setText(_translate("MainWindow", "Включить ВТГ"))
        self.btn_gb.setText(_translate("MainWindow", "Открыть ЗА ГБ"))
        self.btn_call.setText(_translate("MainWindow", "Звонок\n"
"диспетчеру"))
        self.btn_start.setText(_translate("MainWindow", "Запустить демо-сценарий"))

