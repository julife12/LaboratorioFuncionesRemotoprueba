c=int(input("digite la cantidad de veces que se hara el procedimeinto: "))
for i in range(1, c+1):
    def a_power_b(a,b):  
        cuadrado=1
        for j in range(1, b+1):
            cuadrado=cuadrado*a

    
        return cuadrado

    
    try:
        n1=int(input("digite el numero: "))
        if n1==0:
            break
    except ValueError:
        print("debe digitar un numero valido, intente de nuevo")
        break

    try:
        p1=int(input("digite la potencia: "))
    except ValueError:
        print("debe digitar un numero valido, intente de nuevo")
        break

    nm1=a_power_b(n1, p1)
    print("elnumero elevado es igual a: ",nm1)
    
