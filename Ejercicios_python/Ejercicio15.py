cadena = input("Ingrese una cadena: ")

cadena_limpia = cadena.replace(" ", "").lower()
if cadena_limpia == cadena_limpia[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")