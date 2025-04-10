# truba 1
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 16                   # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))

plt.ylabel("y")
plt.xlabel("x")

def func(x, k, b):
    return x * k + b

delta_P_1_1 = [11, 26,39,62,82,103,119]
Q_1_1 = [0.527,1.221,1.810,2.848,3.694,4.565,5.160]

popt1, pcov1 = curve_fit(func, delta_P_1_1, Q_1_1, p0 = (0.0, 0.0))
k1, b1 = popt1
dk1, db1 = np.sqrt(np.diag(pcov1))

x_lin = np.linspace(delta_P_1_1[0], delta_P_1_1[-1], 1000)
plt.plot(x_lin, func(x_lin, k1, b1), "b", label = f"k = {k1}")

delta_P_1_2 = [109,129,148,169,191,221,273]
Q_1_2 = [6.764,7.230,7.712,8.189,8.714,9.362,10.494]

popt2, pcov2 = curve_fit(func, delta_P_1_2, Q_1_2, p0 = (0.0, 0.0))
k2, b2 = popt2
dk2, db2 = np.sqrt(np.diag(pcov2))

x_lin = np.linspace(delta_P_1_2[0], delta_P_1_2[-1], 1000)
plt.plot(x_lin, func(x_lin, k2, b2), "b", label = f"k = {k2}")

for i in range(7):
    Q_1_1[i] = Q_1_1[i] / 60
    Q_1_2[i] /= 60
    delta_P_1_1[i] = 9.8067 * delta_P_1_1[i] * 0.2 * 0.80485
    delta_P_1_2[i] = 9.8067 * delta_P_1_2[i] * 0.4 * 0.80485


for i in range(7):
    Q_1_1.append(Q_1_2[i])
    delta_P_1_1.append(delta_P_1_2[i])



print("k: ({} +- {})".format(k1, dk1))
print("b: ({} +- {})".format(b1, db1))



plt.plot(delta_P_1_1, Q_1_1,'r^')
plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.legend(loc = "best", fontsize = 12) # Активируем легенду графика

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