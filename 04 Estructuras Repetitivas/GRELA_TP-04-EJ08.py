pares = impares = negativos = positivos = 0

for i in range(100):
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")