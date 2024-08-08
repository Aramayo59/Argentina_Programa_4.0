
numero = int(input("Ingrese un número entero positivo: "))


if numero < 0:
    print("Debe ingresar un número entero positivo.")
else:
   
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i

   
    print("El factorial de", numero, "es", factorial)
