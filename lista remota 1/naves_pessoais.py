def calc_luck(num):
    max_d = -1
    min_d = 10
    for d in str(num):
        d = int(d)
        if d > max_d:
            max_d = d
        if d < min_d:
            min_d = d
    return max_d - min_d

def find_luckiest(l, r):
    max_diff = -1
    luckiest = 0

    for i in range(l, r + 1):
        diff = calc_luck(i)
        if diff == 9:
            print(i)
            return
        if diff >= max_diff:
            max_diff = diff
            luckiest = i

    print(luckiest)

t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    find_luckiest(l, r)