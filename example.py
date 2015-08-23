
from PyQt5 import Qt, QtWidgets
import qtgevent
qtgevent.install()
import gevent
from gevent import monkey
monkey.patch_all()
import time


def test_greenlet(name):
    i = 1
    while True:
        print(name, i)
        i += 1
        time.sleep(1)


def btn_clicked():
    gevent.spawn(test_greenlet, "C")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    mainwin = QtWidgets.QMainWindow()
    btn = QtWidgets.QPushButton('Start greenlet', mainwin)
    btn.clicked.connect(btn_clicked)
    gevent.spawn(test_greenlet, 'A')
    gevent.spawn(test_greenlet, 'B')

    mainwin.show()
    app.exec_()
