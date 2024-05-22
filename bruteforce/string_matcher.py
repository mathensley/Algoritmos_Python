def string_matcher(t, p):
    n = len(t)
    m = len(p)
    count = 0
    for i in range(n-m):
        j = 0
        while j < m and p[j] == t[i+j]:
            j += 1
        if j == m:
            print("padrão ocorre com descolamento: ", i)
            count += 1
    print(count, "padrões reconhecidos")


string_matcher("Palavras cruzadas são legais, mas vai se foder seu porra", "as")