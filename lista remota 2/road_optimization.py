n, l, k = map(int, input().split())
coord = list(map(int, input().split()))[:n]
speed = list(map(int, input().split()))[:n]
coord.append(l)
dp = [[1000000000 for _ in range(n+1)] for _ in range(k+1)]
dp[0][0] = 0
for i in range(n+1):
    for j in range(k+1):
        for p in range(j+1):
            dp[j][i] = min(dp[j][i], dp[j-p][i-p-1]+(coord[i]-coord[i-p-1])*speed[i-p-1])

result = dp[0][-1]
for i in range(k+1):
    if result > dp[i][-1]:
        result = dp[i][-1]
print(result)