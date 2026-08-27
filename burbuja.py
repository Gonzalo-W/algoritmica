# 3-7-2-5-1
# 3-7-2-1-5
# 3-7-1-2-5
# 3-1-7-2-5
import random
# 3-1-2-7-5
# 1-3-2-7-5
# 1-2-3-7-5
# 1-2-3-5-7

def metodo_burbuja(lista):
    n = len(lista)
    intercambios = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambios += 1
    return lista, intercambios

aleatorios = []
for _ in range(100):
    n = random.randint(1,300)
    aleatorios.append(n)
    print(f"los aleatorios son: {aleatorios}")


array_lista =[5,2,4,1,3]
ordenado, intercambio = metodo_burbuja(array_lista)
print(f"la lista ordenada es:{ ordenado } y se intercambiaron { intercambio }")