# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

numero1 = int(input("Por favor introduzca el primer número: "))

numero2 = int(input("Por favor introduzca el segundo número: "))

numero3 = int(input("Por favor introduzca el tercer número: "))

numeros = [numero1, numero2, numero3]

numeros.sort(reverse=True)
print(numeros)