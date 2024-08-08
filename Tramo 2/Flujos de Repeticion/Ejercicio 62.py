
total_tiempo = 0
apto = 1 
tiempo_menor_15 = 0 
mejor_tiempo = 100 
dia_mejor_tiempo = 0


dia = 1
while dia <= 10:
    tiempo = int(input("Ingrese el tiempo (en minutos) del día " + str(dia) + ": "))
    
   
    if tiempo <= 0 or tiempo >= 100:
        print("Tiempo inválido. Debe ser un entero mayor que 0 y menor a 100.")
        apto = 0 
        dia = 11  
    else:
        
        total_tiempo += tiempo
        
        
        if tiempo > 20:
            apto = 0  
        if tiempo < 15:
            tiempo_menor_15 = 1  
        if tiempo < mejor_tiempo:
            mejor_tiempo = tiempo
            dia_mejor_tiempo = dia
    
        dia += 1 


if dia > 10:  
    promedio = total_tiempo / 10
else:
    promedio = 0


if apto == 1 and tiempo_menor_15 == 1 and promedio <= 18:
    print("El atleta es apto para la prueba.")
    print("Promedio de tiempo: " + str(round(promedio, 2)) + " minutos")
    print("Mejor tiempo: " + str(mejor_tiempo) + " minutos en el día " + str(dia_mejor_tiempo))
else:
    print("\nEl atleta no es apto para la prueba.")
