from collections import deque

def dfs_mod(graph, start, counter, visited=None):
    # надо найти такую точку, из которой 'пробегается' весь граф
    if visited is None:
        visited = set()
    
    if start not in visited:
        #print(start, end=" ")
        counter += 1
        visited.add(start)
        if(graph.get(start) != None): 
            for neighbor in graph[start]:
                return dfs_mod(graph, neighbor, counter, visited)
        else:return counter
    return counter

def can_rearrange_cities(cities):
    if len(cities) < 2: return False # невозможно играть в города, когда в списке только один город
    
    first_letters = []
    last_letters = []

    for city in cities:
        first_letters.append(city[0])
        last_letters.append(city[-1])
    
    graph = {}
    for i in range(len(cities)):
        graph[first_letters[i]] = last_letters[i]
    #print(graph) # есть граф, надо поискать возможные 'места разрыва'

    for i in range(len(cities)):
        counter = 0
        counter = dfs_mod(graph, first_letters[i], counter)
        if counter == len(cities): return True
    return False



cities1 = ["london", "newyork", "klin", "vienna"]  
cities2 = ["paris", "sydney", "york", "kyoto"]  
cities3 = ["paris", "london", "moscow"] 
cities4 = ["a", "b", "c"]
cities5 = ["alupa"]
cities6 = ["manchester", "riga", "abakan", "nottingham"] 

print(can_rearrange_cities(cities1)) 
print(can_rearrange_cities(cities2)) 
print(can_rearrange_cities(cities3))
print(can_rearrange_cities(cities4))
print(can_rearrange_cities(cities5))
print(can_rearrange_cities(cities6))