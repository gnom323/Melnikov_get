#nums = list(map(int, input().split()))
nums = ['grape','banana','apple','orange']
n=1
while n<len(nums):
    for i in range(len(nums)-n):
        if nums[i]>nums[i+1]:
            print(f'bylo {nums}')
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(f'stalo {nums}')
            print(f'nomer prohoda po massivu {n}')
    n += 1
print(f'itog {nums}')   