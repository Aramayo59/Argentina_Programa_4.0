
num1 = float(input("Ingrese el valor para num1: "))
num2 = float(input("Ingrese el valor para num2: "))

print("Valores iniciales:")
print("num1 =", num1)
print("num2 =", num2)

num1, num2 = num2, num1

print("Valores después del intercambio:")
print("num1 =", num1)
print("num2 =", num2)
