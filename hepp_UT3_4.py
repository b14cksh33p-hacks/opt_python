# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
# o un mensaje de aviso en caso contrario.

numero1 = int(input("Por favor, introduzca el primer número: "))

numero2 = int(input("Por favor, introduzca el segundo número: "))

if numero2 != 0:
    division = numero1 / numero2
    print(f"La división de {numero1} entre {numero2} es: {division}")
else:
    print("Error: No se puede dividir entre cero.")