def find_set(u):
    if dis_set[u] < 0:
        return u
    dis_set[u] = find_set(dis_set[u])
    return dis_set[u]

def union(u, v):
    u = find_set(u)
    v = find_set(v)
    if u == v:
        return False
    if dis_set[u] < dis_set[v]:
        u, v = v, u
    dis_set[v] += dis_set[u]
    dis_set[u] = v
    return True

n, m = map(int, input().split())
dis_set = [-1] * (n + 1)
components = n
largest = 1
for i in range(m):
    a, b = map(int, input().split())
    if union(a, b):
        components -= 1
        largest = max(largest, -dis_set[find_set(a)])
    print(components, largest)