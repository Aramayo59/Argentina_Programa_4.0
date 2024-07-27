
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))


if numero1 >= numero2:
    if numero1 >= numero3:
        mayor = numero1
    else:
        mayor = numero3
else:
    if numero2 >= numero3:
        mayor = numero2
    else:
        mayor = numero3


print("El número mayor es:", mayor)
