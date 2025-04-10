'''Дано N < 100 -- количество смурфов, а также M < 200 -- количество измерений (условий). 
Далее следует M строк, каждая содержит три числа и знак -- l, r, k, >/< где l и r -- первый и последний 
номер измеренных в рамках одного измерения смурфов (измерение включает всех смурфов с номерами от l до r, 
l < r, нумерация начинается с 1), k -- число, с которым сравнивается суммарный рост и знак меньше либо 
равно <= или больше либо равно >=, который говорит о том, как связаны измеренный суммарный рост и k.

Формат вывода
"YES" если итоговая система неравенств совместима и "NO" если нет.'''

'''parameters = list(map(int, input().split()))
rebra = []
for i in range(parameters[1]):
    data = list(input().split()) # l, r, k, oper
    data[0] = int(data[0])
    data[1] = int(data[1])
    data[2] = int(data[2])
    if data[3] == "<=":
        rebra.append((data[0] - 1, data[1], data[2]))
    else: rebra.append((data[1], data[0] - 1, (-1) * data[2]))'''
rebra = [(4, 2, -8), (3, 1, -5), (2, 0, -7), (0, 4, 3), (0, 4, 3)]
parameters = [4, 5]
#rebra = [(0, 4, 5), (1, 3, 10), (0, 3, 3), (1, 3, 7)]
#parameters = [4, 4]
#сделали ребра



# объяснение: вершины графа - суммы смурфов, т.е.
# s[i] - вершина
# s[i] = sigma(k = 1, i)(mass_k)
# => пусть на ввод поступает 3 4 8 >=
# => s[4] - s[3-1] >= 8 , надо преобразовать
# => s[2] <= s[4] + (-8) , это значит, что появилось ребро из s[4] в s[2] с массой (-8)
# пусть s[a] - s[b] <= x, s[b] - s[c] <= y, s[c] - s[a] <= z
# => складываем неравенства
# s[a] - s[b] + s[b] - s[c] + s[c] - s[a] = 0 <= x + y + z
# x + y + z >= 0
# в ином случае система решений не имеет

# ищем отрицательный цикл

'''def relaksatsiya(a, b, w, dist, prev):
    # запихнуть вершины и вес ребра между ними
    print(f"dist[{a}]: {dist[a]} dist[{b}]: {dist[b]}, w {w}")
    if dist[b] > dist[a] + w:
        dist[b] = dist[a] + w
        prev[b] = a
        print(f"--> dist[{a}]: {dist[a]} dist[{b}]: {dist[b]}, w {w}")
        return True
    return False

def cycle(parameters, rebra, start):
    dist = [float('inf')] * (parameters[0] + 1)
    prev = [None for i in range(parameters[0] + 1)]
    dist[start] = 0
    for i in range(len(rebra)):
        for (a, b, w) in rebra:
            relaksatsiya(a, b, w, dist, prev)
    print("---")

def shtuka(parameters, rebra):
    #for (a, b, w) in rebra:
    for i in range(len(rebra)):
        if not cycle(parameters, rebra, rebra[i][0]): return 'no'
        #if not cycle(parameters, rebra, rebra[i][1]): return 'no'
    return 'yes'
    '''


#print(shtuka(parameters, rebra))


'''
d = [None] * n
d[s] = 0

for i in range(n-1):
    for u, v, w in edges:
        if d[u] is not None:
            d[v] = min(float('inf') if d[v] is None else d[v], d[u] + w)'''