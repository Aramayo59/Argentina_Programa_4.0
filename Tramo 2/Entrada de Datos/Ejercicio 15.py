
SALARIO_BASE = 1000            
COMISION_FIJA_POR_VENTA = 50   
PORCENTAJE_COMISION = 0.05      

nombre_vendedor = input("Ingrese el nombre del vendedor: ")
cantidad_ventas = int(input("Ingrese la cantidad de ventas realizadas: "))
valor_total_ventas = float(input("Ingrese el valor total de las ventas realizadas: "))

comision_fija_total = cantidad_ventas * COMISION_FIJA_POR_VENTA
comision_porcentaje = valor_total_ventas * PORCENTAJE_COMISION

salario_total = SALARIO_BASE + comision_fija_total + comision_porcentaje

print("Nombre del vendedor:", nombre_vendedor)
print("Salario total correspondiente:", round(salario_total, 2))
