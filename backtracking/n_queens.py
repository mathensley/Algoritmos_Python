import matplotlib.pyplot as plt

def is_valid(x, i):
    for j in range(i):
        if (x[j] == x[i]) or (abs(x[i] - x[j]) == abs(i - j)):
            return False
    return True

def n_queens(x, i):
    if i == n:
        print(x)
        gera_tabuleiro(x)
    else:
        for j in range(n):
            x[i] = j
            if is_valid(x, i):
                n_queens(x, i+1)

def gera_tabuleiro(pos):
    coords = gera_coord(pos)
    p_x = [ponto[0] for ponto in coords]
    p_y = [ponto[1] for ponto in coords]
    
    plt.figure(figsize=(6, 4))
    plt.scatter(p_x, p_y, color='black', label='Pontos')
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()

def gera_coord(lista):
    result = [(i, lista[i]) for i in range(n)]
    return result
    

n = 4
n_queens([-1]*n, 0)