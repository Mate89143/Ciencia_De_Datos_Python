texto = input("Ingrese una cadena: ")
if any(c.isdigit() for c in texto):
    print("Contiene al menos un número.")
else:
    print("No contiene números.")