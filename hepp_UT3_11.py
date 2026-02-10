# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación,
# va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos 
# que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos 
# intentos lo has acertado), si se llega al límite de intentos te muestra el número que había generado.

import random

num_aleatorio = random.randint(1, 100)
intentos_max = 10
intentos = 0

print("Adivina el número entre 1 y 100. Tienes 10 intentos.")

while intentos < intentos_max:
    intentos += 1
    num_introducido = int(input(f"Intento {intentos}/{intentos_max}. Introduce un número: "))

    if num_introducido < num_aleatorio:
        print("El número es mayor.")
    elif num_introducido > num_aleatorio:
        print("El número es menor.")
    else:
        print(f"¡Felicidades! Has acertado el número {num_aleatorio} en {intentos} intentos.")
        break
else:
    print(f"Has agotado los {intentos_max} intentos. El número era {num_aleatorio}.")