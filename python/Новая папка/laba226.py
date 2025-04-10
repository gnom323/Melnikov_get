# погрешности диаметров
import math
glass = [2.1,2.05,2.05,2.05,2.1,2.1,2.15,2.05]
steel = [0.8,0.85,1,0.7,0.95,0.75,0.75,0.85]

sr_glass = sum(glass)/8
sr_steel = sum(steel)/8

print(f"sr_glass {sr_glass}")
print(sr_steel)

sigma_glass = 0
sigma_steel = 0
for i in range(8):
    sigma_glass += (glass[i] - sr_glass)**2
    sigma_steel += (steel[i] - sr_steel)**2
sigma_glass = math.sqrt(sigma_glass / 56)
sigma_steel = math.sqrt(sigma_steel / 56)

print(sigma_glass)
print(sigma_steel)

epsilon_glass = (sigma_glass * 100) / sr_glass
epsilon_steel = (sigma_steel * 100) / sr_steel
print(epsilon_glass)
print(epsilon_steel)

t1 = [37.4,38.1]
t2 = [38.5,38.1]
t6 = [39.4,39.1]
t7 = [40.4, 40.4]

t3 = [16.5,16.6]
t4= [16.3,16.3]
t8= [16.3,16.0]
t9= [19.5,19.9]

t5= [7.9,8.2]
t11= [8.1,8.1]
t10= [7.6,7.7]
t14= [11.1,11.5]

t12=[4.6,4.5]
t13=[4.2,4.5]
t15=[6.0,6.1]
t16=[4.3,4.6]

sr_t1 = 0
sr_t2 = 0
sr_t6 = 0
sr_t7 = 0

sr_t3 = 0
sr_t4 = 0
sr_t8 = 0
sr_t9 = 0

sr_t5 = 0
sr_t11 = 0
sr_t10= 0
sr_t14= 0

sr_t12= 0
sr_t13= 0
sr_t15= 0
sr_t16= 0

sigma_t1 = 0
sigma_t2 = 0
sigma_t6 = 0
sigma_t7 = 0

sigma_t3 = 0
sigma_t4 = 0
sigma_t8 = 0
sigma_t9 = 0

sigma_t5 = 0
sigma_t11 = 0
sigma_t10= 0
sigma_t14= 0

sigma_t12= 0
sigma_t13= 0
sigma_t15= 0
sigma_t16= 0

for i in range(2):
    sr_t1 += t1[i]
    sr_t2 += t2[i]
    sr_t6 += t6[i]
    sr_t7 += t7[i]

    sr_t3 += t3[i]
    sr_t4 += t4[i]
    sr_t8 += t8[i]
    sr_t9 += t9[i]

    sr_t5 += t5[i]
    sr_t11 += t11[i]
    sr_t10+= t10[i]
    sr_t14+= t14[i]

    sr_t12+= t12[i]
    sr_t13+= t13[i]
    sr_t15+= t15[i]
    sr_t16+= t16[i]

sr_t1 = sr_t1/2
sr_t2 = sr_t2/2
sr_t6 = sr_t6/2
sr_t7 = sr_t7/2

sr_t3 /=2
sr_t4 /=2
sr_t8 /=2
sr_t9 /=2

sr_t5 /=2
sr_t11 /=2
sr_t10 /=2
sr_t14/=2

sr_t12/=2
sr_t13/=2
sr_t15/=2
sr_t16/=2

for i in range(2):
    sigma_t1 = (t1[i] - sr_t1)**2
    sigma_t2 = (t2[i] - sr_t2)**2
    sigma_t6 = (t6[i] - sr_t6)**2
    sigma_t7 = (t7[i] - sr_t7)**2

    sigma_t3 = (t3[i] - sr_t3)**2
    sigma_t4 = (t4[i] - sr_t4)**2
    sigma_t8 = (t8[i] - sr_t8)**2
    sigma_t9 = (t9[i] - sr_t9)**2

    sigma_t5 = (t5[i] - sr_t5)**2
    sigma_t11 = (t11[i] - sr_t11)**2
    sigma_t10 = (t10[i] - sr_t10)**2
    sigma_t14= (t14[i] - sr_t14)**2

    sigma_t12= (t12[i] - sr_t12)**2
    sigma_t13= (t13[i] - sr_t13)**2
    sigma_t15= (t15[i] - sr_t15)**2
    sigma_t16= (t16[i] - sr_t16)**2

