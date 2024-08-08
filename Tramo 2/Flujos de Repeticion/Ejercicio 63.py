viajes_cortos = 0
viajes_medianos = 0
viajes_largos = 0
recaudacion_total = 0
total_viajes = 0

dia_terminado = False

while total_viajes < 30 and not dia_terminado:
    categoria = input("Ingrese la categoría del viaje (C para corto, M para mediano, L para largo, Z para finalizar): ").upper()
    
    if categoria == 'Z':
        dia_terminado = True
        continue
    
    if categoria not in ['C', 'M', 'L']:
        print("Categoría inválida. Intente de nuevo.")
        continue
    
    distancia = float(input("Ingrese la distancia recorrida (en kilómetros): "))
    
    cantidad_pasajeros = int(input("Ingrese la cantidad de pasajeros (1-3): "))
    while cantidad_pasajeros <= 0 or cantidad_pasajeros >= 4:
        print("Cantidad de pasajeros inválida. Debe ser mayor a 0 y menor a 4.")
        cantidad_pasajeros = int(input("Ingrese la cantidad de pasajeros (1-3): "))
    
    importe = float(input("Ingrese el importe a cobrar (incluyendo el costo básico de $180): "))
    while importe < 180:
        print("Importe inválido. Debe ser al menos $180.")
        importe = float(input("Ingrese el importe a cobrar (incluyendo el costo básico de $180): "))
    
    importe_basico = 180
    recargo = importe - importe_basico
    
    mayor_edad = 0
    nombre_mayor = ""
    
    for _ in range(cantidad_pasajeros):
        nombre = input("Ingrese el nombre del pasajero: ")
        edad = int(input("Ingrese la edad del pasajero (18-119): "))
        while edad <= 18 or edad >= 120:
            print("Edad inválida. Debe ser mayor a 18 y menor a 120.")
            edad = int(input("Ingrese la edad del pasajero (18-119): "))
        
        if edad > mayor_edad:
            mayor_edad = edad
            nombre_mayor = nombre
    
    print("La persona más grande del viaje es:", nombre_mayor, "con", mayor_edad, "años.")
    
    if categoria == 'C':
        viajes_cortos += 1
    elif categoria == 'M':
        viajes_medianos += 1
    elif categoria == 'L':
        viajes_largos += 1
    
    recaudacion_total += importe
    total_viajes += 1

valor_promedio_viaje = recaudacion_total / total_viajes if total_viajes > 0 else 0
porcentaje_viajes_cortos = (viajes_cortos / total_viajes * 100) if total_viajes > 0 else 0

print("Cantidad de viajes cortos (C):", viajes_cortos)
print("Cantidad de viajes medianos (M):", viajes_medianos)
print("Cantidad de viajes largos (L):", viajes_largos)
print("Recaudación total: $", round(recaudacion_total, 2))
print("Valor promedio del viaje: $", round(valor_promedio_viaje, 2))
print("Porcentaje de viajes cortos: %.2f%%" % porcentaje_viajes_cortos)
