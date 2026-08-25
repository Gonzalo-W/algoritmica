def encontrar_duplicados(lista):
    for i in range(len(lista)):#o(1)
        for j in range(i + 1, len(lista)):#o(n)
            if lista[i] == lista[j]:#o(1)
                return True   #o(1)
    return False   o(n)+o(n)+o(1)+o(1)
    #o(n^2)+o(1)