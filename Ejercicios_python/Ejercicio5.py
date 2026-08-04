ancho = input("Ingrese el ancho del rectangulo: ")
alto = input("Ingrese el alto del rectangulo: ")

area = float(ancho) * float(alto)

if area > 100:
    print("El área del rectángulo es mayor a 100.")
else:
    print("El área del rectángulo es menor o igual a 100.")
