import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 16                   # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
plt.ylabel("P, 10^-4 торр")
plt.xlabel("t, с")
plt.title("ухудшение вакуума 1")

def func(x, k, b):
    return x * k + b
uhudsh1 = [0.82,0.96,1.5,2.1,2.7,3.3,3.9,4.5,5.0,5.5,6.1]
t1 = [0,5,10,15,20,25,30,35,40,45,50]

popt, pcov = curve_fit(func, t1, uhudsh1, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(t1[0], t1[-1], 1000)
plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {k}")

plt.plot(t1, uhudsh1,'r^')
plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.legend(loc = "best", fontsize = 12) # Активируем легенду графика

plt.show()