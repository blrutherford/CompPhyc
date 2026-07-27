import numpy as np
import matplotlib.pyplot as plt

temp = [1600, 1800, 2000, 2200, 2400, 2600, 2800]

wavelength = [0.481, 0.477, 0.474, 0.471, 0.468, 0.464, 0.461]
p = np.poly1d(np.polyfit(temp, wavelength, deg=1))
print(p)
err = np.polyval(p, temp)

coeff = np.polyfit(temp, wavelength, 2)
y1 = np.poly1d(coeff)
plt.plot(temp, y1(temp))

plt.scatter(temp, wavelength)
plt.xlabel("Temperature (K)")
plt.ylabel("Wavelength (micrometer)")
plt.show()

result = (a-b for a, b in zip(wavelength, err))

plt.plot(result, 'o')
plt.axhline(y=0, linestyle='-')
plt.ylim(-0.01, 0.01)
plt.show()