sigma_t1 = math.sqrt(sigma_t1 / 2)
sigma_t2 = math.sqrt(sigma_t2 / 2)
sigma_t6 = math.sqrt(sigma_t6 / 2)
sigma_t7 = math.sqrt(sigma_t7 / 2)

sigma_t3 = math.sqrt(sigma_t3 / 2)
sigma_t4 = math.sqrt(sigma_t4 / 2)
sigma_t8 = math.sqrt(sigma_t8 / 2)
sigma_t9 = math.sqrt(sigma_t9 / 2)

sigma_t5 = math.sqrt(sigma_t5 / 2)
sigma_t11 = math.sqrt(sigma_t11 / 2)
sigma_t10 = math.sqrt(sigma_t10 / 2)
sigma_t14= math.sqrt(sigma_t14 / 2)

sigma_t12= math.sqrt(sigma_t12 / 2)
sigma_t13= math.sqrt(sigma_t13 / 2)
sigma_t15= math.sqrt(sigma_t15 / 2)
sigma_t16= math.sqrt(sigma_t16 / 2)

epsilon_t1 = 100 * sigma_t1 / sr_t1
epsilon_t2 = 100 * sigma_t2 / sr_t2
epsilon_t6 = 100 * sigma_t6 / sr_t6
epsilon_t7 = 100 * sigma_t7 / sr_t7

epsilon_t3 = 100 * sigma_t3 / sr_t3
epsilon_t4 = 100 * sigma_t4 / sr_t4
epsilon_t8 = 100 * sigma_t8 / sr_t8
epsilon_t9 = 100 * sigma_t9 / sr_t9

epsilon_t5 = 100 * sigma_t5 / sr_t5
epsilon_t11 = 100 * sigma_t11 / sr_t11
epsilon_t10 = 100 * sigma_t10 / sr_t10
epsilon_t14 = 100 * sigma_t14 / sr_t14

epsilon_t12 = 100 * sigma_t12 / sr_t12
epsilon_t13 = 100 * sigma_t13 / sr_t13
epsilon_t15 = 100 * sigma_t15 / sr_t15
epsilon_t16 = 100 * sigma_t16 / sr_t16

print(f"sr_t1 {sr_t1}")
print(sr_t2)
print(f"sr_t6 {sr_t6}")
print(sr_t7)

print(f"sigma_t1 {sigma_t1}")
print(sigma_t2)
print(f"sigma_t6 {sigma_t6}")
print(sigma_t7)

print(f"sr_t3 {sr_t3}")
print(sr_t4)
print(f"sr_t8 {sr_t8}")
print(sr_t9)

print(f"sigma_t3 {sigma_t3}")
print(sigma_t4)
print(f"sigma_t8 {sigma_t8}")
print(sigma_t9)

print(f"sr_t5 {sr_t5}")
print(sr_t11)
print(f"sr_t10 {sr_t10}")
print(sr_t14)

print(f"sigma_t5 {sigma_t5}")
print(sigma_t11)
print(f"sigma_t10 {sigma_t10}")
print(sigma_t14)

print(f"sr_t12 {sr_t12}")
print(sr_t13)
print(f"sr_t15 {sr_t15}")
print(sr_t16)

print(f"sigma_t12 {sigma_t12}")
print(sigma_t13)
print(f"sigma_t15 {sigma_t15}")
print(sigma_t16)

# скорости
l = 100 # mm
sigma_l = 2 # mm
epsilon_l = 2 * 100 / 100

v1 = l / sr_t1
v2 = l / sr_t2
v6 = l / sr_t6
v7 = l / sr_t7

v3 = l / sr_t3
v4 = l / sr_t4
v8 = l / sr_t8
v9 = l / sr_t9

v5 = l / sr_t5
v11 = l / sr_t11
v10 = l / sr_t10
v14 = l / sr_t14

v12 = l / sr_t12
v13 = l / sr_t13
v15 = l / sr_t15
v16 = l / sr_t16

v1_sigma = 0.01 * v1 * math.sqrt(epsilon_t1**2 + epsilon_l**2)
v2_sigma = 0.01 * v2 * math.sqrt(epsilon_t2**2 + epsilon_l**2)
v6_sigma = 0.01 * v6 * math.sqrt(epsilon_t6**2 + epsilon_l**2)
v7_sigma = 0.01 * v7 * math.sqrt(epsilon_t7**2 + epsilon_l**2)

