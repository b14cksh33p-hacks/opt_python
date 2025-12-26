# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Solicita al usuario que ingrese una frase. Luego:
# 1. Extrae e imprime los primeros 10 caracteres de la frase.

frase = str(input("Por favor, ingrese una frase: "))
print(frase[0:10])

# 2. Extrae e imprime los últimos 10 caracteres.

print(frase[-10:])

# 3. Muestra todos los caracteres desde la posición 5 hasta la posición 15.

print(frase[5:15])

# 4. Imprime la frase en orden inverso.

print(frase[::-1])