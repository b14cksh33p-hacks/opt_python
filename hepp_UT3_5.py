# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Escribe un programa que pida un nombre de usuario y una contraseña. 
# Si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

user = str(input("Por favor, introduzca su nombre de usuario: "))

password = str(input("Por favor, introduzca su contraseña: "))

if user == "pepe" and password == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error de autenticación.")