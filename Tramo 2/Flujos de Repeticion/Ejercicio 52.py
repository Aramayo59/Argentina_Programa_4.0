
estaturas = []
suma_estaturas = 0
cantidad_jugadores = 0


estatura = input("Ingresa la estatura del jugador (0 para terminar): ")


while estatura == "0" or estatura > "0" or estatura < "0":
    if estatura == "0":
        estatura = "0"  # Para salir del bucle
    else:
        estatura = float(estatura)
        estaturas.append(estatura)
        suma_estaturas += estatura
        cantidad_jugadores += 1
        estatura = input("Ingresa la estatura del jugador (0 para terminar): ")


if cantidad_jugadores > 0:
    estatura_promedio = suma_estaturas / cantidad_jugadores
    print("La estatura promedio del equipo es:", round(estatura_promedio, 2), "metros")
else:
    print("No se ingresaron estaturas.")
