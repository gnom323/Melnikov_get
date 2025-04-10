a = [1, 2, 3, 4, 5]
for i in range(len(a) - 1): if(i % 2 == 0): a[i], a[i+1] = a[i+1], a[i] 
print(a)