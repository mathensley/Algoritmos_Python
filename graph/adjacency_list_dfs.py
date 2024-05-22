# essa função DFS funciona apenas para grafos conectados ou dígrafos fortemente conectados
def dfs(graph, start, visited):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {}
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 2),
    (4, 3),
    (5, 4),
    (5, 6),
    (6, 6)
]

for edge in edges:
    u, v = edge
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

for node in graph:
    print(f"Origem: {node} -> Destinos: {graph[node]}")

dfs(graph, 1, None)