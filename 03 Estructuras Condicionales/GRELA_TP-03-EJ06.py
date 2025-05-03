from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

m_media = mean(numeros_aleatorios)
m_mediana = median(numeros_aleatorios)
m_moda = mode(numeros_aleatorios)

print(f"Media: {m_media}, Mediana: {m_mediana}, Moda: {m_moda}")

if m_media > m_mediana > m_moda:
    print("Hay sesgo positivo")
elif m_media < m_mediana < m_moda:
    print("Hay sesgo negativo")
elif m_media == m_mediana == m_moda:
    print("No hay sesgo")
else:
    print("No se puede determinar un sesgo claro.")
