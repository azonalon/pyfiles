#!/bin/python
import time
import random
import numpy as np
# import multiprocessing as mp
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

from multiprocessing import Process, Pipe


def counter_writer(conn):
    for i in range(0, 100):
        time.sleep(0.1)
        conn.send((random.random(), random.random()))
    conn.close()


class PIDSpinBoxes:
    def __init__(self):
        self.widget = QtGui.QWidget()
        self.layout = QtGui.QGridLayout()
        self.widget.setLayout(self.layout)
        self.sboxes = [pg.SpinBox(value=5.0, bounds=[0, 10]) for i in range(0,3)]
        self.labels = [(QtGui.QLabel(), label) for label in ["p", "i", "d"]]

        for i, sbox in enumerate(self.sboxes):
            self.layout.addWidget(sbox, 1, i)
        for i, (label, text) in enumerate(self.labels):
            label.setText(text)
            self.layout.addWidget(label, 0, i)

        self.event_handler = None
    def on_update(self):
        values = [ sb.value for sb in self.sboxes ]
        if self.event_handler is not None:
            self.event_handler(values)
    def connect(self, func):
        self.event_handler = func

class ScrollPlotterWidget:
    def __init__(self):
        self.data = np.zeros(100)
        self.widget = pg.PlotWidget()
        self.curve = self.widget.plot(self.data)

    def add_value(self, value):
        self.data[0] = value
        self.data = np.roll(self.data, -1)
        self.curve.setData(self.data)

class XYHistoryPlotterWidget:
    def __init__(self):
        self.xdata = np.zeros(100)
        self.ydata = np.zeros(100)
        self.widget = pg.PlotWidget()
        self.curve = self.widget.plot(self.xdata, self.ydata)

    def add_point(self, x, y):
        self.xdata[0] = x
        self.ydata[0] = y
        self.xdata = np.roll(self.xdata, -1)
        self.ydata = np.roll(self.ydata, -1)
        self.curve.setData(self.xdata, self.ydata)

class XYPIDWidget:
    def __init__(self, ):
        self.widget = QtGui.QWidget()
        self.layout = QtGui.QGridLayout()
        self.widget.setLayout(self.layout)

        self.xSpinBox = PIDSpinBoxes()
        self.ySpinBox = PIDSpinBoxes()
        self.spwdx = ScrollPlotterWidget()
        self.spwdy = ScrollPlotterWidget()
        self.sphxy = XYHistoryPlotterWidget()
        self.layout.addWidget(self.xSpinBox.widget)
        self.layout.addWidget(self.spwdx.widget)
        self.layout.addWidget(self.ySpinBox.widget)
        self.layout.addWidget(self.spwdy.widget)
        self.layout.addWidget(self.sphxy.widget)
    def add_point(self, x, y):
        x, y = np.random.random(size=2)
        self.spwdx.add_value(x)
        self.spwdy.add_value(y)
        self.sphxy.add_point(*(x,y))


app = QtGui.QApplication([])
win = QtGui.QMainWindow()
win.setWindowTitle('Piezo Mirror Stabilization Controller')
cw = XYPIDWidget()
win.setCentralWidget(cw.widget)
win.show()




if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=counter_writer, args=(child_conn,))
    p.start()

    def update():
        x, y = np.random.random(size=2)
        cw.add_point(x, y)


    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(50)
    pg.QtGui.QApplication.instance().exec_()
