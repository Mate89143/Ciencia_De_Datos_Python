palabra = input("Ingrese una palabra: ").lower()
vocales = 0
consonantes = 0
for letra in palabra:
    if letra.isalpha():
        if letra in "aeiou":
            vocales += 1
        else:
            consonantes += 1
if vocales == consonantes:
    print("Tiene la misma cantidad de vocales y consonantes.")
else:
    print("No tiene la misma cantidad.")