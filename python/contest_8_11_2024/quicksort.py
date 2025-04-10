def bistro(dots, mid):
    if len(dots) <= 1:
        return dots
    pivot = dots[0] # стержень - первый эл-т
    left = [x for x in dots[1:] if x <= pivot and x[0]!= mid] 
    right = [x for x in dots[1:] if x > pivot and x[0]!= mid] 
    print(f" Левое {left}, Правое {right}, Опорный элемент {pivot}")
    return bistro(left, x) + [pivot] + bistro(right, x)

num = int(input())
dots = []
x = 0 # иксовая координата оси симметрии

for i in range(num):
    dots.append(list(map(float, input().split())))
    x += dots[i][0]
x = x/num

print(bistro(dots, x))