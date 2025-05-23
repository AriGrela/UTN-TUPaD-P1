#Pasando una lista de numeros,
#obtener la suma total de los mismos de forma recursiva

def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0]+sum_list(lst[1:])
    

#Realizar una funcion recursiva que reciba un numero y una frase y la 
#repita el numero de veces ingresado.

def repetir_frase(num,frase):
    if num >= 1:
        print(frase)
        repetir_frase(num-1,frase)


#Realicemos la suma de los primeros n valores positivos de forma recursiva

def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num+ suma_recursiva(num-1)
    
#Calcula el valor de Fibonacci en la posicion dada de forma recursiva.
# :param pos: Posicion en la secuencia de Fibonacci ( debe ser >= 0).
# :return: Valor de Fibonacci en la posicion indicada.

def fibonacci_recursivo(posicion):
    if posicion==0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1)+fibonacci_recursivo(posicion-2)
    

#Realizar una funcion recursiva que permita sumar los n valores primos
#Para n=35, los divisores son 2,3,4,6,9,12,18 y basta comprobar hasta
# 36=sqrt{36} = 6. Esto significa que si no encontramos divisores de n
# menores o iguales a la raiz cuadrada de su numero, entonces n es primo.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range (2, int(numero**0.5) + 1): # numero**0.5 es la raiz cuadrada
         if numero % i == 0:
             return False
         return True
    
def sum_n_primos(num):
    if num==1:
        return 0 
    elif es_primo(num):
        return num+sum_n_primos(num-1)
    else:
        return sum_n_primos(num-1)


##################################################################################################################################    


#Ejercicios

#Ej 01 - Calcular el Factorial de un Numero de forma recursiva

def calculador_factorial(num):
    if num == 0:
        return 1 
    else:
       return  num * calculador_factorial(num-1)
    
#Ej 02 - Calcular valor serie Fibonacci 

def fibonacci_recursivo(posicion):
    if posicion==0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1)+fibonacci_recursivo(posicion-2)
    
#Ej 03 - Calcular potencia de un numero elevado a un exponente

def funcion_potencia(base,exponente):
    if exponente==0:
        return 1
    elif exponente> 0:
        return base * funcion_potencia(base, exponente-1)
    else:
        return 1 / funcion_potencia(base, -exponente)

#Ej 04 - Numero en binario

def numero_en_binario_base10(num):
    if num  == 0:
        return ""
    else:
        return numero_en_binario_base10(num//2) + str(num % 2)
    
#Ej 05 - Es palindromo?

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#Ej 06 - Sumar digitos

def sumar_digitos(n):
    if n == 0:               
        return 0             
    else:
        return (n % 10) + sumar_digitos(n // 10)
    
#Ej 07 - Piramiodes con Bloques

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)
    

#Ej 08 - Contar Digitos

def contar_digitos(num,digito):
    if num == 0:
        return 0
    elif num % 10 == digito:
        return 1 + contar_digitos(num//10,digito)
    else:
        return contar_digitos(num//10,digito)




    
    



    

    