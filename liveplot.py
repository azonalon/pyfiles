#!/bin/python
import time
import random
import subprocess as sp
import numpy as np



import multiprocessing as mp
from multiprocessing import Process, Pipe

def counter_writer(conn):
    for i in range(0,100):
        time.sleep(0.1)
        conn.send(random.random())
    conn.close()

parent_conn, child_conn = Pipe()
p = Process(target=counter_writer, args=(child_conn,))
p.start()

import pyqtgraph as pg
# from pyqtgraph.Qt import QtCore, QtGui
# # 1) Simplest approach -- update data in the array such that plot appears to scroll
# #    In these examples, the array size is fixed.
win = pg.GraphicsWindow()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')
data1 = np.zeros(100)
pl = win.addPlot()
curve = pl.plot(data1)
#
#

def update():
    global data1, curve

    try:
        while parent_conn.poll():
            value = parent_conn.recv()
            print(value)
            data1[0] = value
            data1 = np.roll(data1, -1)
        curve.setData(data1)
    except EOFError:
        print("Connection was closed")
    # time.sleep(1)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)
pg.QtGui.QApplication.instance().exec_()
