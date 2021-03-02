# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(523, 312)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 80, 231, 201))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pb_8 = QPushButton(self.gridLayoutWidget)
        self.pb_8.setObjectName(u"pb_8")
        font = QFont()
        font.setBold(True)
        self.pb_8.setFont(font)

        self.gridLayout.addWidget(self.pb_8, 3, 1, 1, 1)

        self.pb_9 = QPushButton(self.gridLayoutWidget)
        self.pb_9.setObjectName(u"pb_9")
        self.pb_9.setFont(font)

        self.gridLayout.addWidget(self.pb_9, 3, 2, 1, 1)

        self.pb_sum = QPushButton(self.gridLayoutWidget)
        self.pb_sum.setObjectName(u"pb_sum")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.pb_sum.setFont(font1)

        self.gridLayout.addWidget(self.pb_sum, 2, 3, 1, 1)

        self.pb_6 = QPushButton(self.gridLayoutWidget)
        self.pb_6.setObjectName(u"pb_6")
        self.pb_6.setFont(font)

        self.gridLayout.addWidget(self.pb_6, 4, 2, 1, 1)

        self.pb_2 = QPushButton(self.gridLayoutWidget)
        self.pb_2.setObjectName(u"pb_2")
        self.pb_2.setFont(font)

        self.gridLayout.addWidget(self.pb_2, 5, 1, 1, 1)

        self.pb_plus = QPushButton(self.gridLayoutWidget)
        self.pb_plus.setObjectName(u"pb_plus")
        self.pb_plus.setFont(font)

        self.gridLayout.addWidget(self.pb_plus, 6, 0, 1, 1)

        self.pb_4 = QPushButton(self.gridLayoutWidget)
        self.pb_4.setObjectName(u"pb_4")
        self.pb_4.setFont(font)

        self.gridLayout.addWidget(self.pb_4, 4, 0, 1, 1)

        self.pb_sub = QPushButton(self.gridLayoutWidget)
        self.pb_sub.setObjectName(u"pb_sub")
        self.pb_sub.setFont(font1)

        self.gridLayout.addWidget(self.pb_sub, 3, 3, 1, 1)

        self.pb_kok = QPushButton(self.gridLayoutWidget)
        self.pb_kok.setObjectName(u"pb_kok")
        self.pb_kok.setFont(font)

        self.gridLayout.addWidget(self.pb_kok, 2, 2, 1, 1)

        self.pb_7 = QPushButton(self.gridLayoutWidget)
        self.pb_7.setObjectName(u"pb_7")
        self.pb_7.setFont(font)

        self.gridLayout.addWidget(self.pb_7, 3, 0, 1, 1)

        self.pb_5 = QPushButton(self.gridLayoutWidget)
        self.pb_5.setObjectName(u"pb_5")
        self.pb_5.setFont(font)

        self.gridLayout.addWidget(self.pb_5, 4, 1, 1, 1)

        self.pb_tersi = QPushButton(self.gridLayoutWidget)
        self.pb_tersi.setObjectName(u"pb_tersi")
        self.pb_tersi.setFont(font)

        self.gridLayout.addWidget(self.pb_tersi, 2, 0, 1, 1)

        self.pb_1 = QPushButton(self.gridLayoutWidget)
        self.pb_1.setObjectName(u"pb_1")
        self.pb_1.setFont(font)

        self.gridLayout.addWidget(self.pb_1, 5, 0, 1, 1)

        self.pb_perc = QPushButton(self.gridLayoutWidget)
        self.pb_perc.setObjectName(u"pb_perc")
        self.pb_perc.setEnabled(False)
        self.pb_perc.setFont(font)

        self.gridLayout.addWidget(self.pb_perc, 1, 0, 1, 1)

        self.pb_3 = QPushButton(self.gridLayoutWidget)
        self.pb_3.setObjectName(u"pb_3")
        self.pb_3.setFont(font)

        self.gridLayout.addWidget(self.pb_3, 5, 2, 1, 1)

        self.pb_C = QPushButton(self.gridLayoutWidget)
        self.pb_C.setObjectName(u"pb_C")
        self.pb_C.setFont(font)

        self.gridLayout.addWidget(self.pb_C, 1, 1, 1, 1)

        self.pb_div = QPushButton(self.gridLayoutWidget)
        self.pb_div.setObjectName(u"pb_div")
        self.pb_div.setFont(font1)

        self.gridLayout.addWidget(self.pb_div, 5, 3, 1, 1)

        self.pb_ce = QPushButton(self.gridLayoutWidget)
        self.pb_ce.setObjectName(u"pb_ce")
        self.pb_ce.setFont(font)

        self.gridLayout.addWidget(self.pb_ce, 1, 2, 1, 1)

        self.pb_karesi = QPushButton(self.gridLayoutWidget)
        self.pb_karesi.setObjectName(u"pb_karesi")
        self.pb_karesi.setFont(font)

        self.gridLayout.addWidget(self.pb_karesi, 2, 1, 1, 1)

        self.pb_mul = QPushButton(self.gridLayoutWidget)
        self.pb_mul.setObjectName(u"pb_mul")
        self.pb_mul.setFont(font1)

        self.gridLayout.addWidget(self.pb_mul, 4, 3, 1, 1)

        self.pb_del = QPushButton(self.gridLayoutWidget)
        self.pb_del.setObjectName(u"pb_del")
        self.pb_del.setFont(font1)

        self.gridLayout.addWidget(self.pb_del, 1, 3, 1, 1)

        self.pb_10 = QPushButton(self.gridLayoutWidget)
        self.pb_10.setObjectName(u"pb_10")
        self.pb_10.setFont(font)

        self.gridLayout.addWidget(self.pb_10, 6, 1, 1, 1)

        self.pb_decimal = QPushButton(self.gridLayoutWidget)
        self.pb_decimal.setObjectName(u"pb_decimal")
        self.pb_decimal.setFont(font)

        self.gridLayout.addWidget(self.pb_decimal, 6, 2, 1, 1)

        self.pb_equel = QPushButton(self.gridLayoutWidget)
        self.pb_equel.setObjectName(u"pb_equel")
        self.pb_equel.setFont(font1)

        self.gridLayout.addWidget(self.pb_equel, 6, 3, 1, 1)

        self.lineEdit_deger = QLineEdit(self.centralwidget)
        self.lineEdit_deger.setObjectName(u"lineEdit_deger")
        self.lineEdit_deger.setGeometry(QRect(30, 50, 231, 23))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(10)
        font2.setBold(True)
        self.lineEdit_deger.setFont(font2)
        self.lineEdit_deger.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_save = QLineEdit(self.centralwidget)
        self.lineEdit_save.setObjectName(u"lineEdit_save")
        self.lineEdit_save.setGeometry(QRect(30, 20, 231, 21))
        font3 = QFont()
        font3.setItalic(True)
        self.lineEdit_save.setFont(font3)
        self.lineEdit_save.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 20, 121, 16))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(270, 40, 241, 241))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pb_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pb_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pb_sum.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pb_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pb_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pb_plus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.pb_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pb_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pb_kok.setText(QCoreApplication.translate("MainWindow", u"\u221ax", None))
        self.pb_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pb_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pb_tersi.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.pb_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pb_perc.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pb_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pb_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pb_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.pb_karesi.setText(QCoreApplication.translate("MainWindow", u"x2", None))
        self.pb_mul.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pb_del.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.pb_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pb_decimal.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.pb_equel.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0130\u015flem Ge\u00e7mi\u015fi", None))
    # retranslateUi

