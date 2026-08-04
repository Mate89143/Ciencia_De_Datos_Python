import numpy as np

# Ejercicio 6: Procesamiento de imágenes

print ("Procesamiento de imágenes")

# Función para crear una imagen aleatoria de 15x15 píxeles
def crear_imagen():
    
    return np.random.randint(0, 256, size=(15, 15))

# Función para incrementar el brillo de la imagen
def incrementar_brillo(imagen, valor=50):
    
    return np.clip(imagen + valor, 0, 255)

# Función para disminuir el brillo de la imagen
def disminuir_brillo(imagen, valor=50):
    
    return np.clip(imagen - valor, 0, 255)

# Función para invertir los colores de la imagen
def invertir_colores(imagen):
    
    return 255 - imagen

# Función para obtener la imagen transpuesta
def imagen_transpuesta(imagen):
    
    return np.transpose(imagen)

# Función para obtener la imagen y sus transformaciones
def obtener_imagen():
    img = crear_imagen()
    print("Imagen original (15x15 píxeles):")
    print(img)

# Aplicar transformaciones
    img_brillo_inc = incrementar_brillo(img)
    img_brillo_dec = disminuir_brillo(img)
    img_invertida = invertir_colores(img)
    img_transpuesta = imagen_transpuesta(img)

    return img, img_brillo_inc, img_brillo_dec, img_invertida, img_transpuesta

# Obtener la imagen y sus transformaciones
img, img_brillo_inc, img_brillo_dec, img_invertida, img_transpuesta = obtener_imagen()

print("\nImagen con brillo incrementado:")
print(img_brillo_inc)
print("\nImagen con brillo disminuido:")
print(img_brillo_dec)
print("\nImagen con colores invertidos:")
print(img_invertida)
print("\nImagen transpuesta:")
print(img_transpuesta)
