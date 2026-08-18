import pandas as pd

temperaturas = pd.Series([
    22, 24, 21, 25, 23,
    26, 27, 22, 24, 28,
    25, 23, 29, 26, 24
])

promedio = temperaturas.mean()
maxima = temperaturas.max()
minima = temperaturas.min()

dias_superiores = temperaturas[temperaturas > promedio]
cantidad_superiores = len(dias_superiores)

print("Temperaturas:")
print(temperaturas)

print("\nTemperatura promedio:", promedio)
print("Temperatura máxima:", maxima)
print("Temperatura mínima:", minima)

print("\nDías con temperatura superior al promedio:")
print(dias_superiores)

print("Cantidad de días superiores al promedio:", cantidad_superiores)