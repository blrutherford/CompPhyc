import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('classic')
mpl.rc("figure", facecolor='white')
from matplotlib.ticker import AutoMinorLocator

y = [1, 10, 20, 40, 60, 80, 100, 150, 200, 273, 293, 298, 300, 400, 500, 600, 700, 800, 900]
x = [0.000016e-8, 0.000137e-8, 0.00196e-8, 0.0544e-8, 0.266e-8, 0.606e-8, 1.02e-8, 2.09e-8, 3.18e-8, 4.82e-8, 5.28e-8, 5.39e-8, 5.44e-8, 7.83e-8, 10.3e-8, 13e-8, 15.7e-8, 18.6e-8, 21.5e-8]
p = np.poly1d(np.polyfit(x, y, deg=9))


print(p)
err = np.polyval(p, x)
print(err)

f, ax = plt.subplots(1)
ax.tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax.tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minor_locator2)
ax.yaxis.set_minor_locator(minor_locator)

plt.scatter(x, y)
plt.xlim(0,2.5e-7)
plt.ylim(0, 1000)
plt.ylabel("Temperature (K)")
plt.xlabel("Resistivity (Ohm-meters)")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x,y,6))(np.unique(x)))
plt.show()
