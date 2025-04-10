from collections import deque

# Функция обхода графа в ширину (BFS) для выделения одной компоненты связности
def bfs(graph, start, visited, component):
    queue = deque([start])
    visited.add(start)
    component.append(start)
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                component.append(neighbor)

# Функция поиска всех компонент связности в графе
def find_connected_components(graph):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            component = []
            bfs(graph, node, visited, component)
            components.append(component)
    
    return components

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E'],
    'I': ['J'], # Отдельная компонента
    'J': ['I']  # Отдельная компонента
}

components = find_connected_components(graph)
print("Компоненты связности:")
for i, component in enumerate(components, 1):
    print(f"Компонента {i}: {component}")

for i in range(len(components)):
    print(f"Компонента {i+1}: {components[i]}")
