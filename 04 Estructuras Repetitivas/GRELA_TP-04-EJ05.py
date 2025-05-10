import random

numero_aleatorio = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        adivinado = True

print(f"¡Adivinaste el número en {intentos} intentos!")