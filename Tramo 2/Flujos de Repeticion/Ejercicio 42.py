
suma = 0
cantidad = 0


numero = int(input("Ingrese un número entero (0 para terminar): "))


while numero != 0:
    suma += numero
    cantidad += 1
    numero = int(input("Ingrese un número entero (0 para terminar): "))

if cantidad > 0:
    promedio = suma / cantidad
    print("El promedio de los números ingresados es:", promedio)
else:
    print("No se ingresaron números.")
