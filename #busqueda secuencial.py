#busqueda secuencial
def busquedasecuencial(lista, b):
    n = len(lista)
    for i in range(0, n):
        if lista[i] == b:
            print("contrado en la posicion: ", i)
    return -1

lista = [4,5,9,2,8,1]
busquedasecuencial(lista, 8)