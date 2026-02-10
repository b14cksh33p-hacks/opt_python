# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Programa que pida números y los añada a una lista hasta que llegue a 10 elementos
# o se introduzca un número negativo. A continuación, se debe imprimir la lista.

numeros = []
while len(numeros) < 10:
    try:
        num = float(input("Introduce un número: "))
        if num < 0:
            break
        numeros.append(num)
    except ValueError:
        print("Por favor, introduce un número válido.")

print("Lista de números:", numeros)