from EjemplosyUtilidades import funcion_potencia

base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))

resultado = funcion_potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")
