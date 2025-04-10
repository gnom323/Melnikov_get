mass_g = [75.9, 92.8, 140.8, 268.4, 337.4]
length_m = 0.122
mass_kg = []
M = []
for i in range(len(mass_g)):
    M.append(mass_g[i]* length_m/100)

Big_omega = [(12*3.14)/(180*407),(12*3.14)/(180*332),(12*3.14)/(180*218),(12*3.14)/(180*267),(12*3.14)/(180*303)]

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib as mpl
from math import *

plt.figure(figsize=(10,10))
plt.ylabel("Omega, c^-1")
plt.xlabel("M, H*m")

sr_quad_x1 = 0
sr_quad_y1 = 0

for i in range(5):
  sr_quad_x1 += M[i]**2
  sr_quad_y1 += Big_omega[i]**2

M.sort()
Big_omega.sort()
x1 = np.array(M)
y1 = np.array(Big_omega)


reg1 = LinearRegression(fit_intercept = False).fit(x1.reshape(5,1),y1)
sigma1 = sqrt(((sr_quad_y1 / 5)/(sr_quad_x1 / 5)- reg1.coef_[0]**2)/(5))
plt.plot(x1.reshape(5,1),y1,'--o', label='l = 20 см')
plt.plot(x1, reg1.predict(x1.reshape(5,1)),'grey',label= f"Аппрокс. прямая k = {reg1.coef_[0]:.4f} $\pm$ {sigma1:.4f}")

plt.grid(visible = True, which='major', axis='both', alpha=1)
plt.grid(visible = True, which='minor', axis='both', alpha=1)

plt.legend()
plt.show()