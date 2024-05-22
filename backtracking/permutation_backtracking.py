import math

def is_valid(x, elem):
    return elem in x

def perm(x, a, m):
    if m == n:
        print(x)
    else:
        for i in range(0, n):
            if not is_valid(x[:m], a[i]):
                x[m] = a[i]
                perm(x, a, m+1)
                #x[m] = 0

lista = [1, 2, 3]
n = len(lista)
perm([0]*n, lista, 0)
print(math.factorial(n))