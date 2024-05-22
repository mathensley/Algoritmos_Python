def calc_troco(c, total):
    s = []
    soma = 0
    while soma != total:
        x = max(c)
        if soma + x <= total:
            s.append(x)
            soma += x
        else:
            c.remove(x)
    return s

#c = [100, 25, 10, 5, 1]
c = [6, 4, 1]
total = 8
print(calc_troco(c, total))