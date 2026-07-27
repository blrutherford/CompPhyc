import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
plt.style.use('classic')
mpl.rc("figure", facecolor='white')
from matplotlib.ticker import AutoMinorLocator

data_c = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 1\NMH\NiMH Cyclle 2.xlsx", "Charge 3", skiprows=range(0, 7))
data_d = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 1\NMH\NiMH Cyclle 2.xlsx", "Discharge 3", skiprows=range(0, 7))

volts_c = data_c.iloc[:, 0]
time_c = data_c.iloc[:, 2]

voltc = []
timec = []
for i in range(len(volts_c)):
    if volts_c[i] > 0:
        voltc.append(volts_c[i])
for j in range(len(time_c)):
    if time_c[j] >= 0:
        timec.append(time_c[j])

volts_d = data_d.iloc[:, 0]
time_d = data_d.iloc[:, 2]

voltd = []
timed = []
for i in range(len(volts_d)):
    if volts_d[i] > 0:
        voltd.append(volts_d[i])
for j in range(len(time_d)):
    if time_d[j] >= 0:
        timed.append(time_d[j])
#plot
f, ax = plt.subplots(1)
ax.tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax.tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minor_locator2)
ax.yaxis.set_minor_locator(minor_locator)

plt.plot(timec, voltc, color='k')
plt.plot(timed, voltd, color='k')
plt.yticks(np.arange(3, 4.5, 0.2))
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.show()

#calculate capacity in mAh
cap_c = data_c.iloc[:, 5]
cap_d = data_d.iloc[:, 5]

capc = []
for i in range(len(cap_c)):
    if cap_c[i] > 0:
        capc.append(cap_c[i])

capd = []
for j in range(len(cap_d)):
    if cap_d[j] > 0:
        capd.append(cap_d[j])


f, ax = plt.subplots(1)
ax.tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax.tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minor_locator2)
ax.yaxis.set_minor_locator(minor_locator)
plt.plot(capc, voltc, color='k')
plt.plot(capd, voltd, color='k')
plt.xticks(np.arange(0, 700, 100))
plt.yticks(np.arange(3, 4.5, 0.2))
plt.xlabel("Capacity (mAh)")
plt.ylabel("Voltage (V)")
plt.show()

plt.plot(timec, capc)
plt.plot(timed, capd)
plt.show()

mass = 0.03057 #mass NMH
#mass = 0.022962 #mass Li
#mass = 0.27935 #mass SLA

#calculate specific energy capacity in Wh/kg

#cap * voltage
#find max capacity
capc_max = np.max(capc) / 1000
#capd_max = np.max(capd)

vc_max = np.max(voltc)
#vd_max = np.max(voltd)

def energy(vc_max, capc_max):
    en_c = (capc_max * vc_max) /mass
    #en_d = (capd_max * vd_max) / mass
    ##if en_c > en_d:
     #   return en_c
    #elif en_d > en_c:
     #   return en_d
    #else:
    return en_c #en_d


a = vc_max
b = capc_max
print(energy(a, b))   





    
            