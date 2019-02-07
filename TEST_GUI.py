# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rjeff\Documents\PROJECTS\WeRocketry\GUI\TEST_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

def fileBrowser(root):
    
    lst = os.listdir(root)
    #x = lst.sort()
    dirList = [os.path.splitext(x)[0] for x in lst]
    
    x = max(dirList)
    
    return dirList
    
    

class Ui_MainWindow(object):
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setGeometry(50,50,500,800)
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.label1.setText(_translate("MainWindow", "Enter file path"))
        self.label.setText(_translate("MainWindow", "Directory"))
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 120, 371, 51))
        self.textEdit.setObjectName("textEdit")
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 90, 111, 21))
        self.label1.setFrameShape(QtWidgets.QFrame.Box)
        self.label1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label1.setObjectName("label1")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 250, 371, 281))
        self.textBrowser.setObjectName("textBrowser")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 220, 111, 21))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @pyqtSlot()
    def on_click(self):
        self.textBrowser.clear()
        filePath = self.textEdit.toPlainText()
        dirList = fileBrowser(filePath)
        for i in range(len(dirList)):    
            self.textBrowser.insertPlainText(dirList[i] + "\n")
        
#    def retranslateUi(self, MainWindow):
#        _translate = QtCore.QCoreApplication.translate
#        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#        self.pushButton.setText(_translate("MainWindow", "Run"))
#        self.label1.setText(_translate("MainWindow", "Enter file path"))
#        self.label.setText(_translate("MainWindow", "Directory"))
        
###central to program execution
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())