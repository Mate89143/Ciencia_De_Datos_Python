frase = (input("Ingrese una frase: "))

if frase.endswith("!"):
    print("La frase termina con un signo de exclamación.")
elif frase.endswith("?"):
    print("La frase termina con un signo de interrogación.")
else:
    print("La frase no termina con un signo de exclamación.")
    