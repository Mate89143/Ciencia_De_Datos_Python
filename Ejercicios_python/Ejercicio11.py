numero = int(input("Ingrese un numero: "))

if str(numero).count('9'):
    print("El numero contiene el digito 9.")
elif numero % 9 == 0:
    print("El numero es multiplo de 9.")
else:
    print("El numero no es multiplo de 9.")