import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,5), dpi=120)

mark = list(map(int, input('кол-во оценок "неуд", "уд", "хор", "отл" (через пробел): ').split()))
labels = ['неуд','уд','хор','отл']
plt.title('Относительное количество оценок')
plt.xlabel(f'всего {np.sum(mark)} студентов')
plt.pie(mark, labels = labels, autopct = '%1.f%%')
plt.show()