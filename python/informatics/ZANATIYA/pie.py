import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.ticker as ticker
x = [1,2,3,4,5]
y = ['5','4','3','2','1']

colors = plt.cm.viridis(np.linspace(0,1,len(x)))

plt.pie(x, labels=y, colors=colors, autopct = '%1.f%%')
plt.title('Распределение')


#plt.grid(True) # setka
plt.show()

plt.savefig('pie.png')

