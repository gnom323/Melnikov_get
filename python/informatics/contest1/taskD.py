def zemlemer(n, k, matrix, answer):
    dlina = 0
    for i in range(n):
        for j in range(k):
            if(matrix[i][j] == 1):
                if(i > 0 and j > 0):
                    answer[i][j] = min(answer[i-1][j], answer[i][j-1], 
                                       answer[i-1][j-1])+1
                else:
                    answer[i][j] = 1
                dlina = max(dlina, answer[i][j])
    return dlina
    
n, k = map(int, input().split())
matrix = []
answer = [[0] * k for _ in range(n)]
for i in range(n):
    matrix.append(list(map(int, input().split())))
print(zemlemer(n, k, matrix, answer))