# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario,
# el programa termina cuando se introduce un espacio.

while True:
    entrada = input("Introduce un carácter (espacio para terminar): ")

    # Si está vacío (solo Enter), volvemos a pedir
    if entrada == " ":
        break

    if entrada in 'aeiouAEIOU':
        print("Vocal")
    else:
        print("NO VOCAL")