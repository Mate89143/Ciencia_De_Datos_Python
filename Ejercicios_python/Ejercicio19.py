cadena = (input("Ingrese una cadena: "))
vocales_minúsculas = "aeiou"
vocales_mayúsculas = "AEIOU"
if all(vocal in cadena for vocal in vocales_minúsculas) or all(vocal in cadena for vocal in vocales_mayúsculas):
    print("La cadena contiene todas las vocales.")
else:
    print("La cadena no contiene todas las vocales.")
