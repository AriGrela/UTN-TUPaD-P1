from EjemplosyUtilidades import fibonacci_recursivo as fibonacci

num = int(input("Ingresa una posicion para indicar el numero fibonacci: "))
print(f"Su numero Fibonacci es: {fibonacci(num)}")

for i in range(num+1):
    print(f"Los numeros Fibonacci hasta su posicion son:{fibonacci(i)} ")
