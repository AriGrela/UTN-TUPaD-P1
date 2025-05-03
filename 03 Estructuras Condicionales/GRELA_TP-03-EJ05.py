while True:
    edad = (input("Ingrese su contraseña: "))
    if len(edad) >= 8 and len(edad) <= 14:
         print ("Ha ingresado una contraseña correcta")
         break
    else:
        print ("Ingrese una contraseña de entre 8 y 14 caracteres:")

