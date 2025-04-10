

def horse(matrix, vysota, mschirina):
    for i in range(vysota):
        for j in range(schirina):
            if(i + 2 < vysota and j + 1 < schirina):
                matrix[i+2][j+1] += matrix[i][j]
            if(i+1< vysota and j+2 < schirina):
                matrix[i+1][j+2] += matrix[i][j]
    return int(matrix[vysota-1][schirina-1])

vysota, schirina = list(map(int, input().split()))

matrix = [0 for i in range(vysota)]
for i in range(vysota):
    matrix[i] = [0] * schirina
matrix[0][0] = 1
print(matrix)

print(horse(matrix, vysota, schirina))
