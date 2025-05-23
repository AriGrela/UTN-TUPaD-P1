import utilidades

radio = float(input("Escriba el radio: "))

area = utilidades.calcular_area_circulo(radio)
perimetro = utilidades.calcular_perimetro_circulo(radio)

print(f"Su area es: {area} y su perimetro es: {perimetro}")

