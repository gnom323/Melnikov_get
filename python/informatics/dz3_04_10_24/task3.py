import matplotlib.pyplot as plt
import numpy as np

data = list(map(float, input('запишите массы яблок в килограммах (через пробел): ').split()))
data.sort()
plt.title('Массы яблок')
plt.xlabel('Масса отдельного яблока, кг')
plt.ylabel('Кол-во яблок данной массы, шт')

masses = []
for i in range(len(data)):
    if i == 0 or data[i] != data[i-1]:
        masses.append(data[i])
    

numbers = []
for i in range(len(masses)):
    numbers.append(data.count(masses[i]))

plt.bar(masses, numbers, alpha=0.5, width=0.4)
plt.grid(True, which='both', axis='both', linestyle='dashed')
ax = plt.gca() # osi
ax.set_xlim(1, np.max(data))
ax.set_ylim(0, 10)
plt.show()