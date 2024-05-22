import heapq

def dijkstra(G, start, end):
    dist = {node: float('inf') for node in G}
    dist[start] = 0
    pq = [(0, start)]
    pred = {}

    while pq:
        current, u = heapq.heappop(pq)
        if u == end:
            return path(pred, start, end)
        for v, w in G[u]:
            if dist[v] > current + w:
                dist[v] = current + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))
    return -1

def path(pred, start, end):
    path = ""
    while end != start:
        path = str(end) + " " + path
        end = pred[end]
    path = str(start) + " " + path
    return path.strip()

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    a, b, w = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((b, w))
    graph[b].append((a, w))

print(dijkstra(graph, 1, n))