import numpy as np

np.argmax([10, 20, 15])
# Devuelve el índice (posición) del valor máximo. En este caso, el máximo es 20 en la posición 1.

np.argmin([10, 20, 15])
# Devuelve el índice del valor mínimo. El mínimo es 10 en la posición 0.

np.unique([1, 2, 2, 3], return_counts=True)
# Encuentra valores únicos y sus frecuencias. Devuelve (array([1,2,3]), array([1,2,1])): el 1 aparece 1 vez, el 2 dos veces, el 3 una vez.

np.sort([3, 1, 2])
# Ordena el arreglo en orden ascendente. Resultado: [1, 2, 3].

np.where([1, 0, 2, 0] == 0)
# Devuelve los índices donde la condición es verdadera. Aquí, los ceros están en las posiciones 1 y 3.

np.clip([-5, 0, 300], 0, 255)
# Limita los valores al intervalo [0, 255]. Los menores a 0 se convierten en 0, los mayores a 255 en 255. Resultado: [0, 0, 255].

np.concatenate([[1, 2], [3, 4]])
# Concatena arreglos a lo largo del eje 0 (filas). Resultado: [1, 2, 3, 4].

np.vstack([[1, 2], [3, 4]])
# Apila arreglos verticalmente (uno debajo de otro). Resultado: [[1, 2], [3, 4]].

np.hstack([[1, 2], [3, 4]])
# Apila arreglos horizontalmente (uno al lado del otro). Resultado: [1, 2, 3, 4].

np.random.randint(0, 10, size=5)
# Genera 5 enteros aleatorios entre 0 (incluido) y 10 (excluido). Ejemplo: [5, 2, 9, 1, 7].

np.random.uniform(0, 1, size=3)
# Genera 3 flotantes aleatorios con distribución uniforme entre 0 y 1. Ejemplo: [0.23, 0.76, 0.44].

np.arange(6).reshape(2, 3)
# Cambia la forma de un arreglo de 6 elementos a una matriz de 2 filas y 3 columnas. Resultado: [[0,1,2], [3,4,5]].

np.array([[1, 2], [3, 4]]).T
# Transpone la matriz (intercambia filas por columnas). Resultado: [[1, 3], [2, 4]].

np.array([[1, 2], [3, 4]]).flatten()
# Aplana la matriz a una sola dimensión (copia). Resultado: [1, 2, 3, 4].

np.array([[1, 2], [3, 4]]).ravel()
# Aplana la matriz a una sola dimensión (vista, más eficiente). Resultado: [1, 2, 3, 4].

np.eye(3)
# Crea una matriz identidad de 3x3 (unos en la diagonal principal, ceros fuera). Resultado: [[1,0,0],[0,1,0],[0,0,1]].

np.diag([1, 2, 3])
# Crea una matriz diagonal con los elementos del arreglo en la diagonal principal. Resultado: [[1,0,0],[0,2,0],[0,0,3]].

np.linspace(0, 10, 5)
# Genera 5 números espaciados linealmente entre 0 y 10 (ambos incluidos). Resultado: [0.0, 2.5, 5.0, 7.5, 10.0].

np.meshgrid([1, 2, 3], [4, 5])
# Crea matrices de coordenadas a partir de vectores. Devuelve dos matrices: X e Y, donde X tiene las filas repetidas y Y las columnas repetidas.