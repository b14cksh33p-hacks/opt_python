# Ejercicio realizado por Heiko Hepp (B14cksh33p)

precio_cena = float(input("Ingrese el precio de la cena: €"))

# Calcula el 10% de propina y muestralo

propina = precio_cena * 0.10
print(f"La propina es: €{propina:}")

precio_final = precio_cena + propina
print(f"El precio final es: €{precio_final:}")
