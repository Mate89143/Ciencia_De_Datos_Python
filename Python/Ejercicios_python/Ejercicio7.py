palabra=(input("Ingrese una palabra: "))
vocales = "aeiouAEIOU"

if any(vocal in palabra for vocal in vocales):
    print("La palabra contiene al menos dos vocales.")
else:
    print("La palabra no contiene vocales.")