v3_sigma = 0.01 * v3 * math.sqrt(epsilon_t3**2 + epsilon_l**2)
v4_sigma = 0.01 * v4 * math.sqrt(epsilon_t4**2 + epsilon_l**2)
v8_sigma = 0.01 * v8 * math.sqrt(epsilon_t8**2 + epsilon_l**2)
v9_sigma = 0.01 * v9 * math.sqrt(epsilon_t9**2 + epsilon_l**2)

v5_sigma = 0.01 * v5 * math.sqrt(epsilon_t5**2 + epsilon_l**2)
v11_sigma = 0.01 * v11 * math.sqrt(epsilon_t11**2 + epsilon_l**2)
v10_sigma = 0.01 * v10 * math.sqrt(epsilon_t10**2 + epsilon_l**2)
v14_sigma = 0.01 * v14 * math.sqrt(epsilon_t14**2 + epsilon_l**2)

v12_sigma = 0.01 * v12 * math.sqrt(epsilon_t12**2 + epsilon_l**2)
v13_sigma = 0.01 * v13 * math.sqrt(epsilon_t13**2 + epsilon_l**2)
v15_sigma = 0.01 * v15 * math.sqrt(epsilon_t15**2 + epsilon_l**2)
v16_sigma = 0.01 * v16 * math.sqrt(epsilon_t16**2 + epsilon_l**2)

'''print("#################")
print(v1)
print(f"v1_sigma {v1_sigma}")
print(v2)
print(f"v2_sigma {v2_sigma}")
print(v6)
print(f"v6_sigma {v6_sigma}")
print(v7)
print(f"v7_sigma {v7_sigma}")
print("#################")
print(v3)
print(f"v3_sigma {v3_sigma}")
print(v4)
print(f"v4_sigma {v4_sigma}")
print(v8)
print(f"v8_sigma {v8_sigma}")
print(v9)
print(f"v9_sigma {v9_sigma}")
print("#################")
print(v5)
print(f"v5_sigma {v5_sigma}")
print(v11)
print(f"v11_sigma {v11_sigma}")
print(v10)
print(f"v10_sigma {v10_sigma}")
print(v14)
print(f"v14_sigma {v14_sigma}")
print("#################")
print(v12)
print(f"v12_sigma {v12_sigma}")
print(v13)
print(f"v13_sigma {v13_sigma}")
print(v15)
print(f"v15_sigma {v15_sigma}")
print(v16)
print(f"v16_sigma {v16_sigma}")'''
print('##################')
print(f"sigma_v1 {v1_sigma}")
print(v2_sigma)
print(f"sigma_v6 {v6_sigma}")
print(v7_sigma)

print(f"sigma_v3 {v3_sigma}")
print(v4_sigma)
print(f"sigma_v8 {v8_sigma}")
print(v9_sigma)

print(f"sigma_v5 {v5_sigma}")
print(v11_sigma)
print(f"sigma_v10 {v10_sigma}")
print(v14_sigma)

print(f"sigma_v12 {v12_sigma}")
print(v13_sigma)
print(f"sigma_v15 {v15_sigma}")
print(v16_sigma)

v3 = l / sr_t3
v4 = l / sr_t4
v8 = l / sr_t8
v9 = l / sr_t9

v5 = l / sr_t5
v11 = l / sr_t11
v10 = l / sr_t10
v14 = l / sr_t14

v12 = l / sr_t12
v13 = l / sr_t13
v15 = l / sr_t15
v16 = l / sr_t16

etha = [] # список со всеми знач вязкости

t_minus1 = [] # список температур
for i in range(4): t_minus1.append(1/(273.15 + 19))
for i in range(4): t_minus1.append(1/(273.15 + 30))
for i in range(4): t_minus1.append(1/(273.15 + 40))
for i in range(4): t_minus1.append(1/(273.15 + 50))


ro_glass = 2.5
ro_steel = 7.8

glass_prom_1 = 9.81 * 2 * (ro_glass - 1.26) / 9
glass_prom_2 = 9.81 * 2 * (ro_glass - 1.25) / 9

steel_prom_1 = 9.81 * 2 * (ro_steel - 1.26) / 9
steel_prom_2 = 9.81 * 2 * (ro_steel - 1.25) / 9

etha.append(glass_prom_1 * ((sr_glass/2)**2)/v1)
etha.append(glass_prom_1 * ((sr_glass/2)**2)/v2)
etha.append(steel_prom_1 * ((sr_steel/2)**2)/v6)
etha.append(steel_prom_1 * ((sr_steel/2)**2)/v7)

etha.append(glass_prom_1 * ((sr_glass/2)**2)/v3)
etha.append(glass_prom_1 * ((sr_glass/2)**2)/v4)
etha.append(steel_prom_1 * ((sr_steel/2)**2)/v8)
etha.append(steel_prom_1 * ((sr_steel/2)**2)/v9)

etha.append(glass_prom_2 * ((sr_glass/2)**2)/v5)
etha.append(glass_prom_2 * ((sr_glass/2)**2)/v11)
etha.append(steel_prom_2 * ((sr_steel/2)**2)/v10)
etha.append(steel_prom_2 * ((sr_steel/2)**2)/v14)

etha.append(glass_prom_2 * ((sr_glass/2)**2)/v12)
etha.append(glass_prom_2 * ((sr_glass/2)**2)/v13)
etha.append(steel_prom_2 * ((sr_steel/2)**2)/v15)
etha.append(steel_prom_2 * ((sr_steel/2)**2)/v16)

for i in range(16): 
    print(f"{i+1} etha[i] {etha[i]}")
    #print(t_minus1[i])
    #etha[i] = math.log(etha[i])
    #print(etha[i])

# погрешность вязкости

epsilon_etha = []
epsilon_etha.append(0.01 * etha[0] * math.sqrt((2 * 100 * v1_sigma/v1) + epsilon_glass**2))
epsilon_etha.append(0.01 * etha[1] * math.sqrt((2 * 100 * v2_sigma/v2) + epsilon_glass**2))
epsilon_etha.append(0.01 * etha[2] * math.sqrt((2 * 100 * v6_sigma/v6) + epsilon_steel**2))
epsilon_etha.append(0.01 * etha[3] * math.sqrt((2 * 100 * v7_sigma/v7) + epsilon_steel**2))

epsilon_etha.append(0.01 * etha[4] * math.sqrt((2 * 100 * v3_sigma/v3) + epsilon_glass**2))
epsilon_etha.append(0.01 * etha[5] * math.sqrt((2 * 100 * v4_sigma/v4) + epsilon_glass**2))
epsilon_etha.append(0.01 * etha[6] * math.sqrt((2 * 100 * v8_sigma/v8) + epsilon_steel**2))
epsilon_etha.append(0.01 * etha[7] * math.sqrt((2 * 100 * v9_sigma/v9) + epsilon_steel**2))

epsilon_etha.append(0.01 * etha[8] * math.sqrt((2 * 100 * v5_sigma/v5) + epsilon_glass**2))
epsilon_etha.append(0.01 * etha[9] * math.sqrt((2 * 100 * v11_sigma/v11) + epsilon_glass**2))
epsilon_etha.append(0.01 * etha[10] * math.sqrt((2 * 100 * v10_sigma/v10) + epsilon_steel**2))
epsilon_etha.append(0.01 * etha[11] * math.sqrt((2 * 100 * v14_sigma/v14) + epsilon_steel**2))

epsilon_etha.append(0.01 * etha[12] * math.sqrt((2 * 100 * v12_sigma/v12) + epsilon_glass**2))
epsilon_etha.append(0.01 * etha[13] * math.sqrt((2 * 100 * v13_sigma/v13) + epsilon_glass**2))
epsilon_etha.append(0.01 * etha[14] * math.sqrt((2 * 100 * v15_sigma/v15) + epsilon_steel**2))
epsilon_etha.append(0.01 * etha[15] * math.sqrt((2 * 100 * v16_sigma/v16) + epsilon_steel**2))

for i in range(16):
    print(f"{i+1} погреш {epsilon_etha[i]}")

# рейнольдс

rey = []
rey.append(v1 * sr_glass * 0.5 * 1.26/etha[0])
rey.append(v2 * sr_glass * 0.5 * 1.26/etha[1])
rey.append(v6 * sr_steel * 0.5 * 1.26/etha[2])
rey.append(v7 * sr_steel * 0.5 * 1.26/etha[3])

rey.append(v3 * sr_glass * 0.5 * 1.26/etha[4])
rey.append(v4 * sr_glass * 0.5 * 1.26/etha[5])
rey.append(v8 * sr_steel * 0.5 * 1.26/etha[6])
rey.append(v9 * sr_steel * 0.5 * 1.26/etha[7])

rey.append(v5 * sr_glass * 0.5 * 1.25/etha[8])
rey.append(v11 * sr_glass * 0.5 * 1.25/etha[9])
rey.append(v10 * sr_steel * 0.5 * 1.25/etha[10])
rey.append(v14 * sr_steel * 0.5 * 1.25/etha[11])

rey.append(v12 * sr_glass * 0.5 * 1.25/etha[12])
rey.append(v13 * sr_glass * 0.5 * 1.25/etha[13])
rey.append(v15 * sr_steel * 0.5 * 1.25/etha[14])
rey.append(v16 * sr_steel * 0.5 * 1.25/etha[15])

for i in range(16): print(f"{i+1} Re {rey[i]}")

tau = []
tau.append(1.26 * 2 * sr_glass**2 /(4 * 9*etha[0]))
tau.append(1.26 * 2 * sr_glass**2 /(4 * 9*etha[1]))
tau.append(1.26 * 2 * sr_steel**2 /(4 * 9*etha[2]))
tau.append(1.26 * 2 * sr_steel**2 /(4 * 9*etha[3]))

tau.append(1.26 * 2 * sr_glass**2 /(4 * 9*etha[4]))
tau.append(1.26 * 2 * sr_glass**2 /(4 * 9*etha[5]))
tau.append(1.26 * 2 * sr_steel**2 /(4 * 9*etha[6]))
tau.append(1.26 * 2 * sr_steel**2 /(4 * 9*etha[7]))

tau.append(1.25 * 2 * sr_glass**2 /(4 * 9*etha[8]))
tau.append(1.25 * 2 * sr_glass**2 /(4 * 9*etha[9]))
tau.append(1.25 * 2 * sr_steel**2 /(4 * 9*etha[10]))
tau.append(1.25 * 2 * sr_steel**2 /(4 * 9*etha[11]))

tau.append(1.25 * 2 * sr_glass**2 /(4 * 9*etha[12]))
tau.append(1.25 * 2 * sr_glass**2 /(4 * 9*etha[13]))
tau.append(1.25 * 2 * sr_steel**2 /(4 * 9*etha[14]))
tau.append(1.25 * 2 * sr_steel**2 /(4 * 9*etha[15]))
print("###########")
for i in range(16): print(f"{i+1} tau {tau[i]}")

s = []

s.append(v1 * tau[0])
s.append(v2 * tau[1])
s.append(v6 * tau[2])
s.append(v7 * tau[3])

s.append(v3 * tau[4])
s.append(v4 * tau[5])
s.append(v8 * tau[6])
s.append(v9 * tau[7])

s.append(v5 * tau[8])
s.append(v11 * tau[9])
s.append(v10 * tau[10])
s.append(v14 * tau[11])

s.append(v12 * tau[12])
s.append(v13 * tau[13])
s.append(v15 * tau[14])
s.append(v16 * tau[15])

for i in range(16): print(f"{i+1} s {s[i]}")


'''import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.optimize import curve_fit
mpl.rcParams['font.size'] = 16                   # Управление стилем, в данном случаем - размером шрифта
plt.figure(figsize=(10,10))
#plt.ylabel("P, 10^-4 торр")
#plt.xlabel("t, с")
#plt.title("График зависимости ln( ) от 1/T")

def func(x, k, b):
    return x * k + b

#uhudsh1 = [0.82,0.96,1.5,2.1,2.7,3.3,3.9,4.5,5.0,5.5,6.1]
#t1 = [0,5,10,15,20,25,30,35,40,45,50]

popt, pcov = curve_fit(func, t_minus1, etha, p0 = (0.0, 0.0))
k, b = popt
dk, db = np.sqrt(np.diag(pcov))

print("k: ({} +- {})".format(k, dk))
print("b: ({} +- {})".format(b, db))

x_lin = np.linspace(t_minus1[0], t_minus1[-1], 1000)

#погрешность мнк
x = 0
y = 0
for i in range(16):
    x += t_minus1[i]**2
    y += etha[i]**2
x /= 16
y /= 16

sr_x_squared = sum(t_minus1)/16
sr_x_squared = sr_x_squared**2
sr_y_squared = sum(etha)/16
sr_y_squared = sr_y_squared**2

sigma_k = 0.25 * math.sqrt((y - sr_y_squared)/(x - sr_x_squared) - k**2)

plt.plot(x_lin, func(x_lin, k, b), "b", label = f"k = {round(k, 2)}   {round(sigma_k, 2)} K")

plt.plot(t_minus1, etha,'r^')
plt.grid(visible = True, which = 'major', axis = 'both', alpha = 1, linewidth = 0.9)   # Активируем сетку
plt.grid(visible = True, which = 'minor', axis = 'both', alpha = 0.5, linestyle = ':')

plt.minorticks_on()
plt.tight_layout()
plt.legend(loc = "best", fontsize = 12) # Активируем легенду графика


plt.show()'''