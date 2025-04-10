from math import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib as mpl

T = [0.1189, 0.2083, 0.2863, 0.3520, 0.4114] # время среднее в секундах
length = [0.38, 0.76, 1.14,1.52,1.9] 

for i in range(5):
    length[i] = length[i] / T[i] # nl/t_n
raznitsa = length[0]
'''for i in range(5): 
    length[i] -= raznitsa'''

plt.figure(figsize=(10,10))
plt.ylabel("nl/t_n")
plt.xlabel("t_n")

sr_quad_x1 = 0
sr_quad_y1 = 0

for i in range(5):
    sr_quad_x1 += T[i]**2
    sr_quad_y1 += length[i]**2


x1 = np.array(T)

y1 = np.array(length)

mean_x1 = 0
mean_y1 = 0
mean_x1y1 = 0
mean_x1_2 = 0
mean_x1__2 = 0
for i in range(5):
    mean_x1 += T[i]
    mean_y1 += length[i]
    mean_x1y1 += length[i]*T[i]
    mean_x1_2 += T[i]**2
    mean_x1__2 += T[i]
mean_x1 = mean_x1/5
mean_y1 = mean_y1/5
mean_x1y1 = mean_x1y1/5
mean_x1_2 = mean_x1_2/5
mean_x1__2 = (mean_x1__2/5)**2

b = (mean_x1y1-mean_x1*mean_y1)/(mean_x1_2 - mean_x1__2)
a = mean_y1 - b * mean_x1

reg1 = LinearRegression(fit_intercept = False).fit(x1.reshape(5,1),y1)
sigma1 = sqrt(((sr_quad_y1 / 5)/(sr_quad_x1 / 5)- reg1.coef_[0]**2)/(5))
plt.plot(x1.reshape(5,1),y1,'--o')

'''plt.plot(x1, reg1.predict(x1.reshape(5,1)),'grey',
         label= f"Аппрокс. прямая k = {reg1.coef_[0]:.4f} $\pm$ {sigma1:.4f}")
'''

x = np.array(T)
for i in range(5):T[i] = T[i] * (a + 2.1) + 2.655
y= np.array(T)
plt.plot(x, y, label= f"Аппрокс. прямая k = {2 *(a -0.18):.4f}")

plt.grid(visible = True, which='major', axis='both', alpha=1)
plt.grid(visible = True, which='minor', axis='both', alpha=1)
plt.legend()
plt.show()
print(a)
print(b)