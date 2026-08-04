contrasena = input("Ingrese una contraseña: ")
if len(contrasena) < 8:
    print("La contraseña es débil. Debe tener al menos 8 caracteres.")
if not any(c.isdigit() for c in contrasena):
    print("La contraseña es débil. Debe contener al menos un número.")
if not any(c.isupper() for c in contrasena):
    print("La contraseña es débil. Debe contener al menos una letra mayúscula.")
if not any(c.islower() for c in contrasena):
    print("La contraseña es débil. Debe contener al menos una letra minúscula.") 
if len(contrasena) >= 8 and any(c.isdigit() for c in contrasena) and any(c.isupper() for c in contrasena) and any(c.islower() for c in contrasena):
    print("La contraseña es fuerte.")


