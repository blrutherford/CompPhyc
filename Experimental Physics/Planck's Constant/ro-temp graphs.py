import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
plt.style.use('classic')
mpl.rc("figure", facecolor='white')
from matplotlib.ticker import AutoMinorLocator
trial1_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.8 Trial 1", skiprows=range(0,1))
trial1_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.8 Trial 1", skiprows=range(0,1))
trial2_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.8 Trial 2", skiprows=range(0,1))
trial2_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.8 Trial 2", skiprows=range(0,1))
#trial3_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx","0.5 Trial 3", skiprows=range(0,1))
#trial3_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 3", skiprows=range(0,1))
#trial4_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx","0.5 Trial 4", skiprows=range(0,1))
#trial4_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 4", skiprows=range(0,1))
#trial5_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx","0.5 Trial 5", skiprows=range(0,1))
#trial5_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 5", skiprows=range(0,1))
temp1 = trial1_rtp.iloc[:, 3]
temp2 = trial2_rtp.iloc[:, 3]
#temp3 = trial3_rtp.iloc[:, 3]
#temp4 = trial4_rtp.iloc[:, 3]
#temp5 = trial5_rtp.iloc[:, 3]

resistivity1 = trial1_rtp.iloc[:, 2]
resistivity2 = trial2_rtp.iloc[:, 2]
#resistivity3 = trial3_rtp.iloc[:, 2]
#resistivity4 = trial4_rtp.iloc[:, 2]
#resistivity5 = trial5_rtp.iloc[:, 2]
resist1 = np.zeros(len(resistivity1))
resist2 = np.zeros(len(resistivity2))
#resist3 = np.zeros(len(resistivity3))
#resist4 = np.zeros(len(resistivity4))
#resist5 = np.zeros(len(resistivity5))

for i in range(len(resistivity1)):
    resist1[i] += resistivity1[i] / 1e+19
    
for i in range(len(resistivity2)):
    resist2[i] += resistivity2[i] / 1e+19
   
#for i in range(len(resistivity3)):
  #  resist3[i] += resistivity3[i] / 1e+19
    
#for i in range(len(resistivity4)):
 #   resist4[i] += resistivity4[i] / 1e+19
   
#for i in range(len(resistivity5)):
 #   resist5[i] += resistivity5[i] / 1e+19


f, ax = plt.subplots(2, 1, figsize=(8, 8))
ax[0].tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax[0].tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax[0].xaxis.set_minor_locator(minor_locator2)
ax[0].yaxis.set_minor_locator(minor_locator)

ax[1].tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax[1].tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax[1].xaxis.set_minor_locator(minor_locator2)
ax[1].yaxis.set_minor_locator(minor_locator)

ax[0].tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax[0].tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax[0].xaxis.set_minor_locator(minor_locator2)
ax[0].yaxis.set_minor_locator(minor_locator)

ax[1].tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax[1].tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax[1].xaxis.set_minor_locator(minor_locator2)
ax[1].yaxis.set_minor_locator(minor_locator)

p1 = np.poly1d(np.polyfit(resist1, temp1, deg=9))
err1 = np.polyval(p1, resist1)
ax[0].plot(np.unique(resist1), np.poly1d(np.polyfit(resist1, temp1,6))(np.unique(resist1)), color='k')
p2 = np.poly1d(np.polyfit(resist2, temp2, deg=9))
err2 = np.polyval(p2, resist2)
ax[1].plot(np.unique(resist2), np.poly1d(np.polyfit(resist2, temp2,6))(np.unique(resist2)), color='r')
'''
p3 = np.poly1d(np.polyfit(resist3, temp3, deg=9))
err3 = np.polyval(p3, resist3)
axs[1, 0].plot(np.unique(resist3), np.poly1d(np.polyfit(resist3, temp3,6))(np.unique(resist3)), color='b')
p4 = np.poly1d(np.polyfit(resist4, temp4, deg=9))
err4 = np.polyval(p4, resist4)
axs[1, 1].plot(np.unique(resist4), np.poly1d(np.polyfit(resist4, temp4,6))(np.unique(resist4)), color='g')
'''

ax[0].scatter(resist1, temp1, color ='k', label="Trial 1")
ax[1].scatter(resist2, temp2, color='r', label="Trial 2")
#axs[1, 0].scatter(resist3, temp3, color='b', label="Trial 3")
#axs[1, 1].scatter(resist4, temp4, color='g', label="Trial 4")


ax[0].legend(loc="lower right")
ax[1].legend(loc="lower right")
#axs[1, 0].legend(loc="lower right")
#axs[1, 1].legend(loc="lower right")
ax[0].set_xlabel("Resistivity (Ohm*m)")
ax[0].set_ylabel("Temperature (K)")
ax[1].set_xlabel("Resistivity (Ohm*m)")
ax[1].set_ylabel("Temperature (K)")
#axs[1, 0].set_xlabel("Resistivity (Ohm*m)")
#axs[1, 0].set_ylabel("Temperature (K)")
#axs[1, 1].set_xlabel("Resistivity (Ohm*m)")
#axs[1, 1].set_ylabel("Temperature (K)")
plt.show()

'''
f, ax = plt.subplots(1)
ax.tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax.tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minor_locator2)
ax.yaxis.set_minor_locator(minor_locator)
p5 = np.poly1d(np.polyfit(resist5, temp5, deg=9))
err5 = np.polyval(p5, resist5)
plt.plot(np.unique(resist5), np.poly1d(np.polyfit(resist5, temp5,6))(np.unique(resist5)), color='m')
plt.scatter(resist5, temp5, color='m', label="Trial 5")
plt.legend(loc="lower right")
plt.xlabel("Resistivity (Ohm*m)")
plt.ylabel("Temperature (K)")
plt.show()
'''