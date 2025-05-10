inicio = int(input("Ingresa el valor inicial: "))
fin = int(input("Ingresa el valor final: "))
suma = 0

for i in range(inicio + 1, fin):
    suma += i

print("La suma es:", suma)