import heapq
import sys

def dijkstra(G, start, end):
    dist = [float('inf')]*(n+1)
    pq = [(0, start)]
    path = [0]*(end+1)

    while pq:
        c, u = heapq.heappop(pq)
        for v, w in G[u]:
            if dist[v] > c + w:
                dist[v] = c + w
                path[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    l = [end]
    x = end
    if path[end] > 0:
        while x != 1:
            x = path[x]
            l.append(x)
        print(*l[::-1])
    else:
        print(-1)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    if a != b:
        graph[a].append((b, w))
        graph[b].append((a, w))
dijkstra(graph, 1, n)