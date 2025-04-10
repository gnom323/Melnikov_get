import numpy as np
import matplotlib.pyplot as plt
from math import *
from sklearn.linear_model import LinearRegression
import matplotlib as mpl

plt.figure(figsize=(8,6))

phi = np.array([0.012978,0.027122,0.035551,0.065974,0.099618,0.116296])
M = np.array([0.092,0.184,0.276,0.46,0.644,0.736])

plt.ylabel("φ, рад")
plt.xlabel("М, Н*м")

sr_quad_M = 0
sr_quad_phi = 0
for i in range(len(M)):
    sr_quad_M += M[i]**2
    sr_quad_phi += phi[i]**2


reg1 = LinearRegression(fit_intercept = False).fit(M.reshape(6,1),phi)
sigma1 = sqrt(((sr_quad_phi / 6)/(sr_quad_M / 6)- reg1.coef_[0]**2)/(6))
plt.plot(M.reshape(6,1),phi,'--o', label='l = 20 см')
plt.plot(M, reg1.predict(M.reshape(6,1)),'grey',label= f"Аппрокс. прямая k = {reg1.coef_[0]:.4f} $\pm$ {sigma1:.4f} ")


plt.grid(visible = True, which='major', axis='both', alpha=1)
plt.grid(visible = True, which='minor', axis='both', alpha=1)

plt.legend()
plt.show()