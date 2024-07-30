
maximo = None


numero = int(input("Ingrese un número entero (0 para terminar): "))


while numero != 0:
    if maximo is None or numero > maximo:
        maximo = numero
    numero = int(input("Ingrese un número entero (0 para terminar): "))


if maximo is not None:
    print("El número máximo ingresado es:", maximo)
else:
    print("No se ingresaron números.")
