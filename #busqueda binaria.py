#busqueda binaria
def busquedabinaria(lista, b):
    n = len(lista)
    i = 0
    j = n-1
    while i <= j:
        m = (i+j)//2
        if (b < lista[m]):
            j = m - 1
        elif (b > lista[m]):
            i = m  + 1
        else:
            return m
    return -1


lista =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("la posicion es: ", busquedabinaria(lista, 14))