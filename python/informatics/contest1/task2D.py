def maxarea(n, k, matrix):
    map_ = [[0]*k for _ in range(n)]
    max_side = 0
    for i in range(n):
        for j in range(k):
            if matrix[i][j] == 1:
                if i > 0 and j > 0:
                    map_[i][j] = min(map_[i-1][j], map_[i][j-1],
                                      map_[i-1][j-1])+1
                else: 
                    map_[i][j] = 1
                max_side = max(max_side, map_[i][j])
    print(map_)
    return max_side
n, k  = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(maxarea(n, k, matrix))