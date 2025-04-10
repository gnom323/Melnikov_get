import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 10                  # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
#plt.ylabel("")
#plt.xlabel("")

def func(x, k, b):
    return x * k + b

k_1 = 0.2
delta_P_2_xxx = [ 34, 52, 71]
delta = [17, 34, 52, 71]
length = [ 0.405, 0.805, 1.305]
len = [0.105, 0.405, 0.805, 1.305]

delta_1 = 17 * 9.8067 * 0.2 * 0.80485
length_1 = 0.105
for i in range(3):
    delta_P_2_xxx[i] = 9.8067 * delta_P_2_xxx[i] * 0.2 * 0.80485
    delta[i] = 9.8067 * delta[i] * 0.2 * 0.80485
    delta_P_2_xxx[i] -= delta_1
    delta[i] -= delta_1
    len[i] -= length_1
    length[i] -= length_1

popt, pcov = curve_fit(func, length, delta_P_2_xxx, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(length[0], length[-1], 1000)
plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 11)}")

plt.xlim(-0.05, 1.25) 
plt.ylim(-5, 90)    


plt.plot(length, delta_P_2_xxx,'^r')
plt.plot(len, delta, "r^")
plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.legend(fontsize = 12) # Активируем легенду графика

#погрешность мнк
'''x = 0
y = 0
for i in range(11):
    x += t1[i]**2
    y += uhudsh1[i]**2
x /= 11
y /= 11

import math

sr_x_squared = sum(t1)/11
sr_x_squared = sr_x_squared**2
sr_y_squared = sum(uhudsh1)/11
sr_y_squared = sr_y_squared**2

sigma_k = math.sqrt(11) * math.sqrt((y - sr_y_squared)/(x - sr_x_squared) - k**2) / 11
print(sigma_k)'''

plt.show()

R1 = 3.9/2*10**(-3)
etha1 = 3.14 * R1**4 / (8 * k * 0.5)
print(etha1)