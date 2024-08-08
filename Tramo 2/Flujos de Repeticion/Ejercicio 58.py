def calcular_precio(cantidad, precio_base):
    if cantidad <= 12:
        total = cantidad * precio_base
        descuento_aplicado = "Ninguno"
    elif cantidad <= 100:
        total = (12 * precio_base) + ((cantidad - 12) * (precio_base * 0.9))
        descuento_aplicado = "10%"
    else:
        total = (12 * precio_base) + (88 * (precio_base * 0.9)) + ((cantidad - 100) * (precio_base * 0.75))
        descuento_aplicado = "10% y 25%"
    
    precio_promedio = total / cantidad
    return total, precio_promedio, descuento_aplicado


total_ventas = 0
ventas_con_10_descuento = 0
ventas_sin_descuento = 0

cantidad = 0

while cantidad != -1:
    cantidad = int(input("Ingrese la cantidad solicitada de un producto (-1 para finalizar): "))
    
    if cantidad == -1:
        break

    precio_base = float(input("Ingrese el precio base del producto: "))
    
    total, precio_promedio, descuento_aplicado = calcular_precio(cantidad, precio_base)
    
    print("Valor total de la venta: %.2f" % total)
    print("Precio promedio por unidad: %.2f" % precio_promedio)
    
  
    total_ventas += 1
    
    if descuento_aplicado == "10%":
        ventas_con_10_descuento += 1
    elif descuento_aplicado == "Ninguno":
        ventas_sin_descuento += 1


print("")
print("Informe final:")
print("a- Cantidad de ventas realizadas total: %d" % total_ventas)
print("b- Cantidad de ventas que se aplicaron un 10% de descuento: %d" % ventas_con_10_descuento)
print("c- Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos: %d" % ventas_sin_descuento)
