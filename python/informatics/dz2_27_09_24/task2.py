num = int(input())
answer = []
i = 1
while(i <= num):
    if(num % i == 0):
        num = num / i
        answer.append(i)
        i = 2
    else:
        i +=1
print(*answer)