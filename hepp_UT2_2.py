# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Solicita al usuario su nombre, su apellido y su ciudad de nacimiento. Concaténalos en una sola cadena utilizando f-strings con el formato:
# "Hola, mi nombre es Nombre Apellido y nací en Ciudad." Imprime el resultado.

nombre = str(input("Por favor, introduzca su nombre: "))
apellido = str(input("Por favor, introduzca su apellido: "))
ciudad = str(input("Por favor, introdusca su ciudad de nacimiento: "))

print(f"Hola, mi nombre es {nombre} {apellido} y nací en {ciudad}.")