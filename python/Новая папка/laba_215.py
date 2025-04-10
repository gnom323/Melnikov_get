# f(lambda)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
import math
mpl.rcParams['font.size'] = 16                   # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(8,6))
plt.ylabel("f, Н")
plt.xlabel("λ")
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
E = 1295137.86 # Па
s_0 = 2.98 * 10**(-5) # м^2

C_l_1 = 37.51
C_l_1_1 = 44.69
C_l_1_2 = 42.84

l_1 = 1.763
l_1_1 = 1.305
l_1_2 = 1.763

t_1 = 0.208
t_1_1 = 0.034
t_1_2 = 0.187

alp_1 = ((t_1 * 6 * C_l_1 / (E * s_0 * 0.1 * (l_1 - 1)) - l_1 - 1) * (-l_1 / 2) - 1) / (3 * 295)
alp_2 = ((t_1_1 * 6 * C_l_1_1 / (E * s_0 * 0.1 * (l_1_1 - 1)) - l_1_1 - 1) * (-l_1_1 / 2) - 1) / (3 * 295)
alp_3 = ((t_1_2 * 6 * C_l_1_2 / (E * s_0 * 0.1 * (l_1_2 - 1)) - l_1_2 - 1) * (-l_1_2 / 2) - 1) / (3 * 295)

print(alp_1)

print(alp_2)

print(alp_3)
alp = (alp_1 + alp_2 + alp_3) / 3
print(alp)

epsilon = 100 / alp * math.sqrt(((alp_1 - alp)**2 + (alp_2-alp)**2 + (alp_3 - alp)**2)/6)
print(epsilon)
print(math.sqrt(13.19**2 + 13.34**2 + 0 + 0 + 3.26**2 + epsilon**2))

c1 = 13044.83
c2 = 15544.35
c3 = 14900.78

c_sredn = (c1 + c2 + c3)/3
epsilon_c = 100 / c_sredn * math.sqrt(((c1 - c_sredn)**2 + (c2-c_sredn)**2 + (c3 - c_sredn)**2)/6)
print(c_sredn)
print(math.sqrt(13.99**2 + 13.19**2 + 3.26**2 + epsilon_c**2))





length_meters = [0.131,0.136,0.141,0.148,0.155,0.15,0.15,0.152,0.146,0.144,0.151,0.153,0.149,0.143,0.146,0.159,0.18,0.204,0.239,0.249,0.238]
# lambda = length/length_0
lamb = []
length_0 = 0.10
lamb_second = [] # здесь будут храниться (лямбда - 1/лямбда^2)
for i in range(len(length_meters)): 
    lamb.append(length_meters[i]/length_0 - 1)

    lamb_second.append(lamb[i] - 1/(lamb[i]**2))

# for lamb
popt, pcov = curve_fit(func, lamb, mass_N, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(lamb[0], lamb[-1], 1000)

'''# for lamb_second
popt, pcov = curve_fit(func, lamb_second, mass_N, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(lamb_second[0], lamb_second[-1], 1000)'''


#погрешность мнк - доделать
print(len(lamb))
x = 0
y = 0
for i in range(len(lamb)):
    x += lamb[i]**2
    y += mass_N[i]**2
x /= len(lamb)
y /= len(lamb)



sr_x_squared = sum(lamb)/len(lamb)
sr_x_squared = sr_x_squared**2
sr_y_squared = sum(mass_N)/len(lamb)
sr_y_squared = sr_y_squared**2
print((y - sr_y_squared)/(x - sr_x_squared) - k**2)
sigma_k = math.sqrt(len(lamb)) * math.sqrt((y - sr_y_squared)/(x - sr_x_squared) - k**2) / len(lamb)
print(sigma_k)
'''x = 0
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
print(sigma_k)'''

plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 3)}, σ_k = {round(sigma_k, 3)}  ")
plt.plot(lamb, mass_N,'r^') 

# plt.plot(lamb_second, mass_N,'r^')

plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.legend(loc = "best", fontsize = 12) # Активируем легенду графика

plt.show()