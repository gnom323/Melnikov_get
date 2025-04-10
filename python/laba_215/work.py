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

ramka = 0.138
platforma = 0.1498


mass_N = [0, 0.17755,0.34925,0.52585,0.72585,0.57805,0.58205,0.63425,0.45765,0.40545,0.60545,0.45765,0.54925,0.37755,0.45921,0.80846,1.15006,1.55006,2.02776,2.20576,2.00576]

for i in range(len(mass_N)): 
    mass_N[i] += ramka
    mass_N[i] += platforma
    mass_N[i] *= 9.81
# mass_N в Ньютонах 


length_meters = [0.131,0.136,0.141,0.148,0.155,0.15,0.15,0.152,0.146,0.144,0.151,0.153,0.149,0.143,0.146,0.159,0.18,0.204,0.239,0.249,0.238]
# lambda = length/length_0
lamb = []
length_0 = 0.10
lamb_second = [] # здесь будут храниться (лямбда - 1/лямбда^2)
for i in range(len(length_meters)): 
    lamb.append(length_meters[i]/length_0)

    lamb_second.append(lamb[i] - 1/(lamb[i]**2))

delta_V1 = [2.0,2.4,8.4,13.8,18.6,25.2,28.4,41.6]
delta_v2 = [1.8,2.8,9.0,13.2,18.4,26.0,28.8,41.6]

lamb = [0.02,0.03,0.04,0.05,0.06,0.073,0.08,0.1]
l_0 = 0.131

mu = 200 # мВ/градус
for i in range(len(lamb)):
    delta_V1[i] /=mu
    delta_v2[i] /=mu
    delta_V1[i] = (delta_V1[i] + delta_v2[i])/2
    lamb[i] += l_0
    lamb[i] /= l_0
    #print(delta_V1[i], ' ', delta_v2[i], ' ', lamb[i])

    # попытаемся отлогарифмировать

    #delta_V1[i] = math.log(delta_V1[i])
    #lamb[i] = math.log(lamb[i])

# находим работу
E = 1295137.86 # Па
s_0 = 2.98 * 10**(-5) # м^2

A = []
mnoj = E * s_0 / 3

#print(mnoj)
for i in range(len(lamb)):
    
    A.append(mnoj * ((lamb[i]**2)/2 + 1/lamb[i] - 3/2))
    #print((lamb[i]**2)/2 + 1/lamb[i] - 3/2)
    print(round(delta_V1[i],7), ' ', round(lamb[i],6), ' ', round(A[i],6))
    #A[i] = math.log(A[i])


popt, pcov = curve_fit(func, A, delta_V1, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(A[0], A[-1], 1000)

x = 0
y = 0
for i in range(len(lamb)):
    x += A[i]**2
    y += delta_V1[i]**2
x /= len(lamb)
y /= len(lamb)



sr_x_squared = sum(A)/len(A)
sr_x_squared = sr_x_squared**2
sr_y_squared = sum(delta_V1)/len(delta_V1)
sr_y_squared = sr_y_squared**2
print((y - sr_y_squared)/(x - sr_x_squared) - k**2)
sigma_k = math.sqrt(len(A)) * math.sqrt((y - sr_y_squared)/(x - sr_x_squared) - k**2) / len(A)
print(sigma_k)

plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 5)}, σ_k = {round(sigma_k, 5)}  ")
plt.plot(A, delta_V1,'r^')

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

