def calc_valores(m, p, v):
    p_total = 0
    v_total = 0
    for i in range(0, len(m)):
        if m[i] == "1":
            p_total += p[i]
            v_total += v[i]
    return p_total, v_total

def knapsack(p, v, n, w):
    melhor_item = []
    max_v = 0
    for i in range(0, 2**n):
        itens_mochila = [x for x in bin(i)[2:].zfill(n)]
        print(itens_mochila)
        peso, valor = calc_valores(itens_mochila, p, v)
        if peso <= w and valor > max_v:
            max_v = valor
            melhor_item = itens_mochila
            print(max_v)
    return max_v, melhor_item

p = [2, 5, 10, 5]
v = [20, 30, 50, 10]
w = 16
max_valor, mochila = knapsack(p, v, len(p), w)
print("Maior valor: ", max_valor)
print("Melhor conjunto encontrado: ", mochila)
