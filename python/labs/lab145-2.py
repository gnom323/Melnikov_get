import numpy as np
import matplotlib.pyplot as plt
from math import *
from sklearn.linear_model import LinearRegression
import matplotlib as mpl

plt.figure(figsize=(8,6))

n = np.array([1,2,3,4,5,6,7,8,9,10])
T = np.array([10.8,4.9,14.8,19.7,24.6])
nu_1= np.array([137.8, 275.2,413.4,551.2,689,826.8,964.5,1102.4,1240.2,1378.1])
nu_2= np.array([92.8,185.6,278.5,371.2,464.1,556.8,649.9,742.4,835.6,928])
nu_3= np.array([161.4,322.8,484,645.6,806.8,968.4,1129.4,1291.2,1452.3,1614])
nu_4= np.array([186.2,372.4,558.6,744.8,931,1117.2,1303.2,1489.6,1675.8,1862])
nu_5= np.array([208,416,624,832.1,1040.2,1248.2,1456.2,1664.2,1872.3,2080.3])
plt.ylabel("u^2, м^2/c^2")
plt.xlabel("T, H")

sr_quad_nu_1 = 0
sr_quad_nu_2 = 0
sr_quad_nu_3 = 0
sr_quad_nu_4 = 0
sr_quad_nu_5 = 0
sr_quad_n = 0

for i in range(len(nu_1)):
    sr_quad_nu_1 += nu_1[i]**2
    sr_quad_nu_2 += nu_2[i]**2
    sr_quad_nu_3 += nu_3[i]**2
    sr_quad_nu_4 += nu_4[i]**2
    sr_quad_nu_5 += nu_5[i]**2
    sr_quad_n += n[i]**2
'''
plt.scatter(nu_1, n, color='black', marker='o')
plt.scatter(nu_2, n, color='black', marker='s')
plt.scatter(nu_3, n, color='black', marker='+')
plt.scatter(nu_4, n, color='black', marker='x')
plt.scatter(nu_5, n, color='black', marker='1')'''

reg1 = LinearRegression(fit_intercept = False).fit(nu_1.reshape(10,1), n)
#sigma1 = sqrt(((sr_quad_n / 10)/(sr_quad_nu_1 / 10)- reg1.coef_[0]**2)/(10))
reg2 = LinearRegression(fit_intercept = False).fit(nu_2.reshape(10,1),n)
sigma2 = sqrt(((sr_quad_n / 10)/(sr_quad_nu_2 / 10)- reg2.coef_[0]**2)/(10))
reg3 = LinearRegression(fit_intercept = False).fit(nu_3.reshape(10,1),n)
sigma3 = sqrt(((sr_quad_n / 10)/(sr_quad_nu_3 / 10)- reg3.coef_[0]**2)/(10))
reg4 = LinearRegression(fit_intercept = False).fit(nu_4.reshape(10,1),n)
sigma4 = sqrt(((sr_quad_n / 10)/(sr_quad_nu_4 / 10)- reg4.coef_[0]**2)/(10))
reg5 = LinearRegression(fit_intercept = False).fit(nu_5.reshape(10,1),n)
sigma5 = sqrt(((sr_quad_n / 10)/(sr_quad_nu_5 / 10)- reg5.coef_[0]**2)/(10))
'''
plt.plot(nu_1.reshape(10,1),n,':o', label="T=10,8 H")
plt.plot(nu_1, reg1.predict(nu_1.reshape(10,1)),'grey',label=f"Аппрокс. прямая k'1 = {reg1.coef_[0]:.5f}")

plt.plot(nu_2.reshape(10,1),n,':s', label="T=4,9 H")
plt.plot(nu_2, reg2.predict(nu_2.reshape(10,1)),'grey',label=f"Аппрокс. прямая k'2 = {reg2.coef_[0]:.5f}")
plt.plot(nu_3.reshape(10,1),n,':+', label="T=14,8 H", markersize=8)
plt.plot(nu_3, reg3.predict(nu_3.reshape(10,1)),'grey',label=f"Аппрокс. прямая k'3 = {reg3.coef_[0]:.5f}")
plt.plot(nu_4.reshape(10,1),n,':^', label="T=19,7 H", markersize=7)
plt.plot(nu_4, reg4.predict(nu_4.reshape(10,1)),'grey',label=f"Аппрокс. прямая k'4 = {reg4.coef_[0]:.5f}")
plt.plot(nu_5.reshape(10,1),n,'v', label="T=24,6 H", markersize=7)
plt.plot(nu_5, reg5.predict(nu_5.reshape(10,1)),'grey',label=f"Аппрокс. прямая k'5 = {reg5.coef_[0]:.5f}")
'''
speeds = np.array([(1/reg1.coef_[0])**2, 1/reg2.coef_[0]**2, 1/reg3.coef_[0]**2,1/reg4.coef_[0]**2,1/reg5.coef_[0]**2])
speeds.sort()
print(1/reg2.coef_[0])
T.sort()
reg6 = LinearRegression(fit_intercept = False).fit(T.reshape(5,1),speeds)
sr_quad_speeds=0
sr_quad_T=0
for i in range(len(speeds)):
    sr_quad_speeds += speeds[0]
    sr_quad_T += T[i]

plt.plot(T.reshape(5,1),speeds,'--o', markersize=8)
plt.plot(T, reg6.predict(T.reshape(5,1)),'grey',label=f"Аппрокс. прямая k'3 = {1/reg6.coef_[0]:.7f}")

#plt.plot(T.reshape(5,1),speeds,'--o', label='l = 20 см')
#plt.plot(T, reg6.predict(T.reshape(5,1)),'grey',label= f"Аппрокс. прямая k = {reg1.coef_[0]:.5f} $\pm$ Ом для l = 20 см")


k_1=np.polyfit(nu_1,n,1)
k_2=np.polyfit(nu_2,n,1)
k_3=np.polyfit(nu_3,n,1)
k_4=np.polyfit(nu_4,n,1)
k_5=np.polyfit(nu_5,n,1)



ax = plt.gca()
ax.set_xlim(0)
ax.set_ylim(0)


plt.grid(visible = True, which='major', axis='both', alpha=1)
plt.grid(visible = True, which='minor', axis='both', alpha=1)
plt.legend()
plt.show()