people = list(map(int, input().split()))

answer = []

# для каждого чела прогоняем цикл вправо
right = 0
r = 0
temporary = 0

for i in range(len(people)):
    r = i
    temporary = people[i] # временное хранилище значения для чела
    while(r < len(people)):
        if(people[r]>temporary):
            temporary = people[r]
            right += 1
        r+=1
    answer.append(right)
    right = 0
print(*answer)
