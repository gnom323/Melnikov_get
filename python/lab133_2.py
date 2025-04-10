import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 10                  # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
plt.ylabel("y")
plt.xlabel("x")



#22 значения

delta_P_2_1 = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,145,150,155,160,165,170,175,180]
Q_2_1 = [1.387,2.719,4.204,5.559,6.902,8.079,8.435,8.743,8.981,9.183,9.454,9.842,10.216,10.571,15.493,15.790,16.057,16.296,16.581,16.810,17.115,17.332]

for i in range(22):
    Q_2_1[i] = Q_2_1[i] / 60000
    delta_P_2_1[i] = 9.8067 * delta_P_2_1[i] * 0.2 * 0.80485

plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()

plt.plot(delta_P_2_1, Q_2_1,'r^')
plt.show()