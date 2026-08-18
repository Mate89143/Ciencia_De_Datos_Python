a = float(input("Ingrese la primera longitud: "))
b = float(input("Ingrese la segunda longitud: "))
c = float(input("Ingrese la tercera longitud: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Es un triángulo equilátero.")
    elif a == b or a == c or b == c:
        print("Es un triángulo isósceles.")
    else:
        print("Es un triángulo escaleno.")
else:
    print("No forman un triángulo.")