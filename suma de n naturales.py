def suma_n_naturales(n):
    #caso base
    if n == 1:
        return n
    #caso recursivo
    else:
        return n + suma_n_naturales(n-1)


n = int(input("Ingrese el valor de n: "))
print(suma_n_naturales(n))

# 5 => 5;4;3;2;1;despegue
def cuentaregresiva(n):
    #caso base
    if n == 0: # n= 5 x: n =4 ; 3 = 0
        print("despegue...")
        #caso recursivo
    else:
        print(n) #5; 4
        cuentaregresiva(n-1)

n = int(input("Ingrese el numero: "))
cuentaregresiva(n)


#potencia de base de entera (exponente natural)
# 2**4 = 16 ; 2**8 => 2*2*2*2*2*2*2*2 = 256
def potencia(a , b): #(2,8) ; (2,7) ; (2,6) ; (2,5) ; (2,4) ; (2,3) ; (2,2) ; (2,1) ; (2,0)
    #caso base
    if b == 0: # 8 == 0 ; 7 == 0 ; 6 == 0 ; 5 == 0 ; 4 == 0 ; 3 == 0 ; 2 == 0 ; 1 == 0 ; 0 == 0
        return 1
    #caso recursivo
    else:
        return a * potencia(a, b-1)#2*potencia(2,8-1) ; 2*potencia(2,7) ; 2*potencia(2,6) ; 2*potencia(2,5) ; 2*potencia(2,4) ; 2*potencia(2,3) ; 2*potencia(2,2) ; 2*potencia(2,1) ; 2*potencia(2,0)

x = int(input("Ingrese el valor de la base: ")) #2
y = int(input("Ingrese el valor del exponente: ")) #4       
print(potencia(x, y)) #imprimir (potencia(2,8)) => 256