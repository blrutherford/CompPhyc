import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
plt.style.use('classic')
mpl.rc("figure", facecolor='white')
from matplotlib.ticker import AutoMinorLocator

x = [-100, -30, -10, -3, -1, 1, 3, 10, 30, 100]
y = [-0.36438, -0.11074, -0.038110, -0.01254, -0.005405, 0.001972, 0.009321, 0.035064, 0.107382, 0.361620]


f, ax = plt.subplots(1)
ax.tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax.tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minor_locator2)
ax.yaxis.set_minor_locator(minor_locator)

p1 = np.poly1d(np.polyfit(x, y, deg=1))
err1 = np.polyval(p1, x)


print(p1)

plt.scatter(x, y)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y,6))(np.unique(x)))
plt.xlim(-100,100)
plt.ylabel("Voltage (mV)")
plt.xlabel("Current (microAmps)")
plt.show()