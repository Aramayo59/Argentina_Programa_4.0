
sueldo_fijo = float(input("Ingrese el sueldo fijo del vendedor: "))
porcentaje_comision = float(input("Ingrese el porcentaje de comisión (en %): "))

monto_ventas = float(input("Ingrese el monto total de ventas realizadas durante el mes: "))

comision = monto_ventas * (porcentaje_comision / 100)

importe_total = sueldo_fijo + comision

print("El importe total a cobrar por el vendedor es: $" + str(round(importe_total, 2)))
