import utilidades

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

operaciones = utilidades.operaciones_basicas(num1,num2)

print (f"El resultado de su suma es: {operaciones[0]} ")
print (f"El resultado de su resta es: {operaciones[1]} ")
print (f"El resultado de su multiplicacion es: {operaciones[2]} ")
print (f"El resultado de su division es: {operaciones[3]} ")