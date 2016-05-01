import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import time



def rand(n):
    data = np.random.random(n)
    data[int(n*0.1):int(n*0.13)] += .5
    data[int(n*0.18)] += 2
    data[int(n*0.1):int(n*0.13)] *= 5
    data[int(n*0.18)] *= 20
    data *= 1e-12
    return data, np.arange(n, n+len(data)) / float(n)
    

app = QtGui.QApplication([])
win = QtGui.QMainWindow()
win.setWindowTitle('pyqtgraph example: SpinBox')
cw = QtGui.QWidget()
layout = QtGui.QGridLayout()
cw.setLayout(layout)
win.setCentralWidget(cw)

class PIDSpinBoxes:
    sboxes = [pg.SpinBox(value=5.0, bounds=[0, 10]) for i in range(0,3)]
    for i, sbox in enumerate(sboxes):
    layout.addWidget(sbox, 0, i)

# 1) Simplest approach -- update data in the array such that plot appears to scroll
#    In these examples, the array size is fixed.
p1 = pg.PlotWidget()
p2 = pg.PlotWidget()
layout.addWidget(p1)
layout.addWidget(p2)
data1 = rand(300)[1]
curve1 = p1.plot(data1)
curve2 = p2.plot(data1)
ptr1 = 0
def update1():
    global data1, curve1, ptr1
    data1[:-1] = data1[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
    data1[-1] = np.random.normal()
    curve1.setData(data1)
    
    ptr1 += 1
    curve2.setData(data1)
    curve2.setPos(ptr1, 0)
    
# update all plots
def update():
    update1()

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

sb = pg.SpinBox(value=5.0, bounds=[0, 10])


win.show()
## Start Qt event loop unless running in interactive mode or using pyside.
#if __name__ == '__main__':
#    import sys
#    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
QtGui.QApplication.instance().exec_()
