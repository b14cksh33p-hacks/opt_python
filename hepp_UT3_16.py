# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

numero = int(input("Introduce un número: "))

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")