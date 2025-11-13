# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Tu edad en 2030
# Pide la edad actual al usuario. Calcula cuántos años tendrá en 2030 y muéstralo.

from datetime import datetime

edad = int(input("Por favor ingrese su edad: "))
año_actual = datetime.now().year
edad_2030 = edad + (2030 - año_actual)
print("En el año 2030 tendrás", edad_2030, "años.")