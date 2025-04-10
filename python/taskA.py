'''first = list(map(int, input().split()))
mass = list(map(int, input().split()))
mass.sort()

print(*mass[:first[1]]) # выход за 4 с'''

# идея: сортировка только первых к эл-тов
# quicksort с pivot примерно посередине
# и сортируем необходимые эл-ты
# check QUICKSELECT -> затем сортануть (или вместо этого через кучу heap)

def partition(arr, l, r): pass

# 0_0 working

'''def sml():
    n,k = map(int,input().split())
    num = list(map(int, input().split()))

    def quick(a,b):
        while(len(a)>b):
            pivot = a[len(a)-1]
            a = [x for x in a if x<pivot]
            print(a)
        return a
    result = quick(num, k)
    print(" ".join(map(str, sorted(result)[:k])))

sml()'''


n,k = map(int,input().split())
nums = list(map(int, input().split()))
i = 5
while(len(nums) > k and i != 0):
     pivot = nums[0]*2
     nums = [x for x in nums if x < pivot]
     nums.append(pivot)
     print(nums)
     i -= 1

print(*sorted(nums)[:k])
# kucha

import heapq
import math
def sml_heap():
    n,k = map(int,input().split())
    num = list(map(int, input().split()))
    nums = heapq.nsmallest(k, num)
    print(" ".join(map(str, nums)))