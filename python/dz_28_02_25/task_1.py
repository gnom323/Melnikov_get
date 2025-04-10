def gruppa(graph, node, colors=None, color=0):
    if colors is None: 
        colors = {}
    
    if node in colors:
        return colors[node] == color 
    colors[node] = color
    
    for neighbor in graph[node]:
        if not gruppa(graph, neighbor, colors, 1 - color):
            return False
    
    return True

def pairs(graph, n):
    colors = {} # словарь с 'окрашенными' вершинами графа
    if(n < 2): return False # в двудольном графе не может быть менее двух вершин
    for node in graph:
        if node not in colors: 
            if not gruppa(graph, node, colors):
                return False  
    return True


n = int(input("кол-во людей n:"))
k = int(input("введите число связей:"))
print("далее в каждую строку - связи (пары чисел через пробел):")

graph = {}
for i in range(k):
    pair = input().split()
    if graph.get(pair[0]) == None: graph[pair[0]] = list(pair[1])
    else: graph[pair[0]].append(pair[1])
    if graph.get(pair[1]) == None: graph[pair[1]] = list(pair[0])
    else: graph[pair[1]].append(pair[0])

print(pairs(graph, n))