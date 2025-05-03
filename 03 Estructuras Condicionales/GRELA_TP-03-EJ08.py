nombre = input("Ingrese su nombre: ")
definicion = int(input("Si quiere su nombre en mayusculas ingrese 1, en minusculas ingrese 2, si solo quiere su primera letra en mayuscula ingrese 3: "))

if definicion == 1:
    print (nombre.upper())
elif definicion == 2:
    print (nombre.lower())
elif definicion == 3:
    print (nombre.title())
else:
    print ("No ingreso un numero correcto")



