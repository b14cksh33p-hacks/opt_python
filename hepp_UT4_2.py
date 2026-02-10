# # Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Crea una lista de 5 elementos donde cada elemento sea una cadena que se pide por el teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, y muéstralo por la pantalla.

lista1 = []

for i in range(5):
    texto = str(input("Dime una ciudad: "))
    lista1.append(texto)

lista2 = lista1[::-1]
print(lista2)