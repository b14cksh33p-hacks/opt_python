# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Pide al usuario que escriba una palabra y un número. Imprime la palabra repetida el número de veces indicado.

palabra = str(input("Por favor, escriba una palabra: "))
numero = int(input("Por favor, introduzca un número: "))

print(', '.join([palabra] * numero))