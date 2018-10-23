# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bens-Acer\Desktop\myUI.ui'
#
# Created: Tue Oct 23 02:11:28 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 100, 391, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticle = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticle.setContentsMargins(0, 0, 0, 0)
        self.verticle.setObjectName("verticle")
        self.temp_sensor = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.temp_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_sensor.setObjectName("temp_sensor")
        self.verticle.addWidget(self.temp_sensor)
        self.gas_sensor = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.gas_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.gas_sensor.setObjectName("gas_sensor")
        self.verticle.addWidget(self.gas_sensor)
        self.light_sensor = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.light_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.light_sensor.setObjectName("light_sensor")
        self.verticle.addWidget(self.light_sensor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.temp_sensor.setText(QtWidgets.QApplication.translate("MainWindow", "0.0", None, -1))
        self.gas_sensor.setText(QtWidgets.QApplication.translate("MainWindow", "0.0", None, -1))
        self.light_sensor.setText(QtWidgets.QApplication.translate("MainWindow", "0.0", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

