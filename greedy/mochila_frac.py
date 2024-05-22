def mochila_frac(p, w):
    x = [0] * len(p)
    i = 0
    peso = 0
    while peso < w and i < len(x):
        if peso + p[i] <= w:
            x[i] = 1
            peso = peso + p[i]
        else:
            x[i] = (w - peso) / p[i]
            peso = w
        i += 1
    return x

#p = [50, 40, 30, 20, 10]
p = [40, 30, 20, 10]
w = 50
print(mochila_frac(p, w))