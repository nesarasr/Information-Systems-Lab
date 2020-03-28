

from __future__ import print_function
from datetime import date, datetime, timedelta
import pymysql
from PyQt5 import QtGui , uic ,QtWidgets , QtCore
from PyQt5.QtWidgets import QMessageBox
import pyqtgraph
import sys



connection = pymysql.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='abc_db',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
                              #use_pure=False)
cursor = connection.cursor()

def save_func():
    list1=[]
    list1.append(dlg.did.text())
    list1.append(dlg.dname.text())
    list1.append(dlg.dloc.text())
    add_dept = ("INSERT INTO department "
               "(DID,DNAME,LOCATION) "
               "VALUES (%s, %s %s)")
    data_dept = (list[0],list[1],list[2])
# Insert new student
    cursor.execute(add_dept, data_dept)
    connection.commit()   ##vv imp, needs to save the data
    
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
    dlg.exec_()