numero = int(input("Ingresa un número entero: "))
contador = 0

while numero != 0:
    numero //= 10
    contador += 1

print("La cantidad de dígitos es:", contador)