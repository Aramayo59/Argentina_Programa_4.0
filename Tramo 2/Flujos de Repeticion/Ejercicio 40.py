
a = int(input("Ingrese el primer número entero (a): "))
b = int(input("Ingrese el segundo número entero (b): "))


if a > b:
    a, b = b, a


suma_pares = 0
producto_impares = 1
hay_impares = False


for i in range(a, b + 1):
    if i % 2 == 0:
        suma_pares += i
    else:
        producto_impares *= i
        hay_impares = True

print("La suma de los números pares entre", a, "y", b, "es:", suma_pares)


if hay_impares:
    print("El producto de los números impares entre", a, "y", b, "es:", producto_impares)
else:
    print("No hay números impares entre", a, "y", b)
