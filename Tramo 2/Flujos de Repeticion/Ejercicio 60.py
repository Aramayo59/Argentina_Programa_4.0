
suma_sueldos_nuevos = 0
cantidad_empleados = 0

continuar = "S"

while continuar == "S":
   
    numero_empleado = input("Ingrese el número de empleado: ")
    sueldo_basico = float(input("Ingrese el sueldo básico: "))
    antiguedad = int(input("Ingrese la antigüedad (en años): "))
    cantidad_hijos = int(input("Ingrese la cantidad de hijos: "))
    estudios_superiores = input("Posee estudios superiores (S/N): ").upper()
    
   
    aumento = 0

    if antiguedad > 10:
        aumento += 0.10  

    if cantidad_hijos > 2:
        aumento += 0.10 
    elif cantidad_hijos == 1:
        aumento += 0.05  

    if estudios_superiores == 'S':
        aumento += 0.05  

    
    sueldo_nuevo = sueldo_basico * (1 + aumento)
    
    
    print("\nEmpleado Nº", numero_empleado)
    print("Sueldo Básico: $", round(sueldo_basico, 2))
    print("Nuevo Sueldo: $", round(sueldo_nuevo, 2), "\n")
    
   
    suma_sueldos_nuevos += sueldo_nuevo
    cantidad_empleados += 1
    
    
    continuar = input("¿Desea ingresar otro empleado? (S/N): ").upper()


if cantidad_empleados > 0:
    sueldo_nuevo_promedio = suma_sueldos_nuevos / cantidad_empleados
    print("\nSueldo nuevo promedio de la empresa: $", round(sueldo_nuevo_promedio, 2))
else:
    print("No se ingresaron empleados.")
