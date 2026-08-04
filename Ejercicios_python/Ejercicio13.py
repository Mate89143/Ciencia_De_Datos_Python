numero = (input("Ingrese un número: "))

if len(set(numero)) < len(numero):
    print("Tiene dígitos repetidos.")
else:
    print("No tiene dígitos repetidos.")