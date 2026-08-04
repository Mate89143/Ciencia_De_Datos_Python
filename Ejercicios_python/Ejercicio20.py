a = int(input("Primer número: "))
b = int(input("Segundo número: "))
if b != 0 and a % b == 0:
    print("El segundo número es un factor del primero.")
else:
    print("El segundo número no es un factor del primero (o es cero).")