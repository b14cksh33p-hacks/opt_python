# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Crea un algoritmo que pida un número y diga si es positivo, negativo o 0.

numero = int(input("Por favor, introduzca un número: "))

if numero < 0:
    print("El número introducido es menor que cero.")
elif numero == 0:
    print("El número introducido es igual a 0.")
else:
    print("El número introducido es mayor que 0.")