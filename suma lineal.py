def suma_lineal(a, b):
    pasos = 0 #o(1)
    while b > 0:  #o(log n)
        a = a + 1  #o(1)
        b = b - 1  #o(1)
        pasos += 1 #o(1)
    print(f"total de pasos ejecutados: {pasos}")#o(1)
    return a#o(1)

resultado = suma_lineal(3, 6)
print("resultado:", resultado) 