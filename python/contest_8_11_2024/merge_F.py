def merge_sort(dots, x): # функция для сортировки 
    answer = []
    if len(dots) > 1:  # из пункта 1 помним, если в массиве 1 элемент, то он уже отсортирован
        mid = len(dots)//2
        left = dots[:mid] 
        right = dots[mid:]
        left = merge_sort(left, x)  
        right = merge_sort(right, x)  

        i = j = k = 0

        while i < len(left) and j < len(right) and k <len(left) + len(right): 
            if left[i] < right[j] and left[i][0] != x: 
                answer.append(left[i]) 
                i+=1
            elif right[j][0] != x: 
                answer.append(right[j]) 
                j+=1
            k+=1
#добавим оставшиеся элементы из left и right в nums
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
dots = merge_sort(dots, x)
lefts = dots[:len(dots)//2]
rights = dots[len(dots)//2:]
print(*dots)
print(merge_sort(dots, x)) # отсоритирован по иксовой координате, исключены точки на оси симметрии
print(lefts)
# точки не совпадают -> победа