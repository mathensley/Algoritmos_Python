import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(G, start):
    dist = {node: float('inf') for node in G}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current, u = heapq.heappop(pq)
        for v, w in G[u]:
            if dist[v] > current + w:
                dist[v] = current + w
                heapq.heappush(pq, (dist[v], v))
    return dist


edges = [
    (1, 2, 10),
    (1, 3, 5),
    (2, 3, 2),
    (2, 4, 1),
    (3, 2, 3),
    (3, 4, 9),
    (3, 5, 2),
    (4, 5, 4),
    (5, 4, 6),
    (5, 1, 7)
]
G = {}

for edge in edges:
    u, v, w = edge
    if u not in G:
        G[u] = []
    G[u].append((v, w))

print("Lista de adjacências do grafo:")
for node in G:
    print(f"Origem: {node} -> Destinos e Pesos:", G[node])

start_vertex = 1
distances = dijkstra(G, start_vertex)

print("Distâncias mínimas a partir do vértice", start_vertex)
for vertex, distance in distances.items():
    print("Vértice:", vertex, "- Distância mínima:", distance)

'''
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='black', font_color='white')
edge_labels = {(u, v): w['weight'] for u, v, w in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title('Graph')
plt.show()
'''