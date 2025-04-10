import numpy as np
from math import *

_2k_med = 4.18
k2 = np.array([4.6,4.2,4.1,4.1,4.1,4])
_3k_med = 5.48
k3 = np.array([5.4,5.5,5.4,5.5,5.6,5.5])
_5k_med = 10.18
k5 = np.array([10.2,10,10.1,10.3,10.2,10.3])
_7k_med = 15.4
k7 = np.array([15.5,15.1,15.5,15.5,15.5,15.3])
_8k_med = 18.3
k8 = np.array([18.9,18,18])

sum2=0
sum3=0
sum5=0
sum7=0
sum8=0
for i in range(6):
    sum2 += (k2[i]-_2k_med)**2
    sum3 += (k3[i]-_3k_med)**2
    sum5 += (k5[i]-_5k_med)**2
    sum7 += (k7[i]-_7k_med)**2

for i in range(3):
    sum8 += (k8[i]-_8k_med)**2


print(sqrt(sum2/30))
print(sqrt(sum3/30))
print(sqrt(sum5/30))
print(sqrt(sum7/30))

print(sqrt(sum8/6))

plt.figure(figsize=(10,10))
plt.ylabel("nl/t_n")
plt.xlabel("t_n")