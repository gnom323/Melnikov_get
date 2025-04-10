nums = list(map(int, input().split()))
for i in range(len(nums)):
    for k in range(len(nums)):
        if nums[i] == nums[k] and i != k:
            break
    else: print(nums[i], end=' ')
        