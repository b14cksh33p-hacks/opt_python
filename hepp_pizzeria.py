# Ejercicio reallizado por Heiko Hepp (B14cksh33p)

# Hay una pizzería donde cada pizza vale 5€. Enviar una pizza a casa vale 2€ por pizza. 
# Existe la opción de pagar una tarifa plana de envío de 9€.
# Haz un programa que le pida al usuario cuantas pizzas quiere y le dé dos precios,
# uno con la opción 1 (envío de 2€/pizza) y otro con la opción 2 (tarifa plana de envío por 9€)

pizza = 5
envio1 = 2
tarifa_plana = 9

pedido = int(input("Por favor diga cuantas pizzas desea: "))
print("El envío a casa son 2€ por pizza. También existe la opción de pagar una tarifa plana de envío de 9€. \nIntroduzca el 1 para la opción de 2€ por pizza, o introduzca en 2 para la tarifa plana de ")
seleccion_envio = int(input("Por favor introduzca el número correspondiente a su opción de envío: "))

if seleccion_envio == 1:
    total1 = pedido * (pizza + envio1)
    print("El precio de su pedido asciende a : ", total1, "€")

elif seleccion_envio == 2:
    total2 = pedido * pizza + tarifa_plana
    print("El precio de su pedido asciende a: ", total2, "€")

else:
    print("Por favor, repita el pedido y seleccione una opción de envío válida. Gracias")
