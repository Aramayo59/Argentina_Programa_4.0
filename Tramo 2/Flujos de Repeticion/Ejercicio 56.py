#
edades_menores_18 = []
edades_mayores_18 = []

edad = int(input("Ingrese una edad (999 para finalizar): "))


while edad != 999:
    
    if 0 <= edad <= 100:
        if edad < 18:
            edades_menores_18.append(edad)
        else:
            edades_mayores_18.append(edad)
    else:
        print("Edad no válida. Debe estar entre 0 y 100.")

    
    edad = int(input("Ingrese una edad (999 para finalizar): "))


def calcular_promedio(edades):
    if len(edades) > 0:
        return sum(edades) / len(edades)
    return 0

num_menores_18 = len(edades_menores_18)
promedio_menores_18 = calcular_promedio(edades_menores_18)


num_mayores_18 = len(edades_mayores_18)
promedio_mayores_18 = calcular_promedio(edades_mayores_18)


print("Número de personas menores de 18 años:", num_menores_18)
print("Promedio de edad de personas menores de 18 años:", promedio_menores_18)
print("Número de personas de 18 años o más:", num_mayores_18)
print("Promedio de edad de personas de 18 años o más:", promedio_mayores_18)
