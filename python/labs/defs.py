

def mnog(num):
    i = 0
    res = 1
    while(i < len(num)):
        res *= int(num[i])
        i +=1
    return res

num = input()
print(mnog(num))