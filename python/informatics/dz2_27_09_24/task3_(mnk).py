import numpy as np
x = np.array(list(map(int, input('значения x = ').split())))
y = np.array(list(map(int, input('значения y = ').split())))
n = len(x)
xy = x * y
xx = x * x
a = (n * xy.sum() - x.sum() * y.sum()) / (n * xx.sum() - (x.sum())**2)
b = (y.sum() - a * x.sum()) / n
print(f"a = {a}")
print(f"b = {b}")