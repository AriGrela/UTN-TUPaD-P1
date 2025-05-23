import utilidades

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = utilidades.calcular_imc(peso,altura)

print (f"Su IMC es: {round(imc,2)}")


