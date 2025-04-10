import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.ticker as ticker
x = np.linspace(0, 10, 100)
y = np.sin(x)*5 + 5

plt.scatter(x, y, c=y, cmap='BuPu_r')


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

