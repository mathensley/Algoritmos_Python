def knapsack(x, i, itens, valor, max_v, w):
    if i == n:
        if valor > max_v:
            max_v = valor
            print(max_v, x)
    else:
        if itens[i][0] <= w:
            x[i] = 1
            knapsack(x, i+1, itens, valor + itens[i][1], max_v, w - itens[i][0])
        x[i] = 0
        knapsack(x, i+1, itens, valor, max_v, w)



itens = [(2, 20), (5, 30), (10, 50), (5, 10)]
w = 16
n = len(itens)
knapsack([-1]*n, 0, itens, 0, 0, w)