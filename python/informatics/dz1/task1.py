nums = input().split()
for i in range(len(nums) - 1): 
    if(i % 2 == 0): nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(nums)
