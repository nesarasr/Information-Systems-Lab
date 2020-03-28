from __future__ import print_function
from datetime import date, datetime, timedelta
import pymysql
from PyQt5 import QtGui , uic ,QtWidgets , QtCore
from PyQt5.QtWidgets import QMessageBox
import sys

def save_func():
    list1=[]
    y=dlg.did.text()
    list1.append(dlg.dname.text())
    list1.append(dlg.dloc.text())
    connection = pymysql.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='abc_db',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
                              #use_pure=False)
    cursor = connection.cursor()
    print("connected")

    add_dept = ("INSERT INTO department "
               
               "VALUES (%s,%s,%s)")
    print("cp-1")
    data_dept = (y,list1[0],list1[1])
    print("cp-2")
    cursor.execute(add_dept, data_dept)
    print("cp-3")
    connection.commit()
    print("cp-4") ##vv imp, needs to save the data
    
def reset():
    dlg.did.clear()
    dlg.dname.clear()
    dlg.dloc.clear()
  

if __name__=='__main__':

    
    app=QtWidgets.QApplication(sys.argv)
    dlg = uic.loadUi("department_details.ui")
    dlg.setWindowTitle("Save Details")
    dlg.save.clicked.connect(save_func)
    dlg.reset.clicked.connect(reset)
    dlg.show()
    print("show")
    dlg.exec_()
