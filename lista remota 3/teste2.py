def DFS(G):
    components = []
    for u in G:
        color[u] = 'WHITE'
    for u in G:
        if color[u] == 'WHITE':
            component = []
            visitDFS(u, component)
            components.append(component)
    return components

def visitDFS(u, component):
    color[u] = 'GRAY'
    component.append(u)
    for v in G[u]:
        if color[v] == 'WHITE':
            visitDFS(v, component)
    color[u] = 'BLACK'

n, m = map(int, input().split())
G = {}
color = {}
for i in range(1, n + 1):
    G[i] = []
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    components = DFS(G)
    print(len(components), len(max(components, key=len)))