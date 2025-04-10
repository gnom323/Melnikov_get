import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
import math
mpl.rcParams['font.size'] = 10                  # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
plt.ylabel("")
plt.xlabel("")

def func(x, k, b):
    return x * k + b

# zavisimost Q ot delta_P
k_1 = 0.2

Q = [2.753, 0.888]
R = [5.25/2000, 3.9/2000]
q_1 = [2.753, 0.888, 0.840]
r_1 = [5.25/2000, 3.9/2000, 3/2000]
for i in range(2):
    Q[i] = math.log(Q[i] / 60)
    R[i] = math.log(R[i])

for i in range(3):
    q_1[i] = math.log(q_1[i] / 60)
    r_1[i] = math.log(r_1[i])

print(f"Q = {Q}")
print(f"R = {R}")
popt, pcov = curve_fit(func, R, Q, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(R[0], R[-1], 1000)
plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 11)}")

#plt.xlim(0, 900) 
#plt.ylim(0, 0.000185)    

plt.plot(r_1, q_1,'^r')
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


