import math

chisl = 4 * 3.1415 * 0.335*0.335 * 6.5 * (0.7307 + 0.7302) /2

znam = 6.5 * 6.5 - 4.7 * 4.7

print(chisl / znam)

kI_ = chisl / znam

x = [0.041,0.042,0.038,0.039,0.041]
d = 1.275

fi = []

for i in range(5):
    fi.append(x[i]/d)

m = [5.13,5.08,5.04,5.09,5.1]

r = 0.21

u = []
for i in range(5):
    u.append(fi[i] * kI_ * 10000 / (m[i] * r))

print(u)

u = [137.58,144.41,138.39,137.04,143.28]
sr_u = sum(u) / len(u)
print(sr_u)

summa = 0
for i in range(5):
    summa += (u[i] - sr_u)**2

sigma = math.sqrt(summa / (5 * 4))
print(sigma)


