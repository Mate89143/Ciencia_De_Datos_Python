import numpy as np

numeros = np.arange(1, 101)
print("Primeros 10 números:", numeros[:10])

suma = np.sum(numeros)

promedio = np.mean(numeros)

desviacion = np.std(numeros)

varianza = np.var(numeros)

mediana = np.median(numeros)

print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Desviación estándar: {desviacion}")
print(f"Varianza: {varianza}")
print(f"Mediana: {mediana}")