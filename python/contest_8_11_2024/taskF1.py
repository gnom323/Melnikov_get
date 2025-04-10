# тест 11 вышел за 1 с

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

def sliv(dots, x): # функция для сортировки 
    answer = []
    if len(dots) > 1:  # из пункта 1 помним, если в массиве 1 элемент, то он уже отсортирован
        mid = len(dots)//2
        left = dots[:mid] 
        right = dots[mid:]
        left = sliv(left, x)  
        right = sliv(right, x)  

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right) and k <len(left) + len(right): 
            if left[i] < right[j] and left[i][0] != x: 
                answer.append(left[i]) 
                i+=1
            elif right[j][0] != x: 
                answer.append(right[j]) 
                j+=1
            k+=1
        
        while i < len(left): 
            if left[i][0] != x:
                answer.append(left[i])
            i+=1
            

        while j < len(right): 
            if right[j][0] != x:
                answer.append(right[j])
            j+=1
            
        return answer
    return dots

num = int(input())
dots = []
x = 0 # иксовая координата оси симметрии

for i in range(num):
    dots.append(list(map(float, input().split())))
    x += dots[i][0]
x = x/num
# получен список dots, надо сортировать
dots = sliv(dots, x) # отсортирован, точки на оси симметрии удалены

print(mirror(dots, len(dots), x))