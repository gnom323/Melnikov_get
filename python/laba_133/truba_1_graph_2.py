import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 16                   # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
plt.ylabel("Q, м^3/c")
plt.xlabel("delta_P, Па")

def func(x, k, b):
    return x * k + b

# zavisimost Q ot delta_P
k_1 = 0.2
delta_P_1_2 = [109,129,148,169,191,221,273]
Q_1_2 = [6.764,7.230,7.712,8.189,8.714,9.362,10.494]

for i in range(7):
    Q_1_2[i] /= (60 * 1000)
    delta_P_1_2[i] = 9.8067 * delta_P_1_2[i] * 0.4 * 0.80485
print(delta_P_1_2)
print(Q_1_2)

popt, pcov = curve_fit(func, delta_P_1_2, Q_1_2, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(delta_P_1_2[0], delta_P_1_2[-1], 1000)
plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {k}")

plt.plot(delta_P_1_2, Q_1_2,'--o', label='турб')

plt.xlim(0, 900) 
plt.ylim(0, 0.000185)    

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