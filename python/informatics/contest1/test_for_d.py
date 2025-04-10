def zemlemer(Y, X, matrix, dp_field):
    answer = 0
    for axis_y in range(Y):
        for axis_x in range(X):
            if(matrix[axis_y][axis_x] != 0):
                if axis_x > 0 and axis_y > 0:
                    dp_field[axis_y][axis_x] = 1+min(dp_field[axis_y-1][axis_x-1], dp_field[axis_y-1][axis_x], dp_field[axis_y][axis_x-1])
                else: dp_field[axis_y][axis_x] = 1
                answer = max(answer, dp_field[axis_y][axis_x])
    return answer

Y, X = map(int, input().split())
matrix = []
for i in range(Y): matrix.append(list(map(int, input().split())))
dp_field = [[0] * X for _ in range(Y)]
print(zemlemer(Y, X, matrix, dp_field))
