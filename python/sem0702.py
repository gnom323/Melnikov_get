import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

nodes = [1, 2, 3, 4, 5]
# кортеж (id_1, id_2) означает, что узлы id_1 и id_2 соединены ребром
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

nx.draw(G, with_labels=True, font_weight='bold', 
        node_color='green', edge_color='black', width=3)
plt.show()