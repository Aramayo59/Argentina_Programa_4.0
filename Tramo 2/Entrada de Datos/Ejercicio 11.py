
nombre1 = input("Ingrese el nombre del socio 1: ")
capital1 = float(input("Ingrese el capital aportado por " + nombre1 + ": "))

nombre2 = input("Ingrese el nombre del socio 2: ")
capital2 = float(input("Ingrese el capital aportado por " + nombre2 + ": "))

nombre3 = input("Ingrese el nombre del socio 3: ")
capital3 = float(input("Ingrese el capital aportado por " + nombre3 + ": "))


total_capital = capital1 + capital2 + capital3


porcentaje1 = (capital1 / total_capital) * 100
porcentaje2 = (capital2 / total_capital) * 100
porcentaje3 = (capital3 / total_capital) * 100


print("Valor total aportado: " + str(round(total_capital, 2)))
print(nombre1 + " aportó: " + str(round(porcentaje1, 2)) + "%")
print(nombre2 + " aportó: " + str(round(porcentaje2, 2)) + "%")
print(nombre3 + " aportó: " + str(round(porcentaje3, 2)) + "%")
