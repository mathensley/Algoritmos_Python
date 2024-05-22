import random
import matplotlib.pyplot as plt

def gera_pontos(num):
    f_x = (-10, 10)
    f_y = (-10, 10)
    
    pontos = [(random.randint(f_x[0], f_x[1]), random.randint(f_y[0], f_y[1])) for _ in range(num)]
    return pontos

def orientacao(p1, p2, p3):
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0]) # produto cruzado entre vetores: a.d - b.c
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def graham_scan(pontos):
    if len(pontos) < 3:
        return None
    p_inicial = min(pontos, key=lambda ponto: ponto[1])
    pontos.sort(key=lambda ponto: (orientacao(p_inicial, ponto, ponto), -ponto[1], ponto[0]))
    hull = [pontos[0], pontos[1]]
    
    for i in range(2, len(pontos)):
        while len(hull) > 1 and orientacao(hull[-2], hull[-1], pontos[i]) != 2:
            hull.pop()
        hull.append(pontos[i])
    
    return hull

def gera_grafico(pontos, cv_h):
    p_x = [ponto[0] for ponto in pontos]
    p_y = [ponto[1] for ponto in pontos]
    cv_x = [ponto[0] for ponto in cv_h]
    cv_y = [ponto[1] for ponto in cv_h]
    
    cv_x.append(cv_x[0])
    cv_y.append(cv_y[0])
    
    plt.figure(figsize=(6, 4))
    plt.scatter(p_x, p_y, color='black', label='Pontos')
    plt.plot(cv_x, cv_y, color='pink', linestyle='--', linewidth=2, label='Polígono Convexo')
    plt.legend()
    plt.title('Convex Hull Plot')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid(True)
    plt.show()

pontos = gera_pontos(12)
for p in pontos:
    print(p)
cv_h = graham_scan(pontos)
if cv_h is None:
    print("Não pode menos que três pontos!")
else:
    print("Convex Hull: ", cv_h)
    gera_grafico(pontos, cv_h)