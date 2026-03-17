numero = int(input("Ingrese un número: "))


if numero < 0:
    print("El factorial no existe para números negativos")
else:
    factorial = 1
    
    
    for i in range(1, numero + 1):
        factorial *= i
    
    
    print("El factorial de", numero, "es:", factorial)