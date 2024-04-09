def password():
    while True:
        contrasena = input("Ingrese la contraseña: ")
        if contrasena == "1234":
            print("¡Bienvenido Usuario!")
            break
        else:
            print("Contraseña incorrecta. Intente de nuevo.")

password()
