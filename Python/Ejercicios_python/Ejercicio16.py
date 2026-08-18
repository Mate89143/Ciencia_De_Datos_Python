numero = input("Ingrese un número entero: ")
frecuencias = {}
for d in numero:
    frecuencias[d] = frecuencias.get(d, 0) + 1
if 2 in frecuencias.values():
    print("Tiene exactamente dos dígitos iguales.")
else:
    print("No tiene exactamente dos dígitos iguales.")