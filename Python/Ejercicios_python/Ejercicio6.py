numero = float(input("Ingrese un numero: "))
digitos = len(str(abs(int(numero))))
print("El numero tiene", digitos, "digitos.")

if digitos % 2 == 0:
    print("El numero tiene un numero par de digitos.")
else:
    print("El numero tiene un numero impar de digitos.")