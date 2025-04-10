gamma = [1.401, 1.388, 2.12]

sredn = sum(gamma) / len(gamma)

print(sredn)

import math

summa = 0
for i in range(len(gamma)):
    summa += (gamma[i] - sredn)**2

summa = math.sqrt(summa / (len(gamma) * (len(gamma) - 1)))

epsilon = 100 * summa / sredn
print(summa)
print(epsilon)