import sys
sys.setrecursionlimit(255599)
def calc2(numba, dp, i):
    if dp[len(dp) - 1] != 0:
        return dp[len(dp) - 1]
    else:
        min_2 = -1
        min_3 = -1
        if i % 2 == 0:
            min_2 = int(i / 2)
        if i % 3 == 0:
            min_3 = int(i / 3)
        min_1 = i - 1
        
        #print(f"{min_1},   {min_2},   {min_3}")
        if min_2 != -1:
            if min_3 != -1:
                dp[i-1] = min(dp[min_1 - 1], dp[min_2 - 1], dp[min_3 - 1]) + 1
            else:
                dp[i-1] = min(dp[min_1 - 1], dp[min_2 - 1]) + 1
        elif min_3 != -1:
            dp[i-1] = min(dp[min_3 - 1], dp[min_1 - 1]) + 1
        else: dp[i-1] = dp[min_1 - 1] + 1
        
        #print(dp)
        #print('***')
        i += 1
        return calc2(numba, dp, i)

numba = int(input())
#way = [(i + 1) for i in range(numba)] # посл-ть чисел
dp = [0] * numba # колво ходов
i = 2
#print(calc(numba, way, dp, i))
print(calc2(numba, dp, i))