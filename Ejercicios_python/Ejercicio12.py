numero = int(input("Ingrese un número entero: "))

if numero % 3 == 0 and numero % 5 == 0 and numero % 7 == 0:
    print("Es divisible entre 3, 5 y 7.")
else:
    print("No es divisible entre los tres números.")