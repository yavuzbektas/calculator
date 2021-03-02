import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile,Slot
from ui_calc import Ui_MainWindow
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import sys,math


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.value_update()
        self.setWindowTitle("Hesap Makinesi - v0.0")
    def value_update(self):
        
        self.ui.pb_1.clicked.connect(lambda x: self.update(1))
        self.ui.pb_2.clicked.connect(lambda x: self.update(2))
        self.ui.pb_3.clicked.connect(lambda x: self.update(3))
        self.ui.pb_4.clicked.connect(lambda x: self.update(4))
        self.ui.pb_5.clicked.connect(lambda x: self.update(5))
        self.ui.pb_6.clicked.connect(lambda x: self.update(6))
        self.ui.pb_7.clicked.connect(lambda x: self.update(7))
        self.ui.pb_8.clicked.connect(lambda x: self.update(8))
        self.ui.pb_9.clicked.connect(lambda x: self.update(9))
        self.ui.pb_10.clicked.connect(lambda x: self.update(0))
        self.ui.pb_C.clicked.connect(self.del_all)
        self.ui.pb_ce.clicked.connect(self.del_one)
        self.ui.pb_sum.clicked.connect(self.add)
        self.ui.pb_sub.clicked.connect(self.sub)
        self.ui.pb_mul.clicked.connect(self.mul)
        self.ui.pb_div.clicked.connect(self.div)
        self.ui.pb_equel.clicked.connect(self.equel)
        self.ui.pb_decimal.clicked.connect(self.decimal)
        self.ui.pb_plus.clicked.connect(self.plus)
        self.ui.pb_tersi.clicked.connect(self.tersle)
        self.ui.pb_karesi.clicked.connect(self.square)
        self.ui.pb_kok.clicked.connect(self.root)
        self.ui.pb_del.clicked.connect(self.del_char)
        
    def resizeEvent(self, event):
        print("resize")
        QMainWindow.resizeEvent(self, event)
    def operator_check(self,new_operator):
        old_val=self.ui.lineEdit_save.text()
    
        
        first_val=old_val.split(" ")[0]
        
        
        if len(old_val.split(" "))>1:
            self.ui.lineEdit_save.setText(first_val + new_operator)
            return False
        else:
            return True
    def tersle(self):
        old_val=self.ui.lineEdit_deger.text()
        old_val=1/float(old_val)
        self.ui.lineEdit_deger.setText(str(old_val))
    def square(self):
        old_val=self.ui.lineEdit_deger.text()
        old_val=float(old_val)*float(old_val)
        self.ui.lineEdit_deger.setText(str(old_val))
    def root(self):
        old_val=self.ui.lineEdit_deger.text()
        old_val=math.sqrt(float(old_val))
        self.ui.lineEdit_deger.setText(str(old_val))
    def add(self):
        if self.operator_check(" + ")==True:
       
            old_val=self.ui.lineEdit_deger.text()
            self.ui.lineEdit_save.setText(old_val + " + ")
            self.ui.lineEdit_deger.setText("")
    def sub(self):
        if self.operator_check(" - ")==True:
            old_val=self.ui.lineEdit_deger.text()
            self.ui.lineEdit_save.setText(old_val + " - ")
            self.ui.lineEdit_deger.setText("")
    def mul(self):
        if self.operator_check(" * ")==True:
            old_val=self.ui.lineEdit_deger.text()
            self.ui.lineEdit_save.setText(old_val + " * ")
            self.ui.lineEdit_deger.setText("")
    def div(self):
        if self.operator_check(" / ")==True:
            old_val=self.ui.lineEdit_deger.text()
            self.ui.lineEdit_save.setText(old_val + " / ")
            self.ui.lineEdit_deger.setText("")
    def del_char(self):
        old_val=self.ui.lineEdit_deger.text()[:-1]
        
        self.ui.lineEdit_deger.setText(str(old_val))
    def del_one(self):
        self.ui.lineEdit_deger.setText("")
    def del_all(self):
        self.ui.lineEdit_save.setText("")
        self.ui.lineEdit_deger.setText("")
    def decimal(self):
        old_val=self.ui.lineEdit_deger.text()
        for i in old_val:
            if i==".":
                return False
        
        self.ui.lineEdit_deger.setText(old_val + ".")
    def plus(self):
        old_val=self.ui.lineEdit_deger.text()
        old_val=float(old_val)*(-1)
        self.ui.lineEdit_deger.setText(str(old_val))
    def equel(self):
        old_val=self.ui.lineEdit_save.text()
    
        operator=old_val.split(" ")[1]
        first_val=float(old_val.split(" ")[0])
        second_val=float(self.ui.lineEdit_deger.text())
        self.calculate(first_val,second_val,operator)
    def calculate(self,first_val,second_val,operator):    
        if operator=="+":
            result=first_val + second_val
            print("toplama yapıldı")
        elif operator=="-":
            result=first_val - second_val
            print("cıkarma yapıldı")
        elif operator=="*":
            result=first_val * second_val
            print("çarpma yapıldı")
        elif operator=="/":
            result=first_val / second_val
            print("bölme yapıldı")   
        else:
            print("hatalı işlem",operator)
        print(result)
        self.historical(self.ui.lineEdit_save.text(),self.ui.lineEdit_deger.text(),str(result))
        self.ui.lineEdit_save.setText("")
        self.ui.lineEdit_deger.setText(str(result))
        
    def update(self,sender):
        
        old_val=self.ui.lineEdit_deger.text()
        new_val=str( old_val)+str(sender)
        self.ui.lineEdit_deger.setText(new_val)
    def historical(self,f_val,s_val,result):
        self.ui.listWidget.insertItem(0,(f_val+s_val+"="+result))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())