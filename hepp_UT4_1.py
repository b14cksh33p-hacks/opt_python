# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Ejercicio 1 Realizar un programa que defina una lista llamada “lista_numeros” de 10 enteros, a continuación, la inicialice con valores aleatorios (del 1 al 10)
# y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado (el número al cuadrado).

import random

list_num = [random.randint(1, 10) for _ in range(10)]

for num in list_num:
    print(f"{num} - {num**2}")