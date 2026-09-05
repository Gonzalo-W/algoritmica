import random

def selection_sort(lista):
    n = len(lista)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista







n = int(input("ingrese la cantidad de numeros aleatorios que desea: "))
lista_aleatoria = []
for _ in range(n):
     lista_aleatoria.append(random.randint(0, 500))

print(f"la lista aleatoria es: {lista_aleatoria}")
print("-------------------------------------------")
print(f"la lista ordenada es: {selection_sort(lista_aleatoria)}")
