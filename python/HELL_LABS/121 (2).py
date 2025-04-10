m = [0.509,0.506,0.506,0.511,0.51,0.513,0.508,0.504,0.509,0.51]

eps_m = []

for i in range(10):
    eps_m.append(100 * 0.001 / m[i])
print(eps_m)

eps_M = 0.17
eps_L = 0.01

eps_u = []

del_x = [11.5,12,11.5,11.5,12]

eps_x = []
import math

for i in range(5):
    eps_x.append(100 * 0.125 / del_x[i])
    eps_u.append(math.sqrt(eps_M**2 + eps_m[i]**2 + eps_x[i]**2 + eps_L**2))

print(eps_u)