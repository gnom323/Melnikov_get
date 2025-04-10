import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
import math
mpl.rcParams['font.size'] = 16                   # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
plt.ylabel("ln")
plt.xlabel("t, с")
# plt.title("ухудшение вакуума 1")

def func(x, k, b):
    return x * k + b
uhudsh1 = [0.00064,0.00040,0.00019,0.00013,0.00011,0.00011,0.00011,0.00011] # это улучшение
uluchs_1 = []
t1 = [0,5,10,15,20,25,30,35]

for i in range(8): uhudsh1[i] = math.log(uhudsh1[i])

popt, pcov = curve_fit(func, t1, uhudsh1, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(t1[0], t1[-1], 1000)




#погрешность мнк
x = 0
y = 0
for i in range(8):
    x += t1[i]**2
    y += uhudsh1[i]**2
x /= 11
y /= 11



sr_x_squared = sum(t1)/8
sr_x_squared = sr_x_squared**2
sr_y_squared = sum(uhudsh1)/8
sr_y_squared = sr_y_squared**2
print((y - sr_y_squared)/(x - sr_x_squared) - k**2)
sigma_k = math.sqrt(8) * math.sqrt((-1) * (y - sr_y_squared)/(x - sr_x_squared) - k**2) / 8
print(sigma_k)

plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 4)}   {round(sigma_k,4)}")
plt.plot(t1, uhudsh1,'r^')
plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.legend(loc = "best", fontsize = 12) # Активируем легенду графика

plt.show()