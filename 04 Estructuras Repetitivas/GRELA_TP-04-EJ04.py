total = 0
while True:
    numero = int(input("Ingresa un número (0 para detenerse): "))
    if numero == 0:
        break
    total += numero

print("El total acumulado es:", total)