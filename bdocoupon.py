# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bdocoupon.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 304)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lunch = QtWidgets.QPushButton(self.centralwidget)
        self.lunch.setGeometry(QtCore.QRect(370, 40, 111, 71))
        self.lunch.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lunch.setObjectName("lunch")

        self.daumid = QtWidgets.QLabel(self.centralwidget)
        self.daumid.setGeometry(QtCore.QRect(30, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.daumid.setFont(font)
        self.daumid.setObjectName("daumid")

        self.daumpw = QtWidgets.QLabel(self.centralwidget)
        self.daumpw.setGeometry(QtCore.QRect(30, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.daumpw.setFont(font)
        self.daumpw.setObjectName("daumpw")

        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(30, 220, 501, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setObjectName("description")

        self.save_account = QtWidgets.QCheckBox(self.centralwidget)
        self.save_account.setGeometry(QtCore.QRect(30, 120, 141, 21))
        self.save_account.setObjectName("save_account")

        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(30, 170, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName("status")

        self.daumid_input = QtWidgets.QLineEdit(self.centralwidget)
        self.daumid_input.setGeometry(QtCore.QRect(190, 40, 141, 31))
        self.daumid_input.setObjectName("daumid_input")

        self.daumpw_input = QtWidgets.QLineEdit(self.centralwidget)
        self.daumpw_input.setGeometry(QtCore.QRect(190, 80, 141, 31))
        self.daumpw_input.setObjectName("daumpw_input")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "검은사막 쿠폰 입력 프로그램"))
        self.lunch.setText(_translate("MainWindow", "실행"))
        self.daumid.setText(_translate("MainWindow", "Daum ID"))
        self.daumpw.setText(_translate("MainWindow", "Daum Password"))
        self.description.setText(_translate("MainWindow", "본 프로그램은 OpenSource로 모든 소스 코드를 공개하고 있습니다."))
        self.save_account.setText(_translate("MainWindow", "계정 정보 저장"))
        self.status.setText(_translate("MainWindow", "Status"))
        self.pushButton.setText(_translate("MainWindow", "Github"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

