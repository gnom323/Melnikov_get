eps_d = 100 * 0.05/127.5
x = [4.1,4.2,3.8,3.9,4.1]

eps_x = []
import math
for i in range(5):
    eps_x.append(100 * 0.05/x[i])

m =[0.513,0.508,0.504,0.509,0.51]

eps_m = []

for i in range(5):
    eps_m.append(100 * 0.001/m[i])

eps_r = 100 * 0.05/21
eps_R = 100*0.05/33.5

eps_M = 0.5 * 100 * 0.1 / 730.45

eps_t1 = 0.5 * 100 * 0.02/6.5
eps_t2 = 100 * 0.02/4.7

eps_u = []

for i in range(5):
    eps_u.append(math.sqrt(eps_d**2 + eps_x[i]**2 + eps_t1**2 + eps_m[i]**2 + eps_r**2 + eps_M**2 + eps_R**2 + (2 * eps_t1)**2 + eps_t2**2))

print(eps_u)