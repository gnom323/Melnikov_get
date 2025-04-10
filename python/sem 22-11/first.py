def mirror(dots):
    if len(dots) <= 1:
        return 1
    else:
        x_coordinates = 0
        for i in range(len(dots)): x_coordinates += dots[i][0]
        #print(x_coordinates)
        x_median = x_coordinates / len(dots)

        dots_set = set(dots) # пары координат
        for i in range(len(dots)):
            mirror_x = x_median * 2 - dots[i][0] # находим иксовую координату зеркальной точки
            if(mirror_x, dots[i][1]) not in dots_set: return 0 # чекаем сет на наличие зеркальной точки
        return 1

num = int(input())
dots = []
for i in range(num):
    dots.append(tuple(map(int, input().split()))) # tuple должен быть быстрее list'а -> получу свои 38 мс

print(mirror(dots))