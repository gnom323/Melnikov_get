


nums = list(map(int, input().split())) # вводные чиселки
sum_digits_1 = [0 for i in range(len(nums))]
sum_digits = [0 for i in range(len(nums))]
sum_digits_2 = [0 for i in range(len(nums))]
sum_digits_3 = [0 for i in range(len(nums))]
sum_digits_4 = [0 for i in range(len(nums))]

for i in range(len(nums)):
    sum_digits_1[i] = sum(list(map(int, str(nums[i]))))
for i in range(len(nums)):
    sum_digits_2[i] = sum(list(map(int, str(sum_digits_1[i]))))
for i in range(len(nums)):
    sum_digits_3[i] = sum(list(map(int, str(sum_digits_2[i]))))
for i in range(len(nums)):
    sum_digits_4[i] = sum(list(map(int, str(sum_digits_3[i]))))
for i in range(len(nums)):
    sum_digits[i] = sum(list(map(int, str(sum_digits_4[i]))))


n=1
while n<len(sum_digits):
    for i in range(len(sum_digits)-n):
        if sum_digits[i]>sum_digits[i+1]:
            sum_digits[i], sum_digits[i+1] = sum_digits[i+1], sum_digits[i]
            nums[i], nums[i+1] = nums[i+1], nums[i]
        elif(sum_digits[i] == sum_digits[i+1]):
            if(nums[i] > nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]

    n += 1
print(*nums)   
