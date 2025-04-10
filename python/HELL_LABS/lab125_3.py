L = 1.9881 # m^2 * kg/s

Big_omega = [0.00051459,0.0006308,0.0009607,0.0007844,0.0006912]
Big_omega2 = [5.1459,6.308,9.607,7.844,6.912]
M = []
M2 = []
for i in range(5):
    M.append(L * Big_omega[i])
    M2.append(L * Big_omega2[i])

print(M2)

import matplotlib.pyplot as plt
import numpy as np

x = np.array(Big_omega)
y = np.array(M)
plt.plot(x, y)
plt.plot(x,y, '--o', label=f"Коэффициент наклона L = {(y[4]-y[0])/(x[4]-x[0]):.4f}")


plt.grid(visible = True, which='major', axis='both', alpha=1)
plt.grid(visible = True, which='minor', axis='both', alpha=1)

plt.legend()
plt.show()