import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

plt.figure(figsize=(9,5), dpi=120)

v_0 = int(input('начальная скорость (м/c): '))
a = int(input('ускорение: '))

# время каждые 0.5 секунды
time = np.arange(0, 10.5, 0.5)

x = [] # координаты
for i in range(len(time)):
    x.append(v_0 * time[i] + a * time[i] * time[i] / 2)

ax = plt.gca()
ax.set_xlim(0, np.max(time))
ax.set_ylim(np.min(x) - np.median(x)/2, np.max(x)+ np.median(x)/2)

plt.plot(time, x, color='black', marker='^', markersize=7)
plt.title('зависимость координаты тела от времени')


plt.grid(True, which='both', axis='both', linestyle='dashed')
plt.grid(True)
plt.ylabel('Координата по X, м')
plt.xlabel('Время, с')

plt.show()