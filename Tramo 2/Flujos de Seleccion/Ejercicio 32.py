
TARIFA_MINIMA = 50
TARIFA_0_10KM = 20
TARIFA_10KM_MAS = 15


km = float(input("Ingrese la cantidad de kilómetros que desea recorrer: "))


precio = TARIFA_MINIMA


if km > 10:
    precio += km * TARIFA_10KM_MAS
if km <= 10 and km > 0:
    precio += km * TARIFA_0_10KM


print("El precio del viaje es: $", precio)
