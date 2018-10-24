# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bens-Acer\Desktop\myui3.ui'
#
# Created: Tue Oct 23 22:52:16 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import random
import time

class Ui_homeApp(object):
    def setupUi(self, homeApp):
        homeApp.setObjectName("homeApp")
        homeApp.resize(1117, 935)
        self.centralwidget = QtWidgets.QWidget(homeApp)
        self.centralwidget.setStyleSheet("background-color: rgb(35, 41, 44);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1121, 131))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(42, 51, 63);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.temp_sensor = QtWidgets.QLabel(self.centralwidget)
        self.temp_sensor.setGeometry(QtCore.QRect(-30, 170, 1151, 131))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.temp_sensor.setFont(font)
        self.temp_sensor.setStyleSheet("color: rgb(255, 255, 255);")
        self.temp_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_sensor.setObjectName("temp_sensor")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(-10, 130, 1151, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(570, 220, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label5.setFont(font)
        self.label5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setObjectName("label5")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(-20, 250, 1161, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.humidity = QtWidgets.QLabel(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(-30, 320, 1151, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.humidity.setFont(font)
        self.humidity.setStyleSheet("color: rgb(255, 255, 255);")
        self.humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity.setObjectName("humidity")
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(580, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label7.setFont(font)
        self.label7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setObjectName("label7")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(-20, 380, 1161, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.light_sensor = QtWidgets.QLabel(self.centralwidget)
        self.light_sensor.setGeometry(QtCore.QRect(-20, 460, 1161, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.light_sensor.setFont(font)
        self.light_sensor.setStyleSheet("color: rgb(255, 255, 255);")
        self.light_sensor.setAlignment(QtCore.Qt.AlignCenter)
        self.light_sensor.setObjectName("light_sensor")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(-20, 510, 1161, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.airQuality = QtWidgets.QLabel(self.centralwidget)
        self.airQuality.setGeometry(QtCore.QRect(-20, 580, 1161, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.airQuality.setFont(font)
        self.airQuality.setStyleSheet("color: rgb(255, 255, 255);")
        self.airQuality.setAlignment(QtCore.Qt.AlignCenter)
        self.airQuality.setObjectName("airQuality")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, 650, 1151, 311))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        homeApp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(homeApp)
        self.statusbar.setObjectName("statusbar")
        homeApp.setStatusBar(self.statusbar)

        self.retranslateUi(homeApp)
        QtCore.QMetaObject.connectSlotsByName(homeApp)

    def retranslateUi(self, homeApp):
        homeApp.setWindowTitle(QtWidgets.QApplication.translate("homeApp", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("homeApp", "Welcome to the Home Automation Project", None, -1))
        self.temp_sensor.setText(QtWidgets.QApplication.translate("homeApp", "0.0", None, -1))
        self.label1.setText(QtWidgets.QApplication.translate("homeApp", "Temperature", None, -1))
        self.label5.setText(QtWidgets.QApplication.translate("homeApp", "°F", None, -1))
        self.label2.setText(QtWidgets.QApplication.translate("homeApp", "Humidity", None, -1))
        self.humidity.setText(QtWidgets.QApplication.translate("homeApp", "0.0%", None, -1))
        self.label7.setText(QtWidgets.QApplication.translate("homeApp", "RH", None, -1))
        self.label3.setText(QtWidgets.QApplication.translate("homeApp", "Lighting", None, -1))
        self.light_sensor.setText(QtWidgets.QApplication.translate("homeApp", "OFF", None, -1))
        self.label4.setText(QtWidgets.QApplication.translate("homeApp", "Air Quality", None, -1))
        self.airQuality.setText(QtWidgets.QApplication.translate("homeApp", "High", None, -1))
    def refreshText(self):

        time = QtCore.QTime.currentTime().toString()
        print("Time: " + time)

        sensor = generateRandowNumber()

        self.temp_sensor.setText(str(sensor))
        if sensor > 50:
            self.light_sensor.setText("ON")
        
        
        return time

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_homeApp()
    ui.setupUi(MainWindow)
    MainWindow.show()

    timer=QtCore.QTimer()
    timer.timeout.connect(ui.refreshText)
    timer.start(1000)

    sys.exit(app.exec_())
    
def generateRandowNumber():
    return random.randint(1,101)

if __name__ == '__main__':
    # App.main()
    main()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeApp = QtWidgets.QMainWindow()
    ui = Ui_homeApp()
    ui.setupUi(homeApp)
    homeApp.show()
    sys.exit(app.exec_())