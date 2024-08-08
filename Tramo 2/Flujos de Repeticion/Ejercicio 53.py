
nombre_mas_joven = None
edad_mas_joven = float('inf')


nombre = input("Ingresa el nombre de la persona ('*' para terminar): ")

while nombre != "*":
    edad = int(input("Ingresa la edad de {}: ".format(nombre)))
    if edad < edad_mas_joven:
        nombre_mas_joven = nombre
        edad_mas_joven = edad
    nombre = input("Ingresa el nombre de la persona ('*' para terminar): ")


if nombre_mas_joven:
    print("La persona más joven es:", nombre_mas_joven)
else:
    print("No se ingresaron personas.")
