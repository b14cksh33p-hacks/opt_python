# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número
#  y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).

numero = int(input("Por favor introduzca un número: "))

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")