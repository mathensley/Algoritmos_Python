def slice(arr, s):
    s.add(sum(arr))
    if len(set(arr)) > 1:
        mid = (max(arr) + min(arr)) // 2
        i = 0
        while i < len(arr) and arr[i] <= mid:
            i += 1
        slice(arr[:i], s)
        slice(arr[i:], s)
    return s

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))[:n]
    arr.sort()
    s = slice(arr, set())
    for _ in range(q):
        x = int(input())
        if x in s:
            print("Yes")
        else:
            print("No")