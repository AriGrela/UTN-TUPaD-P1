numero = int(input("Ingresa un número: "))
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

print("El número invertido es:", invertido)