# 2D/test_pylab.py
import os
from pylab import *
from test import *
import matplotlib
import numpy as np
# print 'matplotlib.__version__=', matplotlib.__version__

ion()
figure()
show()

def f(x):
    return np.sin(x)
M = 1000
x = np.linspace(0, 2*np.pi, 100)

for i in range(M):
    phase = i/10.
    xp = x + phase
    # print 'iteration ', i
    y = f(xp)
    plt.clf()
    plt.subplot(311)
    plot(x,y,'k')
    plt.subplot(312)
    plot(x,y,'k')
    plt.subplot(313)
    plot(x,y,'k')

    draw()
