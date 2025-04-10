import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 10                  # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
plt.ylabel("")
plt.xlabel("")

def func(x, k, b):
    return x * k + b

# zavisimost Q ot delta_P
k_1 = 0.2
delta_P_1_1 = [11, 26,39,62,82,103,119]
Q_1_1 = [0.527,1.221,1.810,2.848,3.694,4.565,5.160]

for i in range(7):
    Q_1_1[i] /= 60000
    delta_P_1_1[i] = 9.8067 * delta_P_1_1[i] * 0.2 * 0.80485
print(delta_P_1_1)
print(Q_1_1)

popt, pcov = curve_fit(func, delta_P_1_1, Q_1_1, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(delta_P_1_1[0], delta_P_1_1[-1], 1000)
plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 11)}")

#plt.xlim(0, 900) 
#plt.ylim(0, 0.000185)    

plt.plot(delta_P_1_1, Q_1_1,'--^r')
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

#plt.show()

R1 = 3.9/2*10**(-3)
etha1 = 3.14 * R1**4 / (8 * k * 0.5)
print(etha1)


R1 = 3.9/2*10**(-3)
Re = 10**3
mu = 29 * 10**(-3)
ro = 10**5 * mu / (8.31 * 296)

etha = 2.49 * 10**(-5)

q = 96 * 10**(-6)

re = q * 1.18 / (3.14 * etha * R1**2)
print(f"re {re}")
# труба 2 
R2 = 5.25/2*10**(-3)
q_krit_2 = Re * 2 * 10**(-5) * 3.14 * R2 *8.314*296
q_krit_2 = q_krit_2 / (10.1 * 29)
print(q_krit_2)

delta_p = 8 * 2 * 10**(-5) * 0.5* q_krit_2 / (3.14* (5.25/2*10**(-3))**4)
print(delta_p)

n_del = delta_p / (9.8067 * 0.2 * 0.80485)
print(n_del)

del_p = 10 * 0.2 * 9.8067 * 0.80485
print(del_p)

truba_3 = 6.32 / (9.8067 * 0.2 * 0.80485)
print(truba_3)



print(10**3 * 2 * 10**(-5) * 3.14 * 2 * 10**(-3) / 1.61)