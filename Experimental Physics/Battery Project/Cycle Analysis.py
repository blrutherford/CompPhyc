import numpy as np
import matplotlib.pyplot as plt

import scipy.integrate as integrate

c = 54.94 /1000 #mA to A


#integrate the current with respect to charging time
chrg_str = []
chrg_ext = []
chrg_ext1 = integrate.quad(lambda c:c, 89302, 158921)
chrg_ext.append(chrg_ext1)
print(chrg_ext1)

chrg_stored1 = integrate.quad(lambda c:c, 19301, 89301)
chrg_str.append(chrg_stored1)
print(chrg_stored1)

chrg_ext2 = integrate.quad(lambda c:c, 228140, 297043)
chrg_ext.append(chrg_ext2)
print(chrg_ext2)

chrg_stored2 = integrate.quad(lambda c:c, 158922, 228139)
chrg_str.append(chrg_stored2)
print(chrg_stored2)

chrg_ext3 = integrate.quad(lambda c:c, 365744, 434293)
chrg_ext.append(chrg_ext3)
print(chrg_ext3)

chrg_stored3 = integrate.quad(lambda c:c, 297044, 365743)
chrg_str.append(chrg_stored3)
print(chrg_stored3)

str_avg = [sum(vals)/len(chrg_str) for vals in zip(*chrg_str)]
ext_avg = [sum(vals)/len(chrg_ext) for vals in zip(*chrg_ext)]
print(str_avg, ext_avg)
str_std  = np.std([38010700000, 13396700618, 22766402056])
ext_std = np.std([8640518518, 18093342124, 27420868156])
print(str_std, ext_std)
