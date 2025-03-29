#Ejercicio 1


print("Hola Mundo")


#Ejercicio 2


nombre = input("Ingrese su nombre")
print (f"Hola {nombre}")


#Ejercicio 3


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input ("Ingrese su lugar de residencia: ")


print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4


import math
radio = float(input("Ingrese el radio de un circulo:"))




area = math.pi * (radio ** 2)
perimetro = math.pi * radio * 2


print(f"Su area es:{area} y su perimetro es: {perimetro}")

#Ejercicio 5


segundos = float(input("Ingrese una cantidad de segundos: "))


print(f"Su tiempo en horas es: {segundos/3600}")

#Ejercicio 6


numero = int(input("Ingrese el número del cual quiere obtener la tabla de multiplicar => "))


for factor in range(10):
    print(f"{numero} X {factor} = {factor*numero}")

#Ejercicio 7


num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))


print (f"Su multiplicación es: {num1*num2}")
print (f"Su resta es: {num1-num2}")
print (f"Su suma es: {num1+num2}")
print (f"Su división es: {num1/num2}")


#Ejercicio 8


altura = float(input("Introduzca su altura: "))
peso =  float(input("Introduzca su peso: "))


print(f"Su IMC es: {peso/(altura**2)}")


#Ejercicio 9


temp = float(input("Ingrese una temperatura en Celcius: "))
print (f"Su temperatura en Farenheit es {(temp*1.8)+32}")


#Ejercicio 10


n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
n3 = int(input("Ingrese un ultimo numero: "))


print(f"El promedio de los tres numeros es: {(n1+n2+n3)/3}")