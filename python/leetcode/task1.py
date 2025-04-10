import matplotlib as mtp
import numpy as np
from itertools import zip_longest

import copy # copy.copy(копируемый объект) -> создает копию, которая взаимосвязана с изначальным объектом
# copy.deepcopy() -> создает независимую копию

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

d = np.hstack([num1, num2])
b = np.vstack([num1, num2])
determin = np.linalg.det(b)
print(d)
print(b)
print(determin)
# ОПРЕДЕЛИТЕЛЬ МАТРИЦЫ 


points = zip_longest(num1, num2, fillvalue = 'F')
for point in points:
    print(*point)

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 7])
print(np.linalg.solve(A, b))