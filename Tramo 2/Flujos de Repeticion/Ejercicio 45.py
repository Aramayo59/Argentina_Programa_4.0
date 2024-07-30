
A = int(input("Ingrese el número natural A: "))
B = int(input("Ingrese el número natural B: "))


resultado = 1


for _ in range(B):
    resultado *= A


print(A, "^", B, "=", resultado, "(producto de", A, "multiplicado", B, "veces)")
