
def pendrive(t, c):
    i = 0
    x = []
    while i < len(t) and t[i] <= c:
        x.append(t[i])
        c = c - t[i]
        i += 1
    return x

t = [10, 15, 20, 20, 30, 35, 40, 50]
c = 90
print(pendrive(t, c))