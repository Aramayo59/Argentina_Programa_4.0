
opcion = input("¿Deseás continuar? [S/N]: ")


while opcion != 'S' and opcion != 's' and opcion != 'N' and opcion != 'n':
    print("Opción inválida. Debe ser 'S', 's', 'N' o 'n'.")
    opcion = input("¿Deseás continuar? [S/N]: ")


if opcion == 'S' or opcion == 's':
    print("Has elegido continuar.")
else:
    print("Has elegido no continuar.")
