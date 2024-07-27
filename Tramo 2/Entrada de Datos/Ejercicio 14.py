ancho = float(input("Ingrese el ancho del terreno en metros: "))

largo = float(input("Ingrese el largo del terreno en metros: "))

valor_metro_cuadrado = float(input("Ingrese el valor del metro cuadrado de tierra: "))

area_terreno = ancho * largo

valor_total = area_terreno * valor_metro_cuadrado

print("El valor total del terreno es: $" + str(round(valor_total, 2)))


perimetro = 2 * (ancho + largo)

alambre_1_metro = perimetro * 1
alambre_2_metros = perimetro * 2
alambre_3_metros = perimetro * 3


print("Metros de alambre necesarios para cercar a 1 metro de altura: " + str(round(alambre_1_metro, 2)) + " metros")
print("Metros de alambre necesarios para cercar a 2 metros de altura: " + str(round(alambre_2_metros, 2)) + " metros")
print("Metros de alambre necesarios para cercar a 3 metros de altura: " + str(round(alambre_3_metros, 2)) + " metros")
