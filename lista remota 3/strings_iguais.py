def make_equal(n, a, b):
    i = 0
    count = 0
    while i < n:
        if a[i] != b[i]:
            count += 1
            if i + 1 < n and a[i+1] == b[i]:
                i += 1
        i += 1
    return count

n = int(input())
a = input()[:n]
b = input()[:n]
print(make_equal(n, a, b))