import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.ticker as ticker
x = [1,2,3,4,5]
y = [5,4,3,2,1]
#x = list(map(int, input().split()))
#y = list(map(int, input().split()))

# линия
plt.plot(x, y, color='black', marker='^', markersize=7)
#plt.plot(x, y)

# точки -> plt.scatter(аргументы)

# CHECK LEGEND

plt.ylabel('ось у')
plt.xlabel('ось х')
plt.title('первый график')
ax = plt.gca() # osi
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
# ax.set_x y ticks() -> значения черточек

# маленькие насечки на осях -> по 0,5 значения
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5)) 

# обозначения для маленьких насечек
ax.xaxis.set_minor_formatter(ticker.FormatStrFormatter('%g'))
ax.yaxis.set_minor_formatter(ticker.FormatStrFormatter('%g'))



plt.grid(True, which='both', axis='both', linestyle='dashed')
#plt.grid(True) # setka
plt.show()

