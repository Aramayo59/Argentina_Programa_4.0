
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))


if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1


if menor != 0:  
    if mayor % menor == 0:
        print("El número", mayor, "es divisible por", menor)
    else:
        print("El número", mayor, "no es divisible por", menor)
else:
    print("El número menor es cero, no se puede dividir por cero.")
