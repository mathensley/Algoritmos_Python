import networkx as nx
import matplotlib.pyplot as plt

def DFS(G):
    for u in G:
        color[u] = 'WHITE'
        p[u] = -1
    for u in G.nodes():
        if color[u] == 'WHITE':
            visitDFS(u)
    return color, d, f, p

def visitDFS(u):
    global time
    color[u] = 'GRAY'
    time += 1
    d[u] = time
    for v in G.neighbors(u):
        if color[v] == 'WHITE':
            p[v] = u
            visitDFS(v)
    color[u] = 'BLACK'
    time += 1
    f[u] = time

G = nx.DiGraph()
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
G.add_edges_from(edges)

nx.draw(G, with_labels=True, node_color='black', font_color='white', pos=nx.circular_layout(G))
plt.title('Grafo')
plt.show()

time = 0
color = {}
d = {} # discovery time
f = {} # final time
p = {} # predecessor

color, d, f, p = DFS(G)
print("Vertex colors:", color)
print("Discovery times:", d)
print("Final times:", f)
print("Predecessors:", p)