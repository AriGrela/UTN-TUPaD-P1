import math

def saludo_mundo():
    print("Hola Mundo")

def saludar_usuario(nombre):
   print(f"Hola {nombre}! ")

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    return math.pi * (radio **  2) 

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
    
def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1,11):
        print (i * numero)

def operaciones_basicas(a,b):
   mi_tupla = ((a+b),(a-b),(a*b),(a/b))
   return mi_tupla

def calcular_imc(peso, altura):
    return peso / (altura**2)

def celsius_a_farenheit(celcius):
    return (celcius * (9/5)) + 32

def calcular_promedio(a,b,c):
    return ((a+b+c)/3)

