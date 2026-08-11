import numpy as np

# Ejercicio 10: Dashboard estadístico

print("Dashboard estadístico")

# Función para calcular estadísticas de una matriz
def dashboard(matriz):
    
    if not isinstance(matriz, np.ndarray):
        matriz = np.array(matriz)

    # Calcular dimensiones
    dimension = matriz.ndim
    filas, columnas = matriz.shape
    total_datos = matriz.size

    # Calcular estadísticas
    maximo = np.max(matriz)
    minimo = np.min(matriz)
    promedio = np.mean(matriz)
    mediana = np.median(matriz)
    varianza = np.var(matriz)
    desviacion_estandar = np.std(matriz)

    # Imprimir resultados
    print(f"Dimensiones de la matriz: {dimension}")
    print(f"Filas: {filas}")
    print(f"Columnas: {columnas}")
    print(f"Total de datos: {total_datos}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Desviación estándar: {desviacion_estandar:.2f}")

# Ejemplo de uso
matriz_ejemplo = np.array([[1, 2, 3], [4, 5, 6]])
dashboard(matriz_ejemplo)