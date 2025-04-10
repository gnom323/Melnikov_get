'''Дан ориентированный невзвешенный граф. Определите, 
существует ли у него единственная топологическая сортировка.

Формат ввода
В первой строке содержатся количество вершин N (1 ≤ n ≤ 2 * 10^5) и 
количество рёбер M (1 ≤ m ≤ 10^5) в графе. В следующих M строках задаются 
рёбра графа, каждое -- парой чисел, номерами начальной и конечной вершины. 
Вершины нумеруются с 1.

Формат вывода
Выведите “YES”, если существует единственная топологическая сортировка 
вершин графа, и “NO” если существует несколько вариантов сортировки. 
Если топологическая сортировка невозможна, выведите -1.'''

'''def super_top_sort(n, edges):
    from_to = [[] for _ in range(n + 1)] # собственно сортировка
    rank = [0] * (n + 1)
    for u, v in edges:
        from_to[u].append(v)
        rank[v] += 1
    queue = []
    for i in range(1, n + 1):
        if rank[i] == 0:
            queue.append(i)
    order = []
    visited = [0] * (n + 1)


    def dfs(v):
        visited[v] = 1
        for u in from_to[v]: # для каждой соседней вершины у этой v
            #print(f"v {v}, u {u}")
            #print(f"visited[u = {u}] {visited[u]}")
            if visited[u] == 1:
                return False  
            if visited[u] == 0 and not dfs(u):
                return False
        visited[v] += 1
        return True
    for i in range(1, n + 1):
        if visited[i] == 0:
            if not dfs(i):
                return -1 

    
    while queue:
        if len(queue) > 1:
            return "NO"
        u = queue.pop(0)
        order.append(u)
        for v in from_to[u]:
            rank[v] -= 1
            if rank[v] == 0:
                queue.append(v)
    return "YES" if len(order) == n else -1

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(m)]
print(super_top_sort(n, edges))'''







# -1 -> нет сортировки
# YES -> единственная топологич сортировка
# NO -> несколько топол сорт

parameters = list(map(int, input().split()))
rebra = []
for i in range(parameters[1]):
    rebra.append(tuple(map(int, input().split())))

# логик
def topologicheskaya_sortirovka(n, rebra):
    # i является номером вершины, начинается с 1
    def dfs(v): # поиск циклов
        visited[v] = 1 # отмечаем вершину как посещенную
        for u in napravleniye[v]: # чекаем "потомков"
            if visited[u] == 1: # уже есть посещенный потомок
                return False  
            if visited[u] == 0 and not dfs(u):
                return False
        visited[v] = 2
        # visited[i] == 1 -> цикл
        # visited[i] == 0 -> вершина не посещена
        # visited[i] == 2 -> вершина посещена, но не находится в цикле
        # при наличии цикла программа возвращает -1
        return True
    
    napravleniye = []
    for i in range(n + 1): napravleniye.append([]) # список списков

    prnt = [0] * (n + 1)

    for a, b in rebra:
        napravleniye[a].append(b) # napravleniye[i][0] -> napravleniye[i][1]
        prnt[b] += 1 # кол-во "родителей"
    
    poryadok = []   # собственно топологическая сортировка

    ochered = []
    for i in range(1, n + 1):
        if prnt[i] == 0: # если у вершины нет "родителей"
            ochered.append(i) # добавляем вершину в очередь
    
    # проверка возможности топологич сортировки
    visited = [0] * (n+1) # список-индикатор посещения вершины
    for i in range(1, n + 1): # проверяем вершины, начиная с 1
        if visited[i] == 0: # если вершина еще не была посещена
            if dfs(i) == False: 
                return -1 

    # заполняем список "poryadok" т.е. производим сортировку
    while ochered: # пока очередь не пуста
        if len(ochered) > 1: # есть две вершины без "родителей"
            return "NO" # не единственная топологич сортировка
        u = ochered.pop(0) # удаляем вершину из очереди
        poryadok.append(u) # и добавляем ее в топологич сортировку
        for v in napravleniye[u]: # чекаем каждого "потомка" удаленной вершины
            prnt[v] -= 1 # снижаем количество ее "родителей"
            if prnt[v] == 0:
                ochered.append(v)
    
    return "YES" if len(poryadok) == n else -1 # проверка на изолированные вершины

print(topologicheskaya_sortirovka(parameters[0], rebra))
#print(rebra)

