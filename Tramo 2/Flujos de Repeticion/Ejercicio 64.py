
cantidad_maxima = 0
comida_maxima = 0
total_alimento = 0
numero_comida = 0


for i in range(1, 4):
    cantidad_comida = 0
    seguir_comiendo = 'S'
    
    while seguir_comiendo == 'S':
        alimento = int(input("Ingrese la cantidad de alimento en kg para la comida {}: ".format(i)))
        cantidad_comida += alimento
        seguir_comiendo = input("¿El animal quiere seguir comiendo? (S/N): ").upper()
    
    if cantidad_comida > cantidad_maxima:
        cantidad_maxima = cantidad_comida
        comida_maxima = i
    
    total_alimento += cantidad_comida
    numero_comida += 1


promedio_alimento = total_alimento / numero_comida if numero_comida > 0 else 0


print("La comida en la tanda {} fue la que el animal comió más cantidad de alimento con {} kg.".format(comida_maxima, cantidad_maxima))
print("Total de alimento recibido: {} kg".format(total_alimento))
print("Promedio de alimento por tanda: {} kg".format(int(promedio_alimento)))

