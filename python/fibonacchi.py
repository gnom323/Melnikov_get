num = int(input())
a = 0
b = 1
for i in range(num):
    if(i%2 == 0):
        print(a, end=' ')
        a += b
    else:
        print(b, end=' ')
        b += a