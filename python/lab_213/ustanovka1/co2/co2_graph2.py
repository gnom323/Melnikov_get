import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 10                  # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
plt.title("№2")
plt.ylabel("L, м")
plt.xlabel("n, номер резонанса")

def func(x, k, b):
    return x * k + b

n = [1, 2, 3, 4]
f = 939
L = [0.741, 0.794, 0.847, 0.901]




popt, pcov = curve_fit(func, n, L, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(n[0], n[-1], 1000)
plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 5)}, sigma_k = {round(dk, 6)}")

#plt.xlim(0, 900) 
#plt.ylim(0, 0.000185)    

plt.plot(n, L,'--^r')
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
