'''for sosed in nayti_sosedey(vershina): # пихаем вершину в метод получения соседей, затем чекаем каждого соседа
            if sosed == konets: # нашли искомую вершину
                return shag + 1 
            elif 1 <= sosed <= 9999 and sosed not in visited: 
                visited.add(sosed)

                ochered.append((sosed, shag + 1))'''


def sum_symbols(x): # складываем цифры числа
    y = 0
    while x > 0:
        y += x % 10
        x //= 10
    return y

def nayti_sosedey(y):
    return [y - 2, y * 3, y + sum_symbols(y)]

def kalk(nachalo, konets):
    if nachalo == konets:
        return 0 # числа совпадают
    
    visited = set() 
    
    ochered = [(nachalo, 0)] # list -> сюда пихаем пары из вершинки и кол-ва шагов до нее
    
    visited.add(nachalo) # мн-во посещенных вершин

    index = 0  
    
    while index < len(ochered):
        print(ochered)
        vershina, shag = ochered[index] # вытаскиваем вершину и шаг из списка

        index += 1  
        
        '''sosed1 = vershina - 2
        sosed2 = vershina * 3
        sosed3 = 0
        x = vershina
        while x > 0: 
            sosed3 += x % 10
            x //= 10'''

        '''if sosed1 == konets: 
            return shag + 1
        elif sosed1 >= 1 and sosed1 <= 9999 and sosed1 not in visited:
            visited.add(sosed1)
            ochered.append((sosed1, shag + 1))
        
        if sosed2 == konets: 
            return shag + 1
        elif sosed2 >= 1 and sosed2 <= 9999 and sosed2 not in visited:
            visited.add(sosed2)
            ochered.append((sosed2, shag + 1))
        
        if sosed3 == konets: 
            return shag + 1
        elif sosed3 >= 1 and sosed3 <= 9999 and sosed3 not in visited:
            visited.add(sosed3)
            ochered.append((sosed3, shag + 1))'''
        for sosed in nayti_sosedey(vershina): # пихаем вершину в метод получения соседей, затем чекаем каждого соседа
            if sosed == konets: # нашли искомую вершину
                return shag + 1 
            elif 1 <= sosed <= 9999 and sosed not in visited: 
                visited.add(sosed)

                ochered.append((sosed, shag + 1))
        
numbers = list(map(int, input().split()))
print(kalk(numbers[0], numbers[1]))