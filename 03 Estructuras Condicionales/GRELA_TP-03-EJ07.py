palabra = input("Ingrese una frase o palabra: ")
vocales = ["a","e","i","o","u","A","E","I","O","U"]

if palabra[-1] in vocales:
    print (f"{palabra}!")
else:
    print (f"{palabra}")



