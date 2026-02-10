# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Algoritmo que pida números hasta que se introduzca un cero.
# Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
contador = 0

while True:
    numero = float(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"Suma de los números: {suma}")
    print(f"Media de los números: {media}")
else:
    print("No se introdujeron números.")