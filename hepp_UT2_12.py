# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Pide al usuario que escriba el nombre de su asignatura favorita, su número de créditos y su calificación. Muestra un mensaje como este usando un f-string:
# Mi asignatura favorita es [asignatura], tiene [créditos] créditos y obtuve una calificación de [calificación].

asignatura = str(input("Por favor, ingrese su asignatura favorita: "))
creditos = int(input("Ingrese los créditos de la asignatura: "))
calificacion = float(input("Ingrese la calificación obtenida: "))

print(f"Mi asignatura favorita es {asignatura}, tiene {creditos} y obtuve una calificación de {calificacion}.")