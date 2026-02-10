# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Crea un programa que pida un número de mes al usuario (por ejemplo, el 4, que sería abril) y diga cuántos días tiene
# (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.
# Controla con un bucle while que el número de mes esté en 1 y 12.

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        num_mes = int(input("Introduce el número del mes (1-12): "))
        if 1 <= num_mes <= 12:
            break
        else:
            print("Número de mes inválido. Debe estar entre 1 y 12.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

indice = num_mes - 1
print(f"El mes {num_mes} es {meses[indice]} y tiene {dias[indice]} días.")