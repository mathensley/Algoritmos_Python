def bellman_ford(G, start):
    dist = {node: float('inf') for node in G}
    dist[start] = 0
    for _ in range(len(G)-1):
        for u in G:
            for v, w in G[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
    for u in G:
        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                raise ValueError("O grafo contém um ciclo negativo")
    return dist
'''
edges = [
    (1, 2, 6),
    (1, 3, 7),
    (2, 3, 8),
    (2, 4, 5),
    (3, 4, -3),
    (3, 5, 9),
    (4, 2, -2),
    (5, 4, 7),
    (5, 1, 2)
]
'''
edges = [
    (1, 2, 2),
    (1, 4, 10),
    (2, 4, 3),
    (3, 2, -25),
    (4, 3, 12)
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
shortest_distances = bellman_ford(G, start_vertex)
print("Menor distância de {} para outros vértices:".format(start_vertex))
for vertex, distance in shortest_distances.items():
    print("Para o vértice {}: {}".format(vertex, distance))