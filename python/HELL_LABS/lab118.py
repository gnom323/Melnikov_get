from math import *
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib as mpl

t1 = [358,367,357,356,356,356,356]
t2 = [476,486,476,474,475,475,475]
t3 = [565.6,576,565,564,564,564,564]
t4 = [662,652.6,642,640,641,641,640]
t5 = [709.4,720,709,708,708,708,707]
t6 = [769,779,768,767,767,767,767]

tau1 = [119,120.1,119,119,119.3,118.9,119]
tau2 = [208.1,210,208.6,208.5,208.7,208.3,208]
tau3 = [284,286.6,285.4,284.9,285.2,284.8,284]
tau4 = [350.8,353.6,352.6,351.9,352.3,352,351.7]
tau5 = [410.8,413.3,412,411.5,411.8,411.4,411]

# усреднить
t1_2 = []
t2_3 = []
t3_4 = []
t4_5 = []
t5_6 = []

for i in range(len(t1)):
    t1_2.append(t2[i]-t1[i])
    t2_3.append(t3[i]-t1[i])
    t3_4.append(t4[i]-t1[i])
    t4_5.append(t5[i]-t1[i])
    t5_6.append(t6[i]-t1[i])

T1 = 0
T2 = 0
T3 = 0
T4 = 0
T5 = 0
for i in range(len(t1_2)):
    T1 += t1_2[i]
    T1 += tau1[i]
    T2 += t2_3[i]
    T2 += tau2[i]
    T3 += t3_4[i]
    T3 += tau3[i]
    T4 += t4_5[i]
    T4 += tau4[i]
    T5 += t5_6[i]
    T5 += tau5[i]
T1 = T1 / (14)
T2 = T2 / (14)
T3 = T3 / (14)
T4 = T4 / (14)
T5 = T5 / (14)
# получены средние значения тэшек

# погрешность
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
for i in range(7):
    sum1 += (t1_2[i]-T1)**2
    sum2 += (t2_3[i]-T2)**2
    sum3 += (t3_4[i]-T3)**2
    sum4 += (t4_5[i]-T4)**2
    sum5 += (t5_6[i]-T5)**2
    sum1 += (tau1[i]-T1)**2
    sum2 += (tau2[i]-T2)**2
    sum3 += (tau3[i]-T3)**2
    sum4 += (tau4[i]-T4)**2
    sum5 += (tau5[i]-T5)**2
pogr1 = sqrt(sum1/182)
pogr2 = sqrt(sum2/182)
pogr3 = sqrt(sum3/182)
pogr4 = sqrt(sum4/182)
pogr5 = sqrt(sum5/182)
print(pogr1/1000)
print(pogr2/1000)
print(pogr3/1000)
print(pogr4/1000)
print(pogr5/1000)

print(T1/1000, T2/1000, T3/1000, T4/1000, T5/1000)

