import numpy as np
import pandas as pd

trial1_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.5 Trial 1", skiprows=range(0,1))
trial1_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 1", skiprows=range(0,1))
trial2_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.5 Trial 2", skiprows=range(0,1))
trial2_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 2", skiprows=range(0,1))
trial3_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.5 Trial 3", skiprows=range(0,1))
trial3_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 3", skiprows=range(0,1))
trial4_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.5 Trial 4", skiprows=range(0,1))
trial4_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 4", skiprows=range(0,1))
trial5_viip = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-VIIp.xlsx", "0.5 Trial 5", skiprows=range(0,1))
trial5_rtp = pd.read_excel(r"C:\Users\baile\Downloads\Lab\Project 2\Plank's Constant Raw Data-RT_ro.xlsx", "0.5 Trial 5", skiprows=range(0,1))

resistivity1 = trial1_rtp.iloc[:, 2]
resistivity2 = trial2_rtp.iloc[:, 2]
resistivity3 = trial3_rtp.iloc[:, 2]
resistivity4 = trial4_rtp.iloc[:, 2]
resistivity5 = trial5_rtp.iloc[:, 2]


resist1 = trial1_viip.iloc[:, 3] / trial1_viip.iloc[:, 1]
resist2 = trial2_viip.iloc[:, 3] / trial2_viip.iloc[:, 1]
resist3 = trial3_viip.iloc[:, 3] / trial3_viip.iloc[:, 1]
resist4 = trial4_viip.iloc[:, 3] / trial4_viip.iloc[:, 1]
resist5 = trial5_viip.iloc[:, 3] / trial5_viip.iloc[:, 1]


p =np.mean(resistivity1 + resistivity2 + resistivity3 + resistivity4 + resistivity5)
r = np.mean(resist1 + resist2 + resist3 + resist4 + resist5)
r_room = 3.74
def unc_resist(r_room, r, p):
    resist= np.sqrt((p*r)/r_room**2 * 0.01)
    return resist

unc_res = unc_resist(r_room, r, p)

x = p / 1e+19

dx = (9*1.511e+66*x**8) - (8*1.375e+60*x**7) + (7*5.224e+53*x**6) - (6*1.078e+47*x**5) + (5*1.313e+40*x**4) - (4*9.63e+32*x**3) + (3*4.148e+25*x**2) - (2*9.784e+17*x) + 1.537e+10

def temp_unc(dx, unc_res):
    temp = np.sqrt((dx*unc_res)**2)
    return (temp + 277.44)/ 1e+14

print(temp_unc(dx, unc_res))