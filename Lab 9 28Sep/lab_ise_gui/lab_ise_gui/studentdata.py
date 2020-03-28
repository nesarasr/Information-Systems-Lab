# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 03:30:16 2019

@author: User
"""
import sys
import csv
from PyQt5 import QtGui , uic ,QtWidgets , QtCore
fields = ['Name', 'Department', 'Semester', 'Roll No','Phone No','Gender','Matriculation(With year of passing','10+2(With year of passing)','Comments']
filename = "Student Data.csv"
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
      
def save():
    
def reset():
    dlg.namel.clear()
    dlg.deptl.clear()
    dlg.seml.clear()
    dlg.rolll.clear()
    dlg.male.clear()
    dlg.female.clear()
    dlg.matl.clear()
    dlg.tenplusl.clear()
    dlg.commentl.clear()
if __name__=='__main__':
    
    app=QtWidgets.QApplication(sys.argv)
    dlg=uic.loadUi("studentdata.ui") #Main Window
    dlg.setWindowTitle('DATA INPUT')
    dlg.save.clicked.connect()
    dlg.reset.clicked.connect()
    dlg.show()
    app.exec_()