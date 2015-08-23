from __future__ import print_function

from PyQt5 import Qt, QtCore, QtWidgets
import qtgevent
qtgevent.install()
import gevent
from gevent import monkey; monkey.patch_all()
import functools
import time
import greenlet

def btn_clicked():
    print('before sleep')
    gevent.sleep(3)
    print('after sleep')

if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    mainwin = QtWidgets.QMainWindow()
    btn = QtWidgets.QPushButton('Start greenlet', mainwin)
    btn.clicked.connect(btn_clicked)
    mainwin.show()
    app.exec_()
