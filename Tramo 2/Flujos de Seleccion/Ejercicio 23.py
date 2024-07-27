
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))


if numero_uno >= numero_dos and numero_uno >= numero_tres:
    mayor = numero_uno
    if numero_dos >= numero_tres:
        medio = numero_dos
        menor = numero_tres
    else:
        medio = numero_tres
        menor = numero_dos
elif numero_dos >= numero_uno and numero_dos >= numero_tres:
    mayor = numero_dos
    if numero_uno >= numero_tres:
        medio = numero_uno
        menor = numero_tres
    else:
        medio = numero_tres
        menor = numero_uno
else:
    mayor = numero_tres
    if numero_uno >= numero_dos:
        medio = numero_uno
        menor = numero_dos
    else:
        medio = numero_dos
        menor = numero_uno


print("El mayor es:", mayor)
print("El medio es:", medio)
print("El menor es:", menor)
