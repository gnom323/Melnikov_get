# f(lambda)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
import math
mpl.rcParams['font.size'] = 16                   # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(8,6))
#plt.ylabel("f, Н")
#plt.xlabel("(λ-1/λ^2)")
#plt.title("f(lambda)")

def func(x, k, b):
    return x * k + b

l_0 = 0.131
T_0 = 295 #K

mV_1_nach = -24.2

# delta_l_1 = 0.04
mV_1 = [-17.4,-18.8,-19.6,-20.8,-21.8,-22.5,-23.2,-23.3]

mV_2_nach = -22.8

# delta_l_2 = 0.1
mV_2 = [16.0,9.2,4.8,1.6,-1.6,-4.4,-6.8,-8.4,]

t = [0,20,40,60,80,100,120,140]

delta_V1 = []
delta_V2 = []
for i in range(len(mV_1)):
    delta_V1.append(mV_1[i] - mV_1_nach)
    delta_V2.append(mV_2[i] - mV_2_nach)

mu = 200 # мВ/градус
for i in range(len(mV_1)):
    delta_V1[i] /=mu
    delta_V2[i] /=mu

    delta_V1[i] = math.log(delta_V1[i]/T_0)
    delta_V2[i] = math.log(delta_V2[i]/T_0)
    #print(delta_V1[i], ' ', delta_v2[i], ' ', lamb[i])

    # попытаемся отлогарифмировать

    #delta_V1[i] = math.log(delta_V1[i])
    #lamb[i] = math.log(lamb[i])

popt, pcov = curve_fit(func, t, delta_V2, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))
lamb = (0.1+0.131)/0.131
A = 0
E = 1295137.86 # Па
s_0 = 2.98 * 10**(-5) # м^2
mnoj = E * s_0 / 3
A = mnoj * ((lamb**2)/2 + 1/lamb - 3/2)

print(f"A = {A}")
x_lin = np.linspace(t[0], t[-1], 1000)

x = 0
y = 0
for i in range(len(delta_V2)):
    x += t[i]**2
    y += delta_V2[i]**2
x /= len(delta_V2)
y /= len(delta_V2)

print(delta_V2)

sr_x_squared = sum(t)/len(t)
sr_x_squared = sr_x_squared**2
sr_y_squared = sum(delta_V2)/len(delta_V2)
sr_y_squared = sr_y_squared**2
print((y - sr_y_squared)/(x - sr_x_squared) - k**2)
sigma_k = math.sqrt(len(t)) * math.sqrt((y - sr_y_squared)/(x - sr_x_squared) - k**2) / len(t)
print(sigma_k)

plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 5)}, σ_k = {round(sigma_k, 5)}  ")
plt.plot(t, delta_V2,'r^')

plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.legend(loc = "best", fontsize = 12) # Активируем легенду графика

plt.show()

'''# for lamb_second
popt, pcov = curve_fit(func, lamb_second, mass_N, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(lamb_second[0], lamb_second[-1], 1000)


#погрешность мнк

x = 0
y = 0
for i in range(len(lamb_second)):
    x += lamb_second[i]**2
    y += mass_N[i]**2
x /= len(lamb_second)
y /= len(lamb_second)



sr_x_squared = sum(lamb_second)/len(lamb_second)
sr_x_squared = sr_x_squared**2
sr_y_squared = sum(mass_N)/len(lamb_second)
sr_y_squared = sr_y_squared**2
print((y - sr_y_squared)/(x - sr_x_squared) - k**2)
sigma_k = math.sqrt(len(lamb_second)) * math.sqrt((y - sr_y_squared)/(x - sr_x_squared) - k**2) / len(lamb_second)
print(sigma_k)

plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 3)}, σ_k = {round(sigma_k, 3)}  ")
plt.plot(lamb_second, mass_N,'r^')

plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.legend(loc = "best", fontsize = 12) # Активируем легенду графика

plt.show()'''

# теперь обсчитать работу от растяжения по интегралу и переделать показания вольтметра в градусы цельсия

