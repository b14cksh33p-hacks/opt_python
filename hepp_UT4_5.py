# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Hacer un programa que inicialice una lista de números con valores aleatorios,
# y posteriormente ordene los elementos de menor a mayor.

from random import randint

lista = []

for i in range(5):
    valor = randint(1, 100)
    lista.append(valor)

print("Lista original:", lista)

lista.sort()

print("Lista ordenada:", lista)
