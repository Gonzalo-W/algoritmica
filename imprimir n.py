def imprimirnumeros(n):
    if n == 0:
        print("nro", n)
    else:
        print("nro", n)
        imprimirnumeros(n-1)
        h = int(input("ingreseunnro:"))
        imprimirnumeros(h)