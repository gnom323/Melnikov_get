nums = list(map(int, input().split())) # вводные чиселки

nominals = [0 for i in range(len(nums))]
nominals[0] = -1
i = 1
j = 0

while(i < len(nums)):
    j = i - 1
    while(j >= 0):
        if(nums[j] >= nums[i]):
            nominals[i] = j
            break
        if(j == 0):
            nominals[i] = -1
            break
        j-=1
    i+=1
print(*nominals)