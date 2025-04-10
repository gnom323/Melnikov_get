# truba 1
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 10                  # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,8))

plt.ylabel("Q, м^3/c")
plt.xlabel("delta P, Па")

def func(x, k, b):
    return x * k + b

delta_P_1_1 = [11, 26,39,62,82,103,119]
Q_1_1 = [0.527,1.221,1.810,2.848,3.694,4.565,5.160]

delta_P_1_2 = [109,129,148,169,191,221,273]
Q_1_2 = [6.764,7.230,7.712,8.189,8.714,9.362,10.494]

for i in range(7):
    Q_1_1[i] = Q_1_1[i] / (60 * 1000)
    Q_1_2[i] /= 60000
    delta_P_1_1[i] = 9.8067 * delta_P_1_1[i] * 0.2 * 0.80485
    delta_P_1_2[i] = 9.8067 * delta_P_1_2[i] * 0.4 * 0.80485


for i in range(7):
    Q_1_1.append(Q_1_2[i])
    delta_P_1_1.append(delta_P_1_2[i])

plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.plot(delta_P_1_1, Q_1_1, 'ro')

plt.show()