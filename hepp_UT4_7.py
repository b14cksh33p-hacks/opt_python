# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Programa que cree 2 listas de cinco enteros cada una, y pida sus valores por teclado. 
# A continuación, debe unir las 2 listas en una lista resultado e imprimir sus valores.

lista1 = []
lista2 = []

for i in range(5):
    valor = int(input("Por favor dame un valor: "))
    lista1.append(valor)

for i in range(5):
    valor2 = int(input("Dame más valores por favor: "))
    lista2.append(valor2)

lista_final = lista1 + lista2
print(lista_final)