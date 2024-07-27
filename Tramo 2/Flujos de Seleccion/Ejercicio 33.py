
importe = float(input("Ingrese el importe de la compra: $"))


descuento = 0


if importe > 10000:
    descuento = 0.105 * importe

if 5500 <= importe <= 10000:
    descuento = 0.08 * importe

if importe < 5500:
    descuento = 0.045 * importe


precio_neto = importe - descuento

print("El descuento aplicado es: $" + str(round(descuento, 2)))
print("El precio neto a cobrar es: $" + str(round(precio_neto, 2)))
