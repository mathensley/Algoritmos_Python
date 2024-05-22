import networkx as nx
import matplotlib.pyplot as plt

graph = {}
edges = [
    (1, 2),
    (1, 5),
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 4),
    (4, 5)
]

for edge in edges:
    u, v = edge
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

print(graph)
for vertex in graph:
    print(vertex, "->", graph[vertex])
'''
edges1 = []
for vertex in graph:
    for neighbor in graph[vertex]:
        if (neighbor, vertex) not in edges1:
            edges1.append((vertex, neighbor))
print(edges1)
'''
graph1 = nx.Graph()
graph1.add_edges_from(edges)
print(graph1)
#nx.draw(graph1, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, 
#        font_weight='bold', edge_color='black', linewidths=1, pos=nx.spring_layout(graph1))
nx.draw(graph1, with_labels=True, node_color='black', font_color='white', pos=nx.spring_layout(graph1))
plt.title('Grafo')
plt.show()

#G = nx.complete_graph(4)
G = nx.path_graph(4)
nx.draw(G, with_labels=True, font_color='white', pos=nx.bfs_layout(G, 1))
plt.show()