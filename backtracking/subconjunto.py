def valid(prox, somaParcial, restante, d):
    return not((somaParcial + restante < d) or (somaParcial + prox > d))

def somaSubRec(x, lista, i, somaParcial, restante, d):
    if somaParcial == d:
        print(x, somaParcial)
    elif i < n and valid(lista[i], somaParcial, restante, d):
        x.append(lista[i])
        somaSubRec(x, lista, i+1, somaParcial+lista[i], restante-lista[i], d)
        x.remove(lista[i])
        somaSubRec(x, lista, i+1, somaParcial, restante-lista[i], d)


lista = [1,2,3,5,6,8]
res = sum(lista)
n = len(lista)
somaSubRec([], lista, 0, 0, res, 9)