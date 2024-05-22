import math
import threading

def is_valid(x, elem):
    return elem in x

def perm(x, a, m, result):
    if m == n:
        result.append(x[:])
        #print(f"Thread {thread_id}: Permutação encontrada: {x}")
    else:
        for i in range(n):
            if not is_valid(x[:m], a[i]):
                x[m] = a[i]
                perm(x, a, m+1, result)
                #x[m] = 0

def worker(thread_id):
    start = (n * thread_id) // num_threads
    end = min(n, (n * (thread_id + 1)) // num_threads)
    for i in range(start, end):
        x = [0] * n
        x[0] = lista[i]
        perm(x, lista, 1, result)

lista = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(lista)
num_threads = 4
result = []

threads = []
for i in range(num_threads):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

#for p in result:
    #print(p)

print(math.factorial(n))