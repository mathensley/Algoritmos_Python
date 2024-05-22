import random
import math as m
import matplotlib.pyplot as plt

def gera_pontos(num):
    f_x = (-5, 5)
    f_y = (-5, 5)
    
    pontos = [(random.randint(f_x[0], f_x[1]), random.randint(f_y[0], f_y[1])) for _ in range(num)]
    return pontos

def gera_grafico(pontos):
    x = [ponto[0] for ponto in pontos]
    y = [ponto[1] for ponto in pontos]
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, color='black')
    plt.title('Gráfico de Dispersão de Pontos Aleatórios')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)
    plt.show()

def calc_dist(a, b):
    return m.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def menor_dist(pontos):
    p1 = []
    p2 = []
    distmin = 1000
    for i in range(0, len(pontos)-1):
        for j in range(i+1, len(pontos)):
            dist = calc_dist(pontos[i], pontos[j])
            if dist < distmin:
                p1 = list(pontos[i])
                p2 = list(pontos[j])
                distmin = dist
    return (p1, p2, distmin)


pontos = gera_pontos(15)
for p in pontos:
    print(p)
ponto1, ponto2, dist = menor_dist(pontos)
print(ponto1, ponto2, dist)
gera_grafico(pontos)