def mirror(dots, num, x):
    if len(dots) == 1: return 1
    mid = len(dots)//2
    left = dots[:mid]
    right = dots[mid:]
    '''
    for i in range(num):
        if(dots[i][0] > x):
            right.append(dots[i])
        elif(dots[i][0] < x):
            left.append(dots[i])'''
    # массив точек разделен на две части
    #print(left)
    #print(right)
    if(len(left) != len(right)):
        return 0
    else:
        for i in range(len(left)): # каждому члену находим пару
            j = 0
            while(j< len(left)):
                if(left[i][1] == right[j][1] and abs(left[i][0]-x) == abs(right[j][0]-x)):
                    break
                elif(j == len(left) - 1): return 0
                j += 1
    return 1

def bistro(dots, mid):
    if len(dots) <= 1:
        return dots
    pivot = dots[0] # стержень - первый эл-т
    left = [x for x in dots[1:] if x <= pivot and x[0]!= mid] 
    right = [x for x in dots[1:] if x > pivot and x[0]!= mid] 
    return bistro(left, x) + [pivot] + bistro(right, x)

num = int(input())
dots = []
x = 0 # иксовая координата оси симметрии

for i in range(num):
    dots.append(list(map(float, input().split())))
    x += dots[i][0]
x = x/num
# получен список dots, надо сортировать
dots = bistro(dots, x) # отсортирован, точки на оси симметрии удалены

print(mirror(dots, len(dots), x))