def find_valid_point(x, y):
    dist_ab = abs(x) + abs(y)
    half_dist_ab = dist_ab // 2
    
    for i in range(x+1):
        for j in range(y+1):
            if ((abs(i) + abs(j) == half_dist_ab) and
                (abs(x - i) + abs(y - j) == half_dist_ab)):
                print(i, j)
                return
    print(-1, -1)

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    find_valid_point(x, y)