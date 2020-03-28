# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:42:07 2019

@author: Satyajit
"""
from PyQt5 import QtGui , uic ,QtWidgets , QtCore
import pyqtgraph
import sys
import numpy as np
from functools import partial


    
def exit_func():
    sys.exit(0)
if __name__=='__main__':
    a=str()
    
    app=QtWidgets.QApplication(sys.argv)
    dlg=uic.loadUi("calculator.ui") #Main Window
    dlg.setWindowTitle('calculator')
#    dlg.one.clicked.connect(partial(on_tab,'1'))
#    dlg.two.clicked.connect(partial(on_tab,'2'))
#    dlg.three.clicked.connect(partial(on_tab,'3'))
#    dlg.four.clicked.connect(partial(on_tab,'4'))
#    dlg.five.clicked.connect(partial(on_tab,'5'))
#    dlg.six.clicked.connect(partial(on_tab,'6'))
#    dlg.seven.clicked.connect(partial(on_tab,'7'))
#    dlg.eight.clicked.connect(partial(on_tab,'8'))
#    dlg.nine.clicked.connect(partial(on_tab,'9'))
#    dlg.zero.clicked.connect(partial(on_tab,'0'))
    dlg.exit.clicked.connect(exit_func)
    dlg.show()
    app.exec_()