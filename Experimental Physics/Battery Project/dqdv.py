import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
plt.style.use('classic')
mpl.rc("figure", facecolor='white')
from matplotlib.ticker import AutoMinorLocator

data_c = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 1\SLA\SLA C-D.xlsx", "Charge 3")
data_d = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 1\SLA\SLA C-D.xlsx", "Discharge 3")

volt = []
for i in range(7,9220):
    volt.append(data_c.iloc[i, 0])
for j in range(7,20577):
    volt.append(data_d.iloc[j, 0])


dqdv = []
for i in range(7,9220):
    dqdv.append(data_c.iloc[i, 6])
    if data_c.iloc[i, 6] >= 1000:
        dqdv.remove(data_c.iloc[i, 6])
        volt.remove(data_c.iloc[i, 0])
print(len(volt), len(dqdv))
for j in range(7,20577):
    dqdv.append(data_d.iloc[j, 0])
print(len(dqdv))
    #if data_d.iloc[j, 6] > 0:
        #dqdv.remove(data_d.iloc[j, 6])
       # volt.remove(data_d.iloc[j, 0])


f, ax = plt.subplots(1)
ax.tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax.tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minor_locator2)
ax.yaxis.set_minor_locator(minor_locator)
plt.plot(volt, dqdv)
plt.xlabel("Voltage (V)")
plt.ylabel("dQ/dV")
plt.xticks(np.arange(5.7, 6.6, 0.2))
plt.yticks(np.arange(-500, 500, 50))
plt.xlim(5.7, 6.6)
plt.ylim(-500, 500)
plt.show()