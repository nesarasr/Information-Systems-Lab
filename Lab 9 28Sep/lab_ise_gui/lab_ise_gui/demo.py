# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:51:01 2019

@author: Satyajit
"""

from PyQt5 import QtGui , uic ,QtWidgets , QtCore
import pyqtgraph
import sys
import numpy as np

def sin_func():
    x = np.linspace(-np.pi, np.pi, 201)
    dlg.sine_plot.plot(np.sin(x),pen='b')    

def cos_func():
    x = np.linspace(-np.pi, np.pi, 201)
    dlg.cos_plot.plot(np.cos(x),pen='g')    

def reset_func():
    dlg.sine_plot.clear()
    dlg.cos_plot.clear()


def exit_func():
    sys.exit(0)





if __name__=='__main__':
    
    app=QtWidgets.QApplication(sys.argv)
    dlg=uic.loadUi("demo.ui") #Main Window
    dlg.setWindowTitle('plot_section')
    dlg.sine.clicked.connect(sin_func)
    dlg.cos.clicked.connect(cos_func)
    dlg.reset.clicked.connect(reset_func)
    dlg.exit.clicked.connect(exit_func)
    dlg.show()
    app.exec_()
#generateSynthSeismo.graphicsView.plot(las[m[den]],las.index,pen='y')