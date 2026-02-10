# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10, pueden 
# contener decimales). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

lista_notas = []

for i in range (5):
    nota = float(input("Introduce las notas: "))
    lista_notas.append(nota)

suma_notas = sum(lista_notas)
nota_media = suma_notas/5
nota_maxima = max(lista_notas)
nota_minima = min(lista_notas)
print(f"Las notas son las siguientes {lista_notas} \n La nota media es {nota_media} \n La nota máxima es {nota_maxima} \n La nota mínima es {nota_minima}")