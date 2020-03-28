# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:48:55 2019

@author: user
"""

from PyQt5 import QtGui , uic ,QtWidgets , QtCore
from PyQt5.QtWidgets import QMessageBox
import pyqtgraph
import sys
import numpy as np
import csv

def save_func():
    list1=[]
    list1.append(dlg.txt1.text())
    list1.append(dlg.txt2.text())
    list1.append(dlg.txt3.text())
    list1.append(dlg.txt4.text())
    list1.append(dlg.txt5.text())
    if dlg.radio1.isChecked():
        list1.append("Male")
    if dlg.radio2.isChecked():
        list1.append("Female")
    list1.append(dlg.txt6.text())
    list2=[{"Name":list1[0],"Department":list1[1],"Semester":list1[2],"Roll no":list1[3],"Phone number":list1[4],"Gender":list1[5],"Matriculation":list1[6]}]
    fields=["Name","Department","Semester","Roll no","Phone number","Gender","Matriculation"]
    with open("save.csv", 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames = fields)
        csvwriter.writeheader()
        csvwriter.writerows(list2)
    dialog()
    
def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")        
    mbox.exec_() 

    
def reset():
    dlg.txt1.clear()
    dlg.txt2.clear()
    dlg.txt3.clear()
    dlg.txt4.clear()
    dlg.txt5.clear()
    dlg.txt6.clear()
    dlg.area1.clear()

if __name__=='__main__':
    
    app=QtWidgets.QApplication(sys.argv)
    dlg = uic.loadUi("E:/18IM30014/Lab 9 28Sep/lab_ise_gui/lab_ise_gui/assignment.ui")
    dlg.setWindowTitle("Deatils")
    dlg.save.clicked.connect(save_func)
    dlg.reset.clicked.connect(reset)
    dlg.show()
    dlg.exec_()