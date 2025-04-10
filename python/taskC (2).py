params = list(map(int, input().split()))
rebra = []
for i in range(params[1]):
    data = list(input().split()) # l, r, k, oper
    data[0] = int(data[0])
    data[1] = int(data[1])
    data[2] = int(data[2])
    if data[3] == "<=":
        rebra.append((data[0] - 1, data[1], data[2]))
    else: rebra.append((data[1], data[0] - 1, (-1) * data[2]))

#rebra = [(4, 2, -8), (3, 1, -5), (2, 0, -7), (0, 4, 3), (0, 4, 3)]
#params = [4, 5]

#rebra = [(0, 4, 5), (1, 3, 10), (0, 3, 3), (1, 3, 7)]
#params = [4, 4]

# объяснение: вершины графа - суммы смурфов, т.е.
# s[i] - вершина
# s[i] = sigma(k = 1, i)(mass_k)
# => пусть на ввод поступает 3 4 8 >=
# => s[4] - s[3-1] >= 8 , надо преобразовать
# => s[2] <= s[4] + (-8) , это значит, что появилось ребро из s[4] в s[2] с массой (-8)
# пусть s[a] -[ s[b] <= x, s[b] - s[c] <= y, s[c] - s[a] <= z
# => складываем неравенства
# s[a] - s[b] + s[b] - s[c] + s[c] - s[a] = 0 <= x + y + z
# x + y + z >= 0
# в ином случае система решений не имеет

# ищем отрицательные циклы


def answer(rebra, params):
    for u, v, w in rebra: # требуется выбирать стартовую точку
        if(cycle(rebra, u, params)) == False: return 'NO'
    return 'YES'

def cycle(rebra, start, params):
    infinity = float('inf')
    dist = [infinity] * (params[0] + 1)
    #print(dist)
    dist[start] = 0

    for i in range(len(rebra) - 1):
        for u, v, w in rebra:
            if dist[u] != infinity and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in rebra:
        if dist[u] != infinity and dist[u] + w < dist[v]:
            return False

    return True

print(answer(rebra, params))