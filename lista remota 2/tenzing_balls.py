t = int(input())
for _ in range(t):
    n = int(input())
    colors = list(map(int, input().split()))[:n]
    partial = [-1000000000] * (n + 1)
    result = [0] * (n + 1)
    for i in range(n):
        result[i+1] = max(result[i], i + partial[colors[i]])
        partial[colors[i]] = max(result[i] - i + 1, partial[colors[i]])
    print(result[-1])
