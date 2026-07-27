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
#trial3_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.5 Trial 3", skiprows=range(0,1))
#trial3_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 3", skiprows=range(0,1))
#trial4_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.5 Trial 4", skiprows=range(0,1))
#trial4_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 4", skiprows=range(0,1))
#trial5_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.5 Trial 5", skiprows=range(0,1))
#trial5_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 5", skiprows=range(0,1))
temp1 = trial1_rtp.iloc[:, 3]
temp2 = trial2_rtp.iloc[:, 3]
#temp3 = trial3_rtp.iloc[:, 3]
#temp4 = trial4_rtp.iloc[:, 3]
#temp5 = trial5_rtp.iloc[:, 3]

i_phot1 = trial1_viip.iloc[:, 2]
current1 = trial1_viip.iloc[:, 1]
i_phot2 = trial2_viip.iloc[:, 2]
current2 = trial2_viip.iloc[:, 1]
#i_phot3 = trial3_viip.iloc[:, 2]
#current3 = trial3_viip.iloc[:, 1]
#i_phot4 = trial4_viip.iloc[:, 2]
#current4 = trial4_viip.iloc[:, 1]
#i_phot5 = trial5_viip.iloc[:, 2]
#current5 = trial5_viip.iloc[:, 1]


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
'''
axs[1, 0].tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
axs[1, 0].tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
axs[1, 0].xaxis.set_minor_locator(minor_locator2)
axs[1, 0].yaxis.set_minor_locator(minor_locator)

axs[1, 1].tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
axs[1, 1].tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
axs[1, 1].xaxis.set_minor_locator(minor_locator2)
axs[1, 1].yaxis.set_minor_locator(minor_locator)
'''
ax[0].scatter(temp1, i_phot1, color='k', label="Trial 1")
ax[1].scatter(temp2, i_phot2, color='r', label="Trial 2")
#axs[1, 0].scatter(temp3, i_phot3, color='b', label="Trial 3")
#axs[1, 1].scatter(temp4, i_phot4, color='g', label="Trial 4")
ax[0].legend(loc="lower right")
ax[1].legend(loc="lower right")
#axs[1, 0].legend(loc="lower right")
#axs[1, 1].legend(loc="lower right")
ax[0].set_ylabel("Photocurrent (pA)")
ax[0].set_xlabel("Temperature (K)")
ax[1].set_ylabel("Photocurrent (pA)")
ax[1].set_xlabel("Temperature (K)")
#axs[0, 1].set_ylabel("Photocurrent (pA)")
#axs[0, 1].set_xlabel("Temperature (K)")
#axs[1, 1].set_ylabel("Photocurrent (pA)")
#axs[1, 1].set_xlabel("Temperature (K)")
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
plt.scatter(temp5, i_phot5, color='m', label="Trial 5")
plt.legend(loc="lower right")
plt.ylabel("Photocurrent (pA))")
plt.xlabel("Temperature (K)")
plt.show()
'''
i_phot_max1 = np.max(i_phot1)
t_max1  = np.max(temp1)
i_ratio1 = np.zeros(len(i_phot1))
for i in range(len(i_phot1)):
    i_ratio1[i] += i_phot1[i] / i_phot_max1

i_phot_max2 = np.max(i_phot2)
t_max2  = np.max(temp2)
i_ratio2 = np.zeros(len(i_phot2))
for i in range(len(i_phot2)):
    i_ratio2[i] += i_phot2[i] / i_phot_max2
'''
i_phot_max3 = np.max(i_phot3)
t_max3  = np.max(temp3)
i_ratio3 = np.zeros(len(i_phot3))
for i in range(len(i_phot3)):
    i_ratio3[i] += i_phot3[i] / i_phot_max3

i_phot_max4 = np.max(i_phot4)
t_max4  = np.max(temp4)
i_ratio4 = np.zeros(len(i_phot4))
for i in range(len(i_phot4)):
    i_ratio4[i] += i_phot4[i] / i_phot_max4

i_phot_max5 = np.max(i_phot5)
t_max5 = np.max(temp5)
i_ratio5 = np.zeros(len(i_phot5))
for i in range(len(i_phot5)):
    i_ratio5[i] += i_phot5[i] / i_phot_max5
'''
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
'''
axs[1, 0].tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
axs[1, 0].tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
axs[1, 0].xaxis.set_minor_locator(minor_locator2)
axs[1, 0].yaxis.set_minor_locator(minor_locator)

axs[1, 1].tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
axs[1, 1].tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
axs[1, 1].xaxis.set_minor_locator(minor_locator2)
axs[1, 1].yaxis.set_minor_locator(minor_locator)
'''
ax[0].scatter(temp1, i_ratio1, color='k', label="Trial 1")
ax[1].scatter(temp2, i_ratio2, color='r', label="Trial 2")
#axs[1, 0].scatter(temp3, i_ratio3, color='b', label="Trial 3")
#axs[1, 1].scatter(temp4, i_ratio4, color='g', label="Trial 4")
ax[0].legend(loc="lower right")
ax[1].legend(loc="lower right")
#ax[1, 0].legend(loc="lower right")
#axs[1, 1].legend(loc="lower right")
ax[0].set_ylabel("I ratio)")
ax[0].set_xlabel("Temperature (K)")
ax[1].set_ylabel("I ratio")
ax[1].set_xlabel("Temperature (K)")
#axs[0, 1].set_ylabel("I ratio")
#axs[0, 1].set_xlabel("Temperature (K)")
#axs[1, 1].set_ylabel("I ratio")
#axs[1, 1].set_xlabel("Temperature (K)")

plt.show()


f, ax = plt.subplots(1)
ax.tick_params(direction='in', labelbottom=True, labeltop=False, labelleft=True, labelright=False,
                  bottom=True, top=True, left=True, right=True, length=15)
ax.tick_params(length=5, which='minor')
minor_locator = AutoMinorLocator(5)
minor_locator2 = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minor_locator2)
ax.yaxis.set_minor_locator(minor_locator)

plt.scatter(temp5, i_ratio5, color='m', label="Trial 5")
plt.xlabel("Temperature (K)")
plt.ylabel("I ratio")
plt.show()

temp_data = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.8 Trial 2", skiprows=range(0,1))
x = temp_data.iloc[:, 3]

emiss7 =  np.zeros(len(x))
emiss8 = np.zeros(len(x))
emiss5 = np.zeros(len(x))
emiss9 = np.zeros(len(x))
for i in range(len(x)):
    emiss7[i] += (5.92e-10)*x[i]**2 - (2.369e-5)*x[i] + 0.4806

#0.5 micro meters / 5000 angstroms
    emiss5[i] += (-1.75e-5)*x[i] + 0.4968

#0.8 micro meters / 8000 angstroms
    emiss8[i] += (4.167e-9)*x[i]**2 - (4.44e-5)*x[i] + 0.4914

#0.9 micro meters/ 9000 Angstroms
    emiss9[i] += (5.952e-9)*x[i]**2 - (5.155e-5)*x[i] + 0.4804

#print(emiss5)

e_ratio = np.zeros(len(x))
e_max = np.max(emiss8)
for j in range(len(x)):
    e_ratio[j] += emiss8[j] / e_max



k = 1.380649e-23 #J/K
c = 2.99792458e+8 #m/s
lamb = 8e-7 # meters

#solve for h bar
h = np.zeros(len(x))
log = np.zeros(len(x))
t = np.zeros(len(x))

for i in range(len(x)):
    log[i] += m.log(i_ratio[i]/e_ratio[i])
    t[i] += 1/(1/t_max - 1/temp[i])
    h[i] += log[i] * t[i] * (k*lamb)/c

    
h_splice = h[0:-2]
print(h_splice)
avg_h = np.mean(h_splice)
std_h = np.std(h_splice)

