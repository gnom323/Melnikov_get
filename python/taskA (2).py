n,k = map(int,input().split())
numbers = list(map(int, input().split()))

smallest = numbers[:k]
smallest.sort()
for i in range(k, len(numbers)):
    if numbers[i] < smallest[-1]:
        smallest[-1] = numbers[i]
        print(smallest)
        smallest.sort()
        print(smallest)
print(*smallest